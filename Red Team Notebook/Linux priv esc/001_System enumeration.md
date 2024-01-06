System enumeration

Saturday, December 30, 2023

8:26 PM

 

-   hostname

    -   Can be an indicator

 

-   uname -a

    -   More info to check OS for vulnerabilities

 

-   cat /proc/version

    -   Exact kernel version, name of user who compiled kernel, host name for where it happened, version of GCC compiler used for building kernel, type of kernel, date and time kernel was built

 

-   cat /etc/issue

    -   Distribution

 

-   lscpu

    -   Cpu info

 

-   ps aux

    -   See running services

    -   Ps aux \| grep root

        -   Root users processes. Can substitute any users.
