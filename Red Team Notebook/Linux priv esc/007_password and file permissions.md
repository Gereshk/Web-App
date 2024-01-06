password and file permissions

Saturday, December 30, 2023

10:39 PM

-   stored passwords

    -   history can be your easy win

    -   cat .bash_history also

        -   example

            -   ![](007_password_and_file_permissions_000.png){width="4.28125in" height="1.0833333333333333in"}

    -   [PayloadsAllTheThings/Methodology and Resources/Linux - Privilege Escalation.md at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#looting-for-passwords)

    -   linpeas and linenum finds these also

    -   don\'t forget to check things right in front of you

        -   notes in files

        -   VPN files

            -   example

                -   ![](007_password_and_file_permissions_001.png){width="5.59375in" height="4.708333333333333in"}

        -   creds in webserver

 

-   weak file permissions

    -   ls -la /etc/passwd

    -   ls -la /etc/shadow

    -   lots we can do if we can modify /etc/pass /etc/shadow

        -   linpeas will pick this up

        -   change root hash

        -   remove root x for no pass

        -   change group

        -   unshadow

            -   unshadow passwd shadow

            -   run through hashcat

                -   use windows machine to run on gpu

 

-   SSH keys

    -   [PayloadsAllTheThings/Methodology and Resources/Linux - Privilege Escalation.md at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#ssh-key)

        -   find / -name authorized_keys 2\> /dev/null

        -   find / -name id_rsa 2\> /dev/null

        -   if you find cat out and copy into your own id_rsa

            -   chmod 600 before using

            -   example: ssh -I id_rsa root@x.x.x.x

>  
