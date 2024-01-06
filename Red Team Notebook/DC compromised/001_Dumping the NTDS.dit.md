Dumping the NTDS.dit

Friday, October 13, 2023

11:44 PM

![](001_Dumping_the_NTDS.dit_000.png){width="11.6875in" height="3.3229166666666665in"}

 

 

 

secretsdump.py MARVEL.local/hawkeye:\'Password1@\'@10.0.2.250

![](001_Dumping_the_NTDS.dit_001.png){width="11.354166666666666in" height="9.90625in"}

 

Can dump just ntds.dit with flag -just-dc-ntlm

![](001_Dumping_the_NTDS.dit_002.png){width="9.635416666666666in" height="3.8229166666666665in"}

 

\*Can copy hashes to excel sheet and organize data (data tab, text to columns, set custom) with a delimiter of : to easily pull the NT portion of the hash only to crack\*

\*Watch video for organizing passwords to hashes in excel after you crack\*

 

Crack with hashcat if you can (m -1000)

 

Don\'t bother cracking PC hashes, focus on users.

![](media/image4.png){width="9.614583333333334in" height="3.40625in"}![](media/image5.png){width="0.125in" height="0.2916666666666667in"}
