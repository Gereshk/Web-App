XSS Introduction

Thursday, October 19, 2023

7:25 PM

-   Execute JavaScript in a users browser and gives us control

>  
>
>  

-   Reflected

    -   Scripts you are trying to inject come from the current http request.

        -   [What is reflected XSS (cross-site scripting)? Tutorial & Examples \| Web Security Academy (portswigger.net)](https://portswigger.net/web-security/cross-site-scripting/reflected)

-   Stored

    -   More powerful. Payload stored in database.

        -   [What is stored XSS (cross-site scripting)? Tutorial & Examples \| Web Security Academy (portswigger.net)](https://portswigger.net/web-security/cross-site-scripting/stored)

-   DOM-based

    -   Client side has vulnerable JS.

        -   [What is DOM-based XSS (cross-site scripting)? Tutorial & Examples \| Web Security Academy (portswigger.net)](https://portswigger.net/web-security/cross-site-scripting/dom-based)

>  
>
>  

-   Good way to test but avoid the alert as it is filtered and caught much easier due to popularity

> ![](010_XSS_Introduction_000.png){width="14.791666666666666in" height="4.208333333333333in"}
>
>  
>
>  
>
> [JavaScript Tutorial (w3schools.com)](https://www.w3schools.com/js/)
