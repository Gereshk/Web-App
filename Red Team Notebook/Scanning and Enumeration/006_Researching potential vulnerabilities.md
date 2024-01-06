Researching potential vulnerabilities

Thursday, April 27, 2023

9:48 PM

 

-   Transfer notes from note pad to note taking app. I will probably use OneNote but other options are available.

 

-   CVEDETAILS good for quick check and scores

 

-   Rapid 7 is a good hit when googling (Metasploit)

 

-   Searchsploit from command line if no internet or just because

 

80/443 open default web page Apache PHP 11:43pm

Apache/1.3.20 Server information disclosure 404 page -documentation link

information disclosure 404 page

information disclosure server headsers disclosed

 

mod_ssl/2.8.4 - mod_ssl 2.8.7 and lower are vulnerable to a remote buffer overflow which may allow a remote shell.

\+ ///etc/hosts: The server install allows reading of any system file by adding an extra \'/\' to the URL.

\+ /usage/: Webalizer may be installed. Versions lower than 2.01-09 vulnerable to Cross Site Scripting (XSS). See: <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0835>

 

 

webalizer version 2.01

<http://10.0.2.4/usage/usage_202304.html>

 

SMB

Unix (Samba 2.2.1a)

 

SSH

OpenSSH 2.9p2

 

 

-   80/443/139 juiciest in that order

-   80/443 Potentially vulnerable to OpenLuck [Apache mod_ssl \< 2.8.7 OpenSSL - \'OpenFuckV2.c\' Remote Buffer Overflow (1) - Unix remote Exploit (exploit-db.com)](https://www.exploit-db.com/exploits/764), [heltonWernik/OpenLuck: OpenFuck exploit updated to linux 2018 - Apache mod_ssl \< 2.8.7 OpenSSL - Remote Buffer Overflow (github.com)](https://github.com/heltonWernik/OpenLuck)

-   139 Potentially vulnerable to trans2open [Samba trans2open Overflow (Linux x86) (rapid7.com)](https://www.rapid7.com/db/modules/exploit/linux/samba/trans2open/), [Samba 2.2.x - Remote Buffer Overflow - Linux remote Exploit (exploit-db.com)](https://www.exploit-db.com/exploits/7), [Samba \< 2.2.8 (Linux/BSD) - Remote Code Execution - Multiple remote Exploit (exploit-db.com)](https://www.exploit-db.com/exploits/10)

-   Webalizer 2.01 Potentially vulnerable [Web vulnerabilities to gain access to the system (exploit-db.com)](https://www.exploit-db.com/papers/13017)

-   SSH 2.9p2 potentially vulnerable to SSH User code execution [SSH User Code Execution (rapid7.com)](https://www.rapid7.com/db/modules/exploit/multi/ssh/sshexec/), Kerberos 4 TGT/AFS Token Buffer Overflow [OpenSSH 2.x/3.x - Kerberos 4 TGT/AFS Token Buffer Overflow - Linux remote Exploit (exploit-db.com)](https://www.exploit-db.com/exploits/21402)

 

 

 

 
