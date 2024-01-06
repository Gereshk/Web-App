SQL Injection Blind

Wednesday, October 18, 2023

1:32 PM

 

Adding <http://localhost> to target scope and filtering any traffic outside of that so burp doesn\'t get messy.

 

-   Testing logging in with default creds just to see our http history. We can see user and pass in POST request

> ![](009_SQL_Injection_Blind_000.png){width="13.260416666666666in" height="8.666666666666666in"}
>
> Session cookie may be valuable
>
>  
>
> We can see it in the next GET request as well
>
> ![](009_SQL_Injection_Blind_001.png){width="4.864583333333333in" height="3.2604166666666665in"}
>
>  

-   You can send POST to repeater and send along to view different reactions like 1928 is a valid login in the Content-Length and 2122 is invalid

> ![](009_SQL_Injection_Blind_002.png){width="13.3125in" height="5.96875in"}
>
>  
>
> ![](009_SQL_Injection_Blind_003.png){width="10.479166666666666in" height="4.5625in"}
>
>  

-   Render can be useful too see also

> ![](009_SQL_Injection_Blind_004.png){width="5.1875in" height="6.1875in"}
>
>  

-   Trying simple payload on username jeremy\' or 1=1# but since it\'s in body also highlight and right click \> encode with ctrl + u or encode\>URL\>encode key characters. Ctrl+Shift+U to decode.

 

-   Select the entire request so we can get ready to automate

> ![](009_SQL_Injection_Blind_005.png){width="5.25in" height="3.8229166666666665in"}
>
>  
>
> ![](009_SQL_Injection_Blind_006.png){width="2.0729166666666665in" height="0.625in"}
>
>  
>
> ![](009_SQL_Injection_Blind_007.png){width="2.3229166666666665in" height="0.6354166666666666in"}
>
>  
>
> ![](009_SQL_Injection_Blind_008.png){width="8.510416666666666in" height="4.4375in"}
>
> Long story short no bueno
>
>  

-   Options here for manual testing to continue. In this case we are moving back on to cookie in the next GET request.

> ![](009_SQL_Injection_Blind_009.png){width="5.239583333333333in" height="4.90625in"}
>
> Send it to repeater
>
> ![](009_SQL_Injection_Blind_010.png){width="7.3125in" height="8.375in"}
>
> Send in repeater. We can see the 1027 and the Welcome to your dashboard.
>
>  

-   Try altering cookie with SQL statements

    -   Cookie: session=6967cabefd763ac1a1a88e11159957db\' and 1=1#

> ![](009_SQL_Injection_Blind_011.png){width="14.416666666666666in" height="7.65625in"}
>
> The response still showing a valid login even with the SQL statement added indicates that this app is vulnerable to SQL injection.
>
>  
>
>  
>
> With blind SQL we need to try and find payloads that produce true false outputs and slowly extract data.
>
> <https://www.w3schools.com/sql/func_mysql_substring.asp>
>
>  
>
>  

-   We get a true with ookie: session=6967cabefd763ac1a1a88e11159957db\' and substring(\'a\', 1, 1) = \'a\'#

> ![](009_SQL_Injection_Blind_012.png){width="14.604166666666666in" height="4.03125in"}
>
>  
>
> We can slowly add characters and change the length and starting position
>
> ![](009_SQL_Injection_Blind_013.png){width="14.625in" height="3.1041666666666665in"}
>
>  
>
> We can see we are getting a pass on 8 being the first number when we pull the version of the database.
>
> ![](009_SQL_Injection_Blind_014.png){width="14.604166666666666in" height="2.8854166666666665in"}
>
>  
>
> As we keep going
>
> ![](009_SQL_Injection_Blind_015.png){width="14.59375in" height="2.6041666666666665in"}
>
>  
>
> ![](009_SQL_Injection_Blind_016.png){width="11.09375in" height="2.7291666666666665in"}
>
>  
>
>  

-   We can go after a password now

> ![](009_SQL_Injection_Blind_017.png){width="10.822916666666666in" height="2.5729166666666665in"}
>
> Send to intruder with the updated SQL statement
>
> Cookie: session=6967cabefd763ac1a1a88e11159957db\' and substring((select password from injection0x02 where username = \'jessamy\'), 1, 1) = \'a\'#
>
>  

-   Set up proper payload position

> ![](009_SQL_Injection_Blind_018.png){width="14.1875in" height="3.8229166666666665in"}
>
>  
>
> Set up payload of a-z and 1-0
>
> ![](009_SQL_Injection_Blind_019.png){width="5.427083333333333in" height="3.2604166666666665in"}
>
>  
>
> We can see z stands out
>
> ![](009_SQL_Injection_Blind_020.png){width="5.8125in" height="2.6354166666666665in"}
>
>  
>
>  

-   With sqlmap

> ![](009_SQL_Injection_Blind_021.png){width="2.3229166666666665in" height="0.6354166666666666in"}
>
>  
>
> ![](009_SQL_Injection_Blind_022.png){width="6.625in" height="3.875in"}
>
>  
>
> ![](009_SQL_Injection_Blind_023.png){width="3.0416666666666665in" height="0.5104166666666666in"}
>
>  
>
> ![](009_SQL_Injection_Blind_024.png){width="8.46875in" height="1.71875in"}
>
> Can copy and use payload or
>
> ![](009_SQL_Injection_Blind_025.png){width="5.052083333333333in" height="0.6875in"}
>
>  
>
> ![](009_SQL_Injection_Blind_026.png){width="8.729166666666666in" height="8.166666666666666in"}
>
>  
