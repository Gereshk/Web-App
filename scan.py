#!/usr/bin/python3

import os
import sys
import requests
import subprocess
from datetime import date

if os.geteuid() != 0: exit("run as sudo")
if not os.path.exists('logs'): os.makedirs('logs')

target = input("Enter the target website: ").replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
port = input("Enter the port (default is 443): ") or "443"
log = f"logs/{date.isoformat(date.today()).replace('-', '')}_{target}.log"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
wordlist = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt"
cmds = [
        f"nmap -T4 -A -vv -Pn {target}",
        f"nmap -p {port} --script http-auth,http-auth-finder {target}",
        f"nikto -p {port} -h {target}",
        f"curl -k https://{target}/Images",
        f"curl -k https://{target}/images",
        f"curl -k https://{target}/asdf",
        f"nmap -p {port} --script http-targetmap-generator {target}",
        f"script -c '/home/kaliuser/scripts/bash/testssl/testssl.sh https://{target}' -q /dev/null",
        f"gobuster vhost -u https://{target} -w {wordlist} --proxy {proxies['http']} -k"]

try:
    requests.get(f"https://{target}:{port}", verify=False)
except Exception:
    exit("can't reach target")

with open(log, 'a') as f:
    for cmd in cmds:
        print(f"RUNNING: {cmd}")
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = process.communicate()
        f.write(f"\n\nRUNNING: {cmd}\n{out.decode('utf-8')}\n")

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
