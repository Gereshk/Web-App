Mid capstone SimpleCTF

Monday, January 1, 2024

6:41 PM

 

![](009_Mid_capstone_SimpleCTF_000.png){width="7.927083333333333in" height="6.34375in"}

-   ftp allowed login but only had a text file that said password was easy

 

-   ffuf on web server showed directory simple

    -   cms made simple found

    -   ![](009_Mid_capstone_SimpleCTF_001.png){width="11.447916666666666in" height="6.677083333333333in"}

0

-   [CMS Made Simple \< 2.2.10 - SQL Injection - PHP webapps Exploit (exploit-db.com)](https://www.exploit-db.com/exploits/46635)

    -   download and run with python 46635.py -u \[URL\] \--crack -w \[wordlist\]

 

![](009_Mid_capstone_SimpleCTF_002.png){width="4.625in" height="1.28125in"}

 

-   had to specify p 2222 for ssh since running non standard

![](009_Mid_capstone_SimpleCTF_003.png){width="5.625in" height="6.145833333333333in"}

 

-   when escalating sudo with vim, use sudo vim to open vim after and then type :shell to exit vim for a root bash shell

![](009_Mid_capstone_SimpleCTF_004.png){width="5.1875in" height="4.6875in"}
