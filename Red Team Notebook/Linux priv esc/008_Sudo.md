Sudo

Monday, January 1, 2024

3:05 PM

-   shell escapes

    -   [GTFOBins](https://gtfobins.github.io/)

    -   sudo -l

    -   find the services in GTFOBins

    -   vim example (after exploit use sudo vim to open vim, and then :shell in vim to exit to bash shell)

        -   ![](008_Sudo_000.png){width="8.479166666666666in" height="3.7604166666666665in"}

    -   awk example

        -   ![](008_Sudo_001.png){width="8.541666666666666in" height="1.8645833333333333in"}

 

-   good refresher

    -   [TryHackMe \| Linux PrivEsc](https://tryhackme.com/room/linuxprivesc)

>  

-   escalation via intended functionality

    -   ![](008_Sudo_002.png){width="4.614583333333333in" height="2.2604166666666665in"}

        -   apache not in gtfobins but try to google

        -   [Abusing SUDO (Linux Privilege Escalation) - Touhid\'s Blog (touhidshaikh.com)](https://touhidshaikh.com/blog/2018/04/abusing-sudo-linux-privilege-escalation/)

        -   ![](008_Sudo_003.png){width="11.822916666666666in" height="0.9791666666666666in"}

        -   quick example of cracking the hash with john

            -   ![](008_Sudo_004.png){width="12.104166666666666in" height="3.3541666666666665in"}

 

-   escalation via LD_PRELOAD

    -   ![](008_Sudo_005.png){width="3.9791666666666665in" height="0.6354166666666666in"}

    -   LD_PRELOAD is a feature of the ld (dynamic linker)

    -   able to preload an execute our own malicious library before anything else

    -   on vulnerable machine make file shell.c

        -   ![](008_Sudo_006.png){width="2.4375in" height="2.3854166666666665in"}

    -   compile

        -   ![](008_Sudo_007.png){width="5.645833333333333in" height="0.5in"}

    -   run preload with sudo for anything we have sudo privs on, make sure to use full path to shell.so

        -   ![](008_Sudo_008.png){width="4.8125in" height="0.78125in"}

 

-   CVE-2019-14287

    -   <https://www.exploit-db.com/exploits/47502>

    -   after sudo -l look for

        -   ALL=(ALL, !root} /bin/bash

        -   can take over any user id but can only use once so use wisely

 

-   CVE-2019-18634

    -   <https://github.com/saleemrashid/sudo-cve-2019-18634>

    -   pwfeedback is the asterisks that display when typing password like after sudo su

    -   ElementaryOS and Linux Mint often have this on by default

    -   sudo -l, cat /etc/sudoers and see pwfeedback or sudo -V to see if sudo version is vulnerable to CVE. asterisks after su or sudo su is also an indicator

    -   [GitHub - saleemrashid/sudo-cve-2019-18634: Proof of Concept for CVE-2019-18634](https://github.com/saleemrashid/sudo-cve-2019-18634)

        -   this is only one a few exploits written for this vulnerability

        -   upload and compile with gcc -o \[OUTPUT FILE\] INPUT FILE\]

        -   in this case ./exploit to run

        -   ![](008_Sudo_009.png){width="3.1041666666666665in" height="1.28125in"}

>  

-    
