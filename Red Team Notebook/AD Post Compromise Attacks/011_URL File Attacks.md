URL File Attacks

Thursday, October 12, 2023

6:31 PM

 

[PayloadsAllTheThings/Methodology and Resources/Active Directory Attack.md at master · swisskyrepo/PayloadsAllTheThings (github.com)](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md#scf-and-url-file-attack-against-writeable-share)

 

Compromised user file share access. Can use responder to capture more hashes. Open file share works also.

 

Set up file to point at attacker. URL can be set to open something like google.

![](011_URL_File_Attacks_000.png){width="3.7604166666666665in" height="2.0416666666666665in"}

 

This @ naming convention makes our file appear at the top. We can name it something that matches the business or purpose so they are more likely to click. Quotes around the name \@corporatepay.url hide the url portion.

![](011_URL_File_Attacks_001.png){width="8.385416666666666in" height="6.1875in"}

 

 

 

 

-   Run responder

> ![](011_URL_File_Attacks_002.png){width="5.125in" height="3.8854166666666665in"}
>
>  
>
>  

-   User clicks our file

> ![](011_URL_File_Attacks_003.png){width="6.239583333333333in" height="3.7916666666666665in"}
