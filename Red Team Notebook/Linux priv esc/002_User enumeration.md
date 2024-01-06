User enumeration

Saturday, December 30, 2023

8:56 PM

 

-   whoami

 

-   id

    -   User id, groups

 

-   sudo -l

    -   What we can run as root

 

-   history

    -   can sometimes have good reveals

 

-   sudo su -

    -   try and switch to root

 

-   cat /etc/passwd

    -   cat /etc/passwd \| cut -d : -f 1

        -   cuts out everything else except users

    -   see users

 

-   cat /etc/shadow

    -   displays password hashes if you have privs

 

-   cat /etc/group

    -   shows groups

 
