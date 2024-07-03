#!/usr/bin/python3

import os
import sys
import requests
import subprocess
from datetime import date
import time
import pyautogui
import webbrowser
import threading

# ANSI escape codes for colored output
RED, GREEN, YELLOW, BLUE, RESET = "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[0m"

def run_clickjack_test(url):
    html_content = '''
    <html>
        <head><title>Clickjacking Test Page</title></head>
        <body>
            <h1>Clickjacking Test Results</h1>
            <h2>Target: <a href="{url}">{url}</a></h2>
            <h3>If you see the target website rendered below, it is <font color="red">VULNERABLE</font>.</h3>
            <iframe width="900" height="600" src="{url}"></iframe>
            <iframe style="position: absolute; left: 20px; top: 250px; opacity: 0.8; background: AliceBlue; font-weight: bold;" src="cj-attacker.html"></iframe>
        </body>
    </html>
    '''.format(url=url)

    attacker_content = '''
    <html>
        <div style="opacity: 1.0; left: 10px; top: 50px; background: PapayaWhip; font-weight: bold;">
            <center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a><br>(normally invisible)</center>
        </div>
    </html>
    '''

    with open('cj-target.html', 'w') as t, open('cj-attacker.html', 'w') as a:
        t.write(html_content)
        a.write(attacker_content)

    webbrowser.open('file://' + os.path.abspath('cj-target.html'))
    print('\n[+] Test Complete!')

def run_command(cmd, header, log_file):
    with open(log_file, 'a') as f:
        print(f"{YELLOW}RUNNING: {header}{RESET}")
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = process.communicate()
        f.write(f"\n\n{header}\n{out.decode('utf-8')}\n")
        print(f"{GREEN}Completed: {header}{RESET}")

def run_clickjack(cmd, log_file, log_dir):
    run_clickjack_test(cmd)
    print(f"{YELLOW}Taking a screenshot in 5 seconds...{RESET}")
    time.sleep(5)
    screenshot_path = f"{log_dir}/clickjack_screenshot.png"
    try:
        pyautogui.screenshot(screenshot_path)
        os.chmod(screenshot_path, 0o666)
        print(f"{GREEN}Screenshot taken and saved to {screenshot_path}{RESET}")
    except Exception as e:
        print(f"{RED}Failed to take screenshot: {e}{RESET}")

if os.geteuid() != 0: exit(f"{RED}run as sudo{RESET}")

# Prompt user for target website and port
target = input(f"{BLUE}Enter the target website: {RESET}").replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
port = input(f"{BLUE}Enter the port (default is 443): {RESET}") or "443"

# Create log directory with appropriate permissions
log_dir = f"logs/{target}"
os.makedirs(log_dir, mode=0o755, exist_ok=True)
log_file = f"{log_dir}/{date.today().isoformat().replace('-', '')}_{target}.log"
os.chmod(log_file, 0o666)  # Ensure the log file is writable by all users

cmds = {
    "1": ("Full Nmap Scan", f"nmap -T4 -A -vv -Pn {target}", "FULL NMAP RESULTS"),
    "2": ("Nmap Auth Scripts", f"nmap -p {port} --script http-auth,http-auth-finder {target}", "NMAP AUTH SCRIPT RESULTS"),
    "3": ("Nikto Web Scanner", f"nikto -p {port} -h {target}", "NIKTO WEB SCANNER RESULTS"),
    "4": ("CURL - Check Images Directory", f"curl -k https://{target}/Images", "CURL IMAGES DIRECTORY RESULTS"),
    "5": ("CURL - Check lowercase images Directory", f"curl -k https://{target}/images", "CURL LOWERCASE IMAGES DIRECTORY RESULTS"),
    "6": ("CURL - Check Random Path", f"curl -k https://{target}/asdf", "CURL RANDOM PATH RESULTS"),
    "7": ("Nmap Site Map Generator", f"nmap -p {port} --script http-sitemap-generator {target}", "NMAP SITE MAP GENERATOR RESULTS"),
    "8": ("Run TestSSL.sh", f"script -c '/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}:{port}' -q /dev/null", "TESTSSL.SH RESULTS"),
    "9": ("Gobuster Subdomain Scan", f"gobuster vhost -u https://{target} -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --proxy http://127.0.0.1:8080 -k", "GOBUSTER SUBDOMAIN SCAN RESULTS"),
    "10": ("Run Clickjacking Test", f"https://{target}:{port}", "CLICKJACKING TEST RESULTS")
}

# Display options to the user with colors
print(f"{YELLOW}Select the commands to run (separate choices with commas) or type 'all' to run everything:{RESET}")
options = {key: desc for key, (desc, _, _) in cmds.items()}
for key, desc in options.items():
    print(f"{BLUE}{key}{RESET}: {desc}")
selected_options = input(f"{BLUE}Your choice: {RESET}")

# Determine which commands to run
if selected_options.lower() == "all":
    selected_cmds = [(cmd, header) for _, cmd, header in cmds.values()]
else:
    selected_cmds = [(cmds[opt.strip()][1], cmds[opt.strip()][2]) for opt in selected_options.split(",") if opt.strip() in cmds]

# Ping the target to check if it is up
print(f"{YELLOW}Pinging the target {target}...{RESET}")
ping_process = subprocess.Popen(f"ping -c 4 {target}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
ping_out, _ = ping_process.communicate()
if ping_process.returncode != 0:
    exit(f"{RED}Ping failed. Target is down or unreachable.{RESET}")
print(f"{GREEN}Ping successful. Target is up.{RESET}")

# Check if the target is reachable on the specified port
print(f"{YELLOW}Checking if the target {target} on port {port} is reachable...{RESET}")
try:
    requests.get(f"https://{target}:{port}", verify=False)
    print(f"{GREEN}Target is reachable on port {port}.{RESET}")
except Exception:
    exit(f"{RED}Can't reach target on port {port}.{RESET}")

# Run the selected commands and log the output using threading
threads = []
for cmd, header in selected_cmds:
    if "Clickjacking" in header:
        t = threading.Thread(target=run_clickjack, args=(cmd, log_file, log_dir))
    else:
        t = threading.Thread(target=run_command, args=(cmd, header, log_file))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

if selected_options.lower() == "all":
    print(f"{YELLOW}Gathering headers and cookies from the target...{RESET}")
    resp = requests.get(f"https://{target}", proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}, verify=False)
    with open(log_file, 'a') as f:
        f.write("\nHEADERS\n")
        for header, value in resp.headers.items():
            if header.upper() == 'CONTENT-SECURITY-POLICY':
                f.write(f"{header}\n")
                for c in value.split(";"):
                    f.write(f"\t{c}\n")
            else:
                f.write(f"{header} : {value}\n")

        f.write("\nCOOKIES\n")
        for cookie, value in resp.cookies.items():
            f.write(f"{cookie} : {value}\n")
    print(f"{GREEN}Headers and cookies have been logged.{RESET}")

# Ensure all files in the log directory are writable by all users
for root, dirs, files in os.walk(log_dir):
    for name in dirs:
        os.chmod(os.path.join(root, name), 0o755)
    for name in files:
        os.chmod(os.path.join(root, name), 0o666)

print(f"{BLUE}Scanning and logging completed. Check the log file at {log_file}.{RESET}")
