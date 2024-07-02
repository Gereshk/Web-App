#!/usr/bin/python3

import os
import sys
import requests
import subprocess
from datetime import date
import time
import pyautogui

# ANSI escape codes for colored output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

if os.geteuid() != 0: exit(f"{RED}run as sudo{RESET}")

# Prompt user for target website and port
target = input(f"{BLUE}Enter the target website: {RESET}").replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
port = input(f"{BLUE}Enter the port (default is 443): {RESET}") or "443"

# Create log directory for the target
log_dir = f"logs/{target}"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log = f"{log_dir}/{date.isoformat(date.today()).replace('-', '')}_{target}.log"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
wordlist = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt"
testssl_cmd = f"/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}:{port}" if port != "443" else f"/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}"

cmds = {
    "1": f"nmap -T4 -A -vv -Pn {target}",
    "2": f"nmap -p {port} --script http-auth,http-auth-finder {target}",
    "3": f"nikto -p {port} -h {target}",
    "4": f"curl -k https://{target}/Images",
    "5": f"curl -k https://{target}/images",
    "6": f"curl -k https://{target}/asdf",
    "7": f"nmap -p {port} --script http-targetmap-generator {target}",
    "8": f"script -c '{testssl_cmd}' -q /dev/null",
    "9": f"gobuster vhost -u https://{target} -w {wordlist} --proxy {proxies['http']} -k",
    "10": f"python3 /home/kaliuser/scripts/bash/clickjack/clickjack.py {target}"
}

# Display options to the user
print(f"{YELLOW}Select the commands to run (separate choices with commas) or type 'all' to run everything:{RESET}")
for key, cmd in cmds.items():
    print(f"{key}: {cmd}")

selected_options = input(f"{BLUE}Your choice: {RESET}")

# Determine which commands to run
if selected_options.lower() == "all":
    selected_cmds = cmds.values()
else:
    selected_cmds = [cmds[opt.strip()] for opt in selected_options.split(",") if opt.strip() in cmds]

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
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = process.communicate()
        output = out.decode('utf-8')
        f.write(f"\n\nRUNNING: {cmd}\n{output}\n")
        print(f"{GREEN}Completed: {cmd}{RESET}")
        
        # Check for "Test Complete!" in the clickjack script output
        if "clickjack" in cmd and "Test Complete!" in output:
            print(f"{YELLOW}Taking screenshot of the Firefox browser...{RESET}")
            time.sleep(5)  # Wait for the browser to load completely
            screenshot_path = f"{log_dir}/clickjack_screenshot.png"
            pyautogui.screenshot(screenshot_path)
            print(f"{GREEN}Screenshot taken and saved to {screenshot_path}{RESET}")

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
