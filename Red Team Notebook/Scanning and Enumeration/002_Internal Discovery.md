Internal Discovery

Sunday, April 23, 2023

5:12 PM

 

-   Ping from VM reveals your IP

-   Sudo arp-scan -l shows machines on network

-   Netdiscover -r 192.168.1.0/24 example to arp network

>  
>
>  

-   Nmap -sS (stealth) does SYN SYNACK RST so doesn't establish connection

-   Nmap -T1-5 for speed 4 good default for course, vulnhub or ctf.

-   Nmap -p- all ports -p pick specific ports separate with commas

-   Nmap -A all information

-   \-- script vuln easy built in
