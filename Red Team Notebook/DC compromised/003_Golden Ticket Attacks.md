Golden Ticket Attacks

Saturday, October 14, 2023

2:59 PM

-   Get Mimikatz running and set privilege to debug

> ![](003_Golden_Ticket_Attacks_000.png){width="7.614583333333333in" height="4.21875in"}
>
>  

-   Run lsadump::lsa /inject /name:krbtgt to dump only the krbtgt hashes

> ![](003_Golden_Ticket_Attacks_001.png){width="8.260416666666666in" height="9.322916666666666in"}
>
>  
>
>  

-   We want sid of domain

> ![](003_Golden_Ticket_Attacks_002.png){width="5.552083333333333in" height="1.0in"}
>
> And NTLM hash of krbtgt accoun**t**
>
> ![](003_Golden_Ticket_Attacks_003.png){width="4.40625in" height="1.59375in"}
>
>  

-   Paste into notepad

> ![](003_Golden_Ticket_Attacks_004.png){width="3.875in" height="1.3333333333333333in"}
>
>  

-   Command /User can be anything, Domain must be correct, id:500 is for admin, ptt is pass the ticket

> ![](003_Golden_Ticket_Attacks_005.png){width="10.03125in" height="0.5625in"}
>
>  
>
> ![](003_Golden_Ticket_Attacks_006.png){width="10.854166666666666in" height="3.3541666666666665in"}
>
>  

-   Misc::cmd in Mimikatz opens up new

-   ![](003_Golden_Ticket_Attacks_007.png){width="7.6875in" height="2.6354166666666665in"}

 

-   Able to run dir for PUNISHER machine

> ![](003_Golden_Ticket_Attacks_008.png){width="5.270833333333333in" height="3.40625in"}
>
>  
>
> To take things a step further if you can download psexec to the compromised machine or its already there, you can get a shell for the other machine on the domain
>
> ![](003_Golden_Ticket_Attacks_009.png){width="6.78125in" height="2.9791666666666665in"}

 

![](003_Golden_Ticket_Attacks_010.png){width="4.71875in" height="3.0729166666666665in"}

-   Golden ticket is picked up less than creating a user. Also look up silver ticket.
