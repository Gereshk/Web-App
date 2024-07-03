#!/usr/bin/python3

import os
import sys
import requests
import subprocess
from datetime import date
import time
import pyautogui
import webbrowser

# ANSI escape codes for colored output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def run_clickjack_test(url):
    html = '''
    <html>
        <head>
            <title>Clickjacking Test Page</title>
        </head>
        <body>
            <h1>Clickjacking Test Results</h1>
            <h2>Target: <a href="{url}">{url}</a></h2>
            <h3>If you see the target website rendered below, it is <font color="red">VULNERABLE</font>.</h3>
            <iframe width="900" height="600" src="{url}"></iframe>
            <iframe style="position: absolute; left: 20px; top: 250px; opacity: 0.8; background: AliceBlue; font-weight: bold;" src="cj-attacker.html"></iframe>
        </body>
    </html>
    '''.format(url=url)

    html2 = '''
    <html>
        <div style="opacity: 1.0; left: 10px; top: 50px; background: PapayaWhip; font-weight: bold;">
            <center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a>
            <br>(normally invisible)</center>
        </div>
    </html>
    '''

    cjt = os.path.abspath('cj-target.html')
    cja = os.path.abspath('cj-attacker.html')
    localurl = 'file://' + cjt

    with open(cjt, 'w') as t, open(cja, 'w') as a:
        t.write(html)
        a.write(html2)

    webbrowser.open(localurl)
    print('\n[+] Test Complete!')

if os.geteuid() != 0: exit(f"{RED}run as sudo{RESET}")

# Prompt user for target website and port
target = input(f"{BLUE}Enter the target website: {RESET}").replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
port = input(f"{BLUE}Enter the port (default is 443): {RESET}") or "443"

# Create log directory for the target with appropriate permissions
log_dir = f"logs/{target}"
if not os.path.exists(log_dir):
    os.makedirs(log_dir, mode=0o777)

log = f"{log_dir}/{date.isoformat(date.today()).replace('-', '')}_{target}.log"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
wordlist = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt"
testssl_cmd = f"/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}:{port}" if port != "443" else f"/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}"

cmds = {
    "1": ("Full Nmap Scan", f"nmap -T4 -A -vv -Pn {target}"),
    "2": ("Nmap Auth Scripts", f"nmap -p {port} --script http-auth,http-auth-finder {target}"),
    "3": ("Nikto Web Scanner", f"nikto -p {port} -h {target}"),
    "4": ("CURL - Check Images Directory", f"curl -k https://{target}/Images"),
    "5": ("CURL - Check lowercase images Directory", f"curl -k https://{target}/images"),
    "6": ("CURL - Check Random Path", f"curl -k https://{target}/asdf"),
    "7": ("Nmap Target Map Generator", f"nmap -p {port} --script http-targetmap-generator {target}"),
    "8": ("Run TestSSL.sh", f"script -c '{testssl_cmd}' -q /dev/null"),
    "9": ("Gobuster Subdomain Scan", f"gobuster vhost -u https://{target} -w {wordlist} --proxy {proxies['http']} -k"),
    "10": ("Run Clickjacking Test", target)
}

# Display options to the user
print(f"{YELLOW}Select the commands to run (separate choices with commas) or type 'all' to run everything:{RESET}")
for key, (desc, _) in cmds.items():
    print(f"{key}: {desc}")

selected_options = input(f"{BLUE}Your choice: {RESET}")

# Determine which commands to run
if selected_options.lower() == "all":
    selected_cmds = [cmd for _, cmd in cmds.values()]
    run_all = True
else:
    selected_cmds = [cmds[opt.strip()][1] for opt in selected_options.split(",") if opt.strip() in cmds]
    run_all = False

# Ping the target to check if it is up
print(f"{YELLOW}Pinging the target {target}...{RESET}")
ping_cmd = f"ping -c 4 {target}"
ping_process = subprocess.Popen(ping_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
ping_out, _ = ping_process.communicate()
if ping_process.returncode == 0:
    print(f"{GREEN}Ping successful. Target is up.{RESET}")
else:
    exit(f"{RED}Ping failed. Target is down or unreachable.{RESET}")

# Check if the target is reachable on the specified port
print(f"{YELLOW}Checking if the target {target} on port {port} is reachable...{RESET}")
try:
    requests.get(f"https://{target}:{port}", verify=False)
    print(f"{GREEN}Target is reachable on port {port}.{RESET}")
except Exception:
    exit(f"{RED}Can't reach target on port {port}.{RESET}")

# Run the selected commands and log the output
with open(log, 'a') as f:
    for cmd in selected_cmds:
        print(f"{YELLOW}RUNNING: {cmd}{RESET}")
        if cmd == target:
            run_clickjack_test(f"https://{target}:{port}")
            print(f"{YELLOW}Taking a screenshot in 5 seconds...{RESET}")
            time.sleep(5)  # Wait for 5 seconds
            screenshot_path = f"{log_dir}/clickjack_screenshot.png"
            try:
                pyautogui.screenshot(screenshot_path)
                print(f"{GREEN}Screenshot taken and saved to {screenshot_path}{RESET}")
            except Exception as e:
                print(f"{RED}Failed to take screenshot: {e}{RESET}")
        else:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, _ = process.communicate()
            output = out.decode('utf-8')
            f.write(f"\n\nRUNNING: {cmd}\n{output}\n")
            print(f"{GREEN}Completed: {cmd}{RESET}")

    if run_all:
        print(f"{YELLOW}Gathering headers and cookies from the target...{RESET}")
        resp = requests.get(f"https://{target}", proxies=proxies, verify=False)

        headers = resp.headers
        f.write("\nHEADERS\n")
        for header in headers:
            if header.upper() == 'CONTENT-SECURITY-POLICY':
                csp = headers[header].split(";")
                f.write(f"{header}\n")
                for c in csp:
                    f.write(f"\t{c}\n")
            else:
                f.write(f"{header} : {headers[header]}\n")

        cookies = resp.cookies
        f.write("\nCOOKIES\n")
        for cookie in cookies.get_dict():
            f.write(f"{cookie} : {cookies.get_dict()[cookie]}")
        print(f"{GREEN}Headers and cookies have been logged.{RESET}")

print(f"{BLUE}Scanning and logging completed. Check the log file at {log}.{RESET}")
