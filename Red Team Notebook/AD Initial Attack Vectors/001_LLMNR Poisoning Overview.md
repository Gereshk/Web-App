LLMNR Poisoning Overview

Wednesday, June 28, 2023

9:46 PM

 

-   Used to identify hosts when DNS fails to do so.

-   Link Local Multicast Name Resolution

-   Previously NBT-NS

-   Key flaw is that the service uses a user\'s username and NTLMv2 hash when appropriately responded to.

>  
>
> ![](001_LLMNR_Poisoning_Overview_000.png){width="8.729166666666666in" height="7.177083333333333in"}
>
>  
>
>  

-   Run Responder

```{=html}
<!-- -->
```
-   Sudo Responder -I tun0 -dwPv

```{=html}
<!-- -->
```
-   An event occurs

-   Get hashes

-   Crack hashes (hashcat or online)

```{=html}
<!-- -->
```
-   Hashcat -m 5600 hashes.txt rockyou.txt
