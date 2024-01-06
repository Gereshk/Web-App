Scripting with Bash

Sunday, March 19, 2023

10:25 PM

 

Ping sweep bash script

 

#!/bin/bash

if \[ \"\$1\" == \"\" \]

then

echo \"You forgot an IP address!\"

echo \"Syntax: ./ipsweep.sh 192.168.1\"

else

for ip in \`seq 1 254\`; do

ping -c 1 \$1.\$ip \| grep \"64 bytes\" \| cut -d \" \" -f 4 \| tr -d \":\" &

done

fi

 

 
