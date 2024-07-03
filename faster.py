# this is an attempt to make this script run faster

#!/usr/bin/python3

import os
import sys
import requests
import subprocess
from datetime import date
import time
import pyautogui
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# ANSI escape codes for colored output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Configuration
PROXIES = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
WORDLIST = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt"
TESTSSL_CMD_TEMPLATE = "/home/kaliuser/scripts/bash/testssl/testssl.sh https://{}:{}"
CLICKJACK_CMD_TEMPLATE = "python3 /home/kaliuser/scripts/python/clickjack/clickjack.py https://{}:{}"
LOG_DIR_TEMPLATE = "logs/{}"
LOG_FILE_TEMPLATE = "{}/{}_{}.log"

def run_command(desc, cmd, log_file):
    """Run a command and log its output."""
    with open(log_file, 'a') as f:
        f.write(f"\n{MAGENTA}{'='*10} RUNNING: {desc} {'='*10}{RESET}\n")
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = process.communicate()
        output = out.decode('utf-8')
        f.write(output)
        f.write(f"\n{MAGENTA}{'='*10} COMPLETED: {desc} {'='*10}{RESET}\n\n")
    return output

def clickjack_test(cmd, log_dir, log_file):
    """Run clickjacking test and take a screenshot."""
    print(f"{YELLOW}Running Clickjacking Test and taking a screenshot in 5 seconds...{RESET}")
    with open(log_file, 'a') as f:
        f.write(f"\n{MAGENTA}{'='*10} RUNNING: Clickjacking Test {'='*10}{RESET}\n")
    subprocess.Popen(cmd, shell=True)
    time.sleep(5)  # Wait for 5 seconds
    screenshot_path = f"{log_dir}/clickjack_screenshot.png"
    try:
        pyautogui.screenshot(screenshot_path)
        with open(log_file, 'a') as f:
            f.write(f"{GREEN}Screenshot taken and saved to {screenshot_path}{RESET}\n")
        print(f"{GREEN}Screenshot taken and saved to {screenshot_path}{RESET}")
    except Exception as e:
        error_message = f"{RED}Failed to take screenshot: {e}{RESET}"
        with open(log_file, 'a') as f:
            f.write(error_message)
        print(error_message)
    with open(log_file, 'a') as f:
        f.write(f"\n{MAGENTA}{'='*10} COMPLETED: Clickjacking Test {'='*10}{RESET}\n\n")

def ping_target(target):
    """Ping the target to check if it is up."""
    return subprocess.call(f"ping -c 1 {target}", shell=True) == 0

def check_target_reachable(target, port):
    """Check if the target is reachable on the specified port."""
    try:
        with requests.get(f"https://{target}:{port}", verify=False) as response:
            return True
    except Exception:
        return False

def gather_headers_and_cookies(target, log_file, proxies):
    """Gather headers and cookies from the target and log them."""
    with open(log_file, 'a') as f:
        f.write(f"\n{MAGENTA}{'='*10} GATHERING HEADERS AND COOKIES {'='*10}{RESET}\n")
    with requests.get(f"https://{target}", proxies=proxies, verify=False) as resp:
        with open(log_file, 'a') as f:
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
    with open(log_file, 'a') as f:
        f.write(f"\n{MAGENTA}{'='*10} COMPLETED: GATHERING HEADERS AND COOKIES {'='*10}{RESET}\n\n")
    print(f"{GREEN}Headers and cookies have been logged.{RESET}")

def main():
    if os.geteuid() != 0:
        exit(f"{RED}run as sudo{RESET}")

    # Prompt user for target website and port
    target = input(f"{BLUE}Enter the target website: {RESET}").replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
    port = input(f"{BLUE}Enter the port (default is 443): {RESET}") or "443"

    # Create log directory and file for the target
    log_dir = LOG_DIR_TEMPLATE.format(target)
    os.makedirs(log_dir, exist_ok=True)
    log_file = LOG_FILE_TEMPLATE.format(log_dir, date.today().strftime('%Y%m%d'), target)

    testssl_cmd = TESTSSL_CMD_TEMPLATE.format(target, port)
    clickjack_cmd = CLICKJACK_CMD_TEMPLATE.format(target, port)

    cmds = [
        ("Full Nmap Scan", f"nmap -T4 -A -vv -Pn {target}"),
        ("Nmap Auth Scripts", f"nmap -p {port} --script http-auth,http-auth-finder {target}"),
        ("Nmap Site Map Generator", f"nmap -p {port} --script http-sitemap-generator {target}"),
        ("Nmap Stored XSS Scan", f"nmap -p {port} --script http-stored-xss {target}"),
        ("Nikto Web Scanner", f"nikto -p {port} -h {target}"),
        ("CURL - Check Images Directory", f"curl -k https://{target}/Images"),
        ("CURL - Check lowercase images Directory", f"curl -k https://{target}/images"),
        ("CURL - Check Random Path", f"curl -k https://{target}/asdf"),
        ("Run TestSSL.sh", f"script -c '{testssl_cmd}' -q /dev/null"),
        ("Gobuster Subdomain Scan", f"gobuster vhost -u https://{target} -w {WORDLIST} --proxy {PROXIES['http']} -k"),
        ("Run Clickjacking Test", clickjack_cmd)
    ]

    # Display options to the user
    print(f"{YELLOW}Select the commands to run (separate choices with commas) or type 'all' to run everything:{RESET}")
    for i, (desc, _) in enumerate(cmds, start=1):
        color = CYAN if i % 2 == 0 else GREEN  # Alternate colors
        print(f"{color}{i}: {desc}{RESET}")

    selected_options = input(f"{BLUE}Your choice: {RESET}")

    # Determine which commands to run
    run_all = selected_options.lower() == "all"
    selected_cmds = [(desc, cmd) for i, (desc, cmd) in enumerate(cmds, start=1) if run_all or str(i) in selected_options.split(",")]

    # Ping the target to check if it is up
    print(f"{YELLOW}Pinging the target {target}...{RESET}")
    if not ping_target(target):
        exit(f"{RED}Ping failed. Target is down or unreachable.{RESET}")
    print(f"{GREEN}Ping successful. Target is up.{RESET}")

    # Check if the target is reachable on the specified port
    print(f"{YELLOW}Checking if the target {target} on port {port} is reachable...{RESET}")
    if not check_target_reachable(target, port):
        exit(f"{RED}Can't reach target on port {port}.{RESET}")
    print(f"{GREEN}Target is reachable on port {port}.{RESET}")

    # Run the selected commands and log the output
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(run_command, desc, cmd, log_file): desc for desc, cmd in selected_cmds if "clickjack" not in cmd}

        if run_all:
            print(f"{YELLOW}Gathering headers and cookies from the target...{RESET}")
            gather_headers_and_cookies(target, log_file, PROXIES)

        for future in as_completed(futures):
            desc = futures[future]
            try:
                future.result()
                print(f"{GREEN}Completed: {desc}{RESET}")
            except Exception as exc:
                print(f"{RED}Error running {desc}: {exc}{RESET}")

        if any("clickjack" in cmd for _, cmd in selected_cmds):
            clickjack_future = executor.submit(clickjack_test, clickjack_cmd, log_dir, log_file)
            try:
                clickjack_future.result()
            except Exception as exc:
                print(f"{RED}Error running Clickjacking Test: {exc}{RESET}")

    print(f"{BLUE}Scanning and logging completed. Check the log file at {log_file}.{RESET}")

if __name__ == "__main__":
    main()
