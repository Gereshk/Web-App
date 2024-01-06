Domain Enumeration with ldapdomaindump

Friday, October 6, 2023

7:10 PM

-   We need to make a directory

![](001_Domain_Enumeration_with_ldapdomaindump_000.png){width="2.875in" height="1.25in"}

 

-   We need to cd to new directory we created

![](001_Domain_Enumeration_with_ldapdomaindump_001.png){width="3.4166666666666665in" height="1.25in"}

 

 

-   Example command: sudo /usr/bin/ldapdomaindump ldaps://10.0.2.250 -u \'MARVEL\\fcastle\' -p Password1

    -   Use -o to output to folder you created if you aren\'t running command from that directory

 

![](001_Domain_Enumeration_with_ldapdomaindump_002.png){width="8.947916666666666in" height="1.4895833333333333in"}

 

-   All very useful info. Computers, Users etc. check all info as time allows

![](001_Domain_Enumeration_with_ldapdomaindump_003.png){width="11.822916666666666in" height="1.34375in"}

 

-   Open files and view same info you received from MITM6

![](001_Domain_Enumeration_with_ldapdomaindump_004.png){width="4.59375in" height="0.9479166666666666in"}

Lots of valuable info -High value targets, admins, users, passwords from descriptions

![](001_Domain_Enumeration_with_ldapdomaindump_005.png){width="17.34375in" height="9.760416666666666in"}

 
