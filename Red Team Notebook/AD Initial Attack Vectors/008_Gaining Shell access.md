Gaining Shell access

Tuesday, October 3, 2023

7:01 PM

With a password \*REAL EXAMPLE NOTES BELOW THE STANDARD TUTORIALS

![](008_Gaining_Shell_access_000.png){width="12.166666666666666in" height="6.46875in"}

 

 

With a hash

-   Domain not needed with hash

-   LM and NT part of hash needed

![](008_Gaining_Shell_access_001.png){width="11.604166666666666in" height="6.9375in"}

 

\*REMEMBER TO CHECK TARGETS, AUTOMATIC MAY NOT WORK AND YOU CAN TRY POWERSHELL ETC.\*

\*METASPLOIT IS NOISY AND MAY BE PICKED UP IN PROD ENV\*

\*background to background shell, sessions to re-open\*

 

Psexec.py less likely to get picked up

With password

![](008_Gaining_Shell_access_002.png){width="9.0in" height="7.21875in"}

 

 

With hash

![](008_Gaining_Shell_access_003.png){width="12.729166666666666in" height="6.5625in"}

 

 

Fire up Metasploit (msfconsole)

Search psexec

![](008_Gaining_Shell_access_004.png){width="13.0625in" height="5.59375in"}

 

 

Select option -in this case \"use 4\"

![](008_Gaining_Shell_access_005.png){width="12.75in" height="5.927083333333333in"}

 

Set payload to 64 bit

![](008_Gaining_Shell_access_006.png){width="10.697916666666666in" height="1.5625in"}

 

Set options

![](008_Gaining_Shell_access_007.png){width="8.822916666666666in" height="3.1354166666666665in"}

 

May have to experiment with setting different targets

![](008_Gaining_Shell_access_008.png){width="6.21875in" height="3.2916666666666665in"}

 

 

Run and enjoy shell

![](008_Gaining_Shell_access_009.png){width="9.6875in" height="3.2604166666666665in"}

 

Using hash instead of password in metasploit/psexec

![](008_Gaining_Shell_access_010.png){width="12.854166666666666in" height="2.6875in"}

 

![](008_Gaining_Shell_access_011.png){width="9.385416666666666in" height="2.875in"}

 

Shell

![](008_Gaining_Shell_access_012.png){width="12.9375in" height="3.3229166666666665in"}

 

 

 

Using psexec.py instead of metasploit example

Psexec.py MARVEL/fcastle:\'Password1\'@10.0.2.220

![](008_Gaining_Shell_access_013.png){width="5.96875in" height="3.9479166666666665in"}

 

Can also enter password after with psexec.py (works well with funky passwords)

![](008_Gaining_Shell_access_014.png){width="7.34375in" height="1.625in"}

 

Psexec.py with hash instead of password

![](008_Gaining_Shell_access_015.png){width="10.90625in" height="3.1979166666666665in"}

 

Wmiexec.py another option

![](008_Gaining_Shell_access_016.png){width="11.25in" height="1.84375in"}

Smbexec.py another option

![](008_Gaining_Shell_access_017.png){width="11.53125in" height="1.65625in"}

 
