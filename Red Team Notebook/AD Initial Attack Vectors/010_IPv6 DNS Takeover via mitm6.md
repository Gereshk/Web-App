IPv6 DNS Takeover via mitm6

Wednesday, October 4, 2023

7:27 PM

Setup ntlmrelayx.py -6 (for ipv6)

![](010_IPv6_DNS_Takeover_via_mitm6_000.png){width="12.947916666666666in" height="3.9791666666666665in"}

The lootme at the end is a folder you setup. It can be named anything.

 

Run mitm6 and we are now mitm

Example: Sudo mitm6 -d marvel.local

![](010_IPv6_DNS_Takeover_via_mitm6_001.png){width="12.197916666666666in" height="7.875in"}

 

\*DO NOT RUN AND WALK AWAY \> ONLY USE IN SMALL SPRINTS 5-10 MIN\*

 

As computers reboot, or people login etc., lootme will capture the information

![](010_IPv6_DNS_Takeover_via_mitm6_002.png){width="15.854166666666666in" height="3.4166666666666665in"}

 

![](010_IPv6_DNS_Takeover_via_mitm6_003.png){width="17.4375in" height="2.125in"}

 

![](010_IPv6_DNS_Takeover_via_mitm6_004.png){width="17.375in" height="4.34375in"}

Notice the password in the description for SQLService account.

Look at last login and changes. Never logged in can signal honeypot.

 

Capturing Domain Admin creates new user also

![](010_IPv6_DNS_Takeover_via_mitm6_005.png){width="12.84375in" height="5.9375in"}

 

![](010_IPv6_DNS_Takeover_via_mitm6_006.png){width="9.604166666666666in" height="5.59375in"}

 

**\*Created user can access enterprise admins group and can run secretsdump.py and dump entire secrets of domain.\***

![](media/image8.png){width="7.854166666666667in" height="0.34375in"}
