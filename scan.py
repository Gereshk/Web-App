#!/usr/bin/python3

import os
import sys
import requests
import subprocess
from datetime import date
import time
import pyautogui
import threading

# ANSI escape codes for colored output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

if os.geteuid() != 0:
    exit(f"{RED}run as sudo{RESET}")

# Prompt user for target website and port
target = input(f"{BLUE}Enter the target website: {RESET}").replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
port = input(f"{BLUE}Enter the port (default is 443): {RESET}") or "443"

# Create log directory for the target
log_dir = f"logs/{target}"
os.makedirs(log_dir, exist_ok=True)

log_file = f"{log_dir}/{date.today().strftime('%Y%m%d')}_{target}.log"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
wordlist = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt"
testssl_cmd = f"/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}:{port}" if port != "443" else f"/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}"
clickjack_cmd = f"python3 /home/kaliuser/scripts/python/clickjack/clickjack.py https://{target}:{port}" if port != "443" else f"python3 /home/kaliuser/scripts/python/clickjack/clickjack.py https://{target}"

cmds = [
    ("Full Nmap Scan", f"nmap -T4 -A -vv -Pn {target}"),
    ("Nmap Auth Scripts", f"nmap -p {port} --script http-auth,http-auth-finder {target}"),
    ("Nikto Web Scanner", f"nikto -p {port} -h {target}"),
    ("CURL - Check Images Directory", f"curl -k https://{target}/Images"),
    ("CURL - Check lowercase images Directory", f"curl -k https://{target}/images"),
    ("CURL - Check Random Path", f"curl -k https://{target}/asdf"),
    ("Nmap Site Map Generator", f"nmap -p {port} --script http-sitemap-generator {target}"),
    ("Run TestSSL.sh", f"script -c '{testssl_cmd}' -q /dev/null"),
    ("Gobuster Subdomain Scan", f"gobuster vhost -u https://{target} -w {wordlist} --proxy {proxies['http']} -k"),
    ("Run Clickjacking Test", clickjack_cmd)
]

# Display options to the user
print(f"{YELLOW}Select the commands to run (separate choices with commas) or type 'all' to run everything:{RESET}")
for i, (desc, _) in enumerate(cmds, start=1):
    print(f"{i}: {desc}")

selected_options = input(f"{BLUE}Your choice: {RESET}")

# Determine which commands to run
run_all = selected_options.lower() == "all"
selected_cmds = [cmd for i, (_, cmd) in enumerate(cmds, start=1) if run_all or str(i) in selected_options.split(",")]

# Function to run a command and log output
def run_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, _ = process.communicate()
    return out.decode('utf-8')

# Function to run clickjacking test and take a screenshot
def clickjack_test(cmd, log_dir):
    print(f"{YELLOW}Running Clickjacking Test and taking a screenshot in 5 seconds...{RESET}")
    subprocess.Popen(cmd, shell=True)
    time.sleep(5)  # Wait for 5 seconds
    screenshot_path = f"{log_dir}/clickjack_screenshot.png"
    try:
        pyautogui.screenshot(screenshot_path)
        print(f"{GREEN}Screenshot taken and saved to {screenshot_path}{RESET}")
    except Exception as e:
        print(f"{RED}Failed to take screenshot: {e}{RESET}")

# Ping the target to check if it is up
print(f"{YELLOW}Pinging the target {target}...{RESET}")
if subprocess.call(f"ping -c 1 {target}", shell=True) != 0:
    exit(f"{RED}Ping failed. Target is down or unreachable.{RESET}")
print(f"{GREEN}Ping successful. Target is up.{RESET}")

# Check if the target is reachable on the specified port
print(f"{YELLOW}Checking if the target {target} on port {port} is reachable...{RESET}")
try:
    with requests.get(f"https://{target}:{port}", verify=False) as response:
        print(f"{GREEN}Target is reachable on port {port}.{RESET}")
except Exception:
    exit(f"{RED}Can't reach target on port {port}.{RESET}")

# Run the selected commands and log the output
with open(log_file, 'a') as f:
    for cmd in selected_cmds:
        if "clickjack" in cmd:
            threading.Thread(target=clickjack_test, args=(cmd, log_dir)).start()
        else:
            print(f"{YELLOW}RUNNING: {cmd}{RESET}")
            output = run_command(cmd)
            f.write(f"\n\nRUNNING: {cmd}\n{output}\n")
            print(f"{GREEN}Completed: {cmd}{RESET}")

    if run_all:
        print(f"{YELLOW}Gathering headers and cookies from the target...{RESET}")
        with requests.get(f"https://{target}", proxies=proxies, verify=False) as resp:
            f.write("\nHEADERS\n")
            for header, value in resp.headers.items():
                if header.upper() == 'CONTENT-SECURITY-POLICY':
                    csp = value.split(";")
                    f.write(f"{header}\n")
                    for c in csp:
                        f.write(f"\t{c}\n")
                else:
                    f.write(f"{header} : {value}\n")
            
            f.write("\nCOOKIES\n")
            for cookie, value in resp.cookies.items():
                f.write(f"{cookie} : {value}\n")
        print(f"{GREEN}Headers and cookies have been logged.{RESET}")

print(f"{BLUE}Scanning and logging completed. Check the log file at {log_file}.{RESET}")
