# Web Reconnaissance Script

# This is a work in progress

This repository contains a Python script that automates various web application security testing tasks, including Nmap scans, Nikto scans, TestSSL checks, Clickjacking tests, and header and cookie gathering. The script logs the output of each test and includes functionality for taking screenshots during clickjacking tests.

## Features

- Full Nmap Scan
- Nmap Auth Scripts
- Nmap Site Map Generator
- Nmap Stored XSS Scan
- Nikto Web Scanner
- CURL checks for specific directories
- TestSSL.sh for SSL/TLS security checks
- Gobuster Subdomain Scan
- Clickjacking Test with screenshot functionality
- Header and Cookie Gathering

## Prerequisites

Before running the main script, you need to install the required dependencies and set up the environment. This can be done using the provided installation script.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gereshk/Web-App.git
   cd Web-App
   ```
   2. Run the installation script:

    ```bash
    chmod +x reqs.sh
    sudo ./reqs.sh
    ```

## Usage

Ensure you have the necessary permissions to run the script (it should be run with `sudo`):

```bash
chmod +x scan.py
sudo ./scan.py
```

Follow the prompts to enter the target website and port. The default port is 443 if not specified.

Select the commands to run by typing the corresponding numbers separated by commas, or type 'all' to run all commands. You can also choose to skip the Nikto scan if running all commands.

The script will perform the selected tests, log the output, and save the log files in a directory named after the target website under the `logs` folder. For example, if your target is `example.com`, the logs will be saved in `logs/example.com`.

## Screenshots

During the Clickjacking test, a screenshot will be taken and saved in the same log directory.

## Logs

Logs are detailed and include colored output for easier reading. Each log file is named with the date and target website for easy reference.

## Example

Here is an example of running the script:

```bash
sudo ./scan.py
```

You will be prompted to enter the target website and port, and then to select the commands to run. The script will handle the rest, including taking screenshots and saving logs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## Acknowledgements

- [SecLists](https://github.com/danielmiessler/SecLists) for the wordlists.
- [testssl.sh](https://github.com/drwetter/testssl.sh) for the SSL testing tool.
- [Clickjack](https://github.com/nxkennedy/clickjack) for the clickjacking test script.
