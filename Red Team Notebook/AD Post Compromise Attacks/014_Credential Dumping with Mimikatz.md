Credential Dumping with Mimikatz

Thursday, October 12, 2023

7:16 PM

 

[gentilkiwi/mimikatz: A little tool to play with Windows security (github.com)](https://github.com/gentilkiwi/mimikatz)

 

 

Latest release and DL trunk.zip or .7zip

![](014_Credential_Dumping_with_Mimikatz_000.png){width="4.96875in" height="0.3645833333333333in"}

 

Extract x64 files

\*I\'ve extracted all of them to /home/b33f/transfer/mimkatz

![](014_Credential_Dumping_with_Mimikatz_001.png){width="6.25in" height="4.9375in"}

 

 

Set up server

![](014_Credential_Dumping_with_Mimikatz_002.png){width="5.020833333333333in" height="1.8333333333333333in"}

 

 

Since we have access to the web browser we can open up to attacker machine and pull files

![](014_Credential_Dumping_with_Mimikatz_003.png){width="3.9791666666666665in" height="7.9375in"}

 

\*IF FILES ARE BLOCKED JUST OVERRIDE AND KEEP

 

![](014_Credential_Dumping_with_Mimikatz_004.png){width="6.739583333333333in" height="2.2916666666666665in"}

 

 

\*Open cmd as admin and cd to location of mimikatz

\*must be admin or NT Authority\\system - Download [PsTools - Sysinternals \| Microsoft Learn](https://learn.microsoft.com/en-us/sysinternals/downloads/pstools) , extract, cmd to extracted folder and run .\\PsExec64.exe -i -s cmd.exe

 

*From \<<https://www.reddit.com/r/oscp/comments/rn5wje/mimikatz/>\>*

 

Run

![](014_Credential_Dumping_with_Mimikatz_005.png){width="6.375in" height="4.864583333333333in"}

 

Most of the time we want to run privilege as debug

![](014_Credential_Dumping_with_Mimikatz_006.png){width="6.927083333333333in" height="1.9895833333333333in"}

 

Some things we can do

![](014_Credential_Dumping_with_Mimikatz_007.png){width="8.322916666666666in" height="4.84375in"}

 

![](014_Credential_Dumping_with_Mimikatz_008.png){width="12.166666666666666in" height="9.5625in"}

 

Admin password stored in clear text for share

![](014_Credential_Dumping_with_Mimikatz_009.png){width="3.2291666666666665in" height="1.0520833333333333in"}

 

-   Hashes are in there as well
