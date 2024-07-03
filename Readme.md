# Web Reconnaissance Script
This script performs a series of reconnaissance tasks on a target web server. It can run various tools such as nmap, nikto, curl, gobuster, and custom scripts like testssl.sh and clickjack.py. It logs the results and takes a screenshot if the clickjacking test completes successfully.

## Prerequisites
Before running the script, make sure you have the following installed:

- Python 3.x
- requests library for Python: pip install requests
- nmap: Install using sudo apt-get install nmap
- nikto: Install using sudo apt-get install nikto
- curl: Install using sudo apt-get install curl
- gobuster: Install using sudo apt-get install gobuster
- testssl.sh: Download and install
- clickjack.py: Download from nxkennedy/clickjack
  
## Installation
Clone this repository or copy the script to your local machine.

```sh
git clone https://github.com/your-repo/web-recon-script.git
cd web-recon-script
Ensure the script is executable:
```

```sh
chmod +x script_name.py
Install testssl.sh:
```
```sh
git clone https://github.com/drwetter/testssl.sh.git
cd testssl.sh
chmod +x testssl.sh
```

### Install clickjack.py:

```sh
git clone https://github.com/nxkennedy/clickjack.git
Move testssl.sh and clickjack.py to the appropriate directories:
```

Place testssl.sh in /home/kaliuser/scripts/bash/testssl/
Place clickjack.py in /home/kaliuser/scripts/python/clickjack/

Place the main script in a directory of your choice.

It is recommended to place it in a directory that is part of your PATH for easy execution.

## Usage
Run the script with sudo:

```sh
sudo ./script_name.py
```

Options
When you run the script, you will be prompted to enter the target website and port. You will then be presented with a list of commands that you can choose to run. You can select specific commands by entering their numbers separated by commas or type all to run all available commands.

### Example
```bash
Enter the target website: example.com
Enter the port (default is 443): 8080

Select the commands to run (separate choices with commas) or type 'all' to run everything:
1: nmap -T4 -A -vv -Pn example.com
2: nmap -p 8080 --script http-auth,http-auth-finder example.com
3: nikto -p 8080 -h example.com
4: curl -k https://example.com/Images
5: curl -k https://example.com/images
6: curl -k https://example.com/asdf
7: nmap -p 8080 --script http-targetmap-generator example.com
8: script -c '/home/kaliuser/scripts/bash/testssl/testssl.sh https://example.com:8080' -q /dev/null
9: gobuster vhost -u https://example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --proxy http://127.0.0.1:8080 -k
10: python3 /home/kaliuser/scripts/bash/clickjack/clickjack.py example.com

Your choice: all
```

### Features
Ping Test: Checks if the target is up before proceeding.
Reachability Check: Ensures the target is reachable on the specified port.
Command Execution: Runs selected or all commands and logs the output.
Clickjacking Test: Runs a clickjacking test and takes a screenshot if the test completes successfully.
Logging: Logs are saved in a directory named after the target inside the logs directory.
Logging
Logs are saved in a subdirectory inside the logs directory, named after the target website. Each log file is timestamped with the date of execution.

Example log directory structure:

```bash

logs/
└── example.com/
    └── 20230701_example.com.log
    └── clickjack_screenshot.png
```

### Notes
Make sure to run the script as sudo to ensure all commands have the necessary permissions.
Adjust the paths to testssl.sh and clickjack.py if they are located in different directories on your system.
