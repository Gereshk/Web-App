Pass Attacks Overview

Saturday, October 7, 2023

8:31 PM

 

![](000_Pass_Attacks_Overview_000.png){width="13.479166666666666in" height="7.15625in"}

 

Pass the password crackmapexec

![](000_Pass_Attacks_Overview_001.png){width="7.65625in" height="3.25in"}

 

 

Pass the hash crackmapexec

![](000_Pass_Attacks_Overview_002.png){width="7.34375in" height="3.3541666666666665in"}

 

SAM [What is the Windows Security Accounts Manager (SAM)? (techtarget.com)](https://www.techtarget.com/searchenterprisedesktop/definition/Security-Accounts-Manager)

![](000_Pass_Attacks_Overview_003.png){width="11.21875in" height="6.9375in"}

Shares

![](000_Pass_Attacks_Overview_004.png){width="13.96875in" height="4.1875in"}

 

Built in modules

![](000_Pass_Attacks_Overview_005.png){width="10.5in" height="7.09375in"}

 

Lsa (will dump in secrets dump so you don't have to run)

![](000_Pass_Attacks_Overview_006.png){width="7.114583333333333in" height="1.53125in"}

\*Can try and crack these dcc2 hashes but may be old login

![](000_Pass_Attacks_Overview_007.png){width="17.40625in" height="6.6875in"}

 

Dump lsass with lsassy

![](000_Pass_Attacks_Overview_008.png){width="11.791666666666666in" height="6.1875in"}

(Local Security Authority Subsystem Service (LSASS)\[1\] is a process in Microsoft Windows operating systems that is responsible for enforcing the security policy on the system. It verifies users logging on to a Windows computer or server, handles password changes, and creates access tokens.\[2\] It also writes to the Windows Security Log.

 

Forcible termination of lsass.exe will result in the system losing access to any account, including NT AUTHORITY, prompting a restart of the machine.

 

Because lsass.exe is a crucial system file, its name is often faked by malware. The lsass.exe file used by Windows is located in the directory %WINDIR%\\System32 and the description of the file is Local Security Authority Process. If it is running from any other location, that lsass.exe is most likely a virus, spyware, trojan or worm. Due to the way some systems display fonts, malicious developers may name the file something like Isass.exe (capital \"i\" instead of a lowercase \"L\") in efforts to trick users into installing or executing a malicious file instead of the trusted system file.\[3\] The Sasser worm spreads by exploiting a buffer overflow in the LSASS on Windows XP and Windows 2000 operating systems.

Crack map exec database stores all info)

 

Crack map exec database cmedb

![](000_Pass_Attacks_Overview_009.png){width="12.072916666666666in" height="5.53125in"}
