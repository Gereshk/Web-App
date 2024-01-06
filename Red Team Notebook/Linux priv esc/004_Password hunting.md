Password hunting

Saturday, December 30, 2023

9:31 PM

-   grep \--color=auto -rnw \'/\' -ie \"PASSWORD\" \--color=always 2\> /dev/null

    -   finds work password and shows in red

    -   all try \"PASSWORD=\"

 

-   locate password \| more

    -   also try passwd, pass, pwd

 

-   find / -name id_rsa 2\> /dev/null

    -   authorized_keys
