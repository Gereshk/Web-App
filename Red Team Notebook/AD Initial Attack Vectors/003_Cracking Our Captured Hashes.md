Cracking Our Captured Hashes

Saturday, September 30, 2023

8:30 PM

 

\*Simulating an event by using the frankcastle machine to connect to a share that doesn\'t exist on our attacker machine. [\\\\10.0.2.15](file://10.0.2.15) to connect to our own machine from file explorer

 

![](003_Cracking_Our_Captured_Hashes_000.png){width="12.635416666666666in" height="6.09375in"}

 

 

 

-   Copy and paste hash into a file. Example hashes.txt (Entire hash highlighted above with user name and all)

> ![](003_Cracking_Our_Captured_Hashes_001.png){width="6.395833333333333in" height="0.5104166666666666in"}
>
> Generally not best practice to crack on your VM. Pentesting firms have cracking rigs with many GPUs. Better on metal.
>
>  

-   To find code for hash type

> ![](003_Cracking_Our_Captured_Hashes_002.png){width="8.666666666666666in" height="1.9375in"}

 

-   Run

> ![](003_Cracking_Our_Captured_Hashes_003.png){width="6.802083333333333in" height="0.8125in"}
>
>  

-   Cracked

-   ![](003_Cracking_Our_Captured_Hashes_004.png){width="17.270833333333332in" height="4.5in"}

>  
>
>  
>
> Run with \--show to see again
>
> ![](003_Cracking_Our_Captured_Hashes_005.png){width="17.34375in" height="1.28125in"}
>
>  

-   NTLM V1 doesn't change V2 changes every time you capture

 

-   Rockyou2021 96gb file

 

-   Explore rulesets -O with hashcat
