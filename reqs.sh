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
sudo apt-get install -y python3 python3-pip nmap nikto curl gobuster git unzip wget gnome-screenshot

# Install Python packages
echo -e "${YELLOW}Installing required Python packages...${RESET}"
pip3 install requests pyautogui

# Get the current user's home directory
HOME_DIR=$(eval echo "~$USER")

# Check and create the necessary directories
echo -e "${YELLOW}Checking and creating directory structure if necessary...${RESET}"
if [ ! -d "$HOME_DIR/scripts/python/clickjack" ]; then
  mkdir -p "$HOME_DIR/scripts/python/clickjack"
fi

if [ ! -d "$HOME_DIR/scripts/bash/testssl" ]; then
  mkdir -p "$HOME_DIR/scripts/bash/testssl"
fi

# Download the clickjacking script
CLICKJACK_DIR="$HOME_DIR/scripts/python/clickjack"
echo -e "${YELLOW}Cloning the clickjacking script repository...${RESET}"
git clone https://github.com/nxkennedy/clickjack.git $CLICKJACK_DIR

# Ensure the main script is executable
echo -e "${YELLOW}Making sure the main script is executable...${RESET}"
chmod +x $CLICKJACK_DIR/clickjack.py

# Download testssl.sh script
echo -e "${YELLOW}Cloning the testssl.sh repository...${RESET}"
TESTSSL_DIR="$HOME_DIR/scripts/bash/testssl"
git clone https://github.com/drwetter/testssl.sh.git $TESTSSL_DIR

# Make testssl.sh executable
echo -e "${YELLOW}Making testssl.sh executable...${RESET}"
chmod +x $TESTSSL_DIR/testssl.sh

# Download the wordlist if not already present
WORDLIST_DIR="/usr/share/wordlists/SecLists/Discovery/DNS"
WORDLIST="$WORDLIST_DIR/subdomains-top1million-5000.txt"
if [ ! -f "$WORDLIST" ]; then
  echo -e "${YELLOW}Downloading wordlist...${RESET}"
  sudo mkdir -p $WORDLIST_DIR
  sudo wget https://github.com/danielmiessler/SecLists/raw/master/Discovery/DNS/subdomains-top1million-5000.txt -O $WORDLIST
fi

echo -e "${GREEN}All requirements installed and scripts set up successfully!${RESET}"
