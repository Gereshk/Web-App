#!/bin/bash

# Define colors for output
RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
BLUE="\033[94m"
RESET="\033[0m"

echo -e "${BLUE}Starting the installation process...${RESET}"

# Update package list
echo -e "${YELLOW}Updating package list...${RESET}"
sudo apt-get update -y

# Install required packages
echo -e "${YELLOW}Installing required packages...${RESET}"
sudo apt-get install -y python3 python3-pip nmap nikto curl gobuster git unzip wget

# Install Python packages
echo -e "${YELLOW}Installing required Python packages...${RESET}"
pip3 install requests pyautogui

# Download the clickjacking script
CLICKJACK_DIR="/home/kaliuser/scripts/python/clickjack"
echo -e "${YELLOW}Cloning the clickjacking script repository...${RESET}"
git clone https://github.com/nxkennedy/clickjack.git $CLICKJACK_DIR

# Ensure the main script is executable
echo -e "${YELLOW}Making sure the main script is executable...${RESET}"
chmod +x /home/kaliuser/scripts/python/clickjack/clickjack.py

# Create directory structure if not exists
echo -e "${YELLOW}Creating directory structure...${RESET}"
mkdir -p /home/kaliuser/scripts/bash/testssl

# Download testssl.sh script
echo -e "${YELLOW}Downloading testssl.sh script...${RESET}"
wget https://github.com/drwetter/testssl.sh/archive/refs/heads/3.0-dev.zip -O /tmp/testssl.zip
unzip /tmp/testssl.zip -d /home/kaliuser/scripts/bash/testssl
mv /home/kaliuser/scripts/bash/testssl/testssl.sh-3.0-dev/* /home/kaliuser/scripts/bash/testssl/
rm -rf /home/kaliuser/scripts/bash/testssl/testssl.sh-3.0-dev
rm /tmp/testssl.zip

# Download the wordlist if not already present
WORDLIST_DIR="/usr/share/wordlists/SecLists/Discovery/DNS"
WORDLIST="$WORDLIST_DIR/subdomains-top1million-5000.txt"
if [ ! -f "$WORDLIST" ]; then
  echo -e "${YELLOW}Downloading wordlist...${RESET}"
  sudo mkdir -p $WORDLIST_DIR
  sudo wget https://github.com/danielmiessler/SecLists/raw/master/Discovery/DNS/subdomains-top1million-5000.txt -O $WORDLIST
fi

echo -e "${GREEN}All requirements installed and scripts set up successfully!${RESET}"
