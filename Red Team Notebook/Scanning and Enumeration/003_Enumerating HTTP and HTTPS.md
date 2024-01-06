Enumerating HTTP and HTTPS

Sunday, April 23, 2023

11:36 PM

 

-   Go to web page if you find web server open

    -   Test page is automatic finding. Gives insight into poor hygiene.

    -   Links on default web page can give information disclosure

    -   Check source code for comments

 

Nikto

Nikto -h <http://10.0.2.4> example

-   Sometimes not good against good security

-   Pay attention to remote vs local

-   Save scan gedit or nano in txt file

 

 

Directory busting

 

-   Dirbuster

-   Dirb

-   Gobsuter

-   Ffuf (quick)

    -   Sample syntax ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt:FUZZ -u <http://10.0.2.15/FUZZ>

>  

Dirbuster& OWASP dirbuster gui use dirbuster& to open

![](003_Enumerating_HTTP_and_HTTPS_000.png){width="7.96875in" height="5.625in"}

 

Add multiple file types or change file type based on server type and info found. Apache runs php, Microsoft runs asp aspx etc.

 

-   Enumerate all findings

 

**Burp Suite**

-   **Capture request in proxy and send to repeater where you can resend and capture response in real time. Can also send different requests like POST etc.**
