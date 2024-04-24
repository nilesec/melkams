#!/bin/bash

#varialbes
set -e 

cyan='\e[0;36m'
lightcyan='\e[96m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
#v2


unset melkam os architecture kernelrelease internalip externalip nameserver loadaverage



if [[ $# -eq 0 ]]
then
{
melkam=$(tput sgr0)

echo -e $red"      ####################################################################################################"
echo -e "      #                                                                                                  #"
echo -e "      # $yellow                      Well come to The melkam os security analayzer $red                              #"
echo -e $red"      #                                                                                                  #"
echo -e "      #                                                                                                  #"
echo -e "      #                                                                                                  #"
echo -e "      #                                                                                                  #"
echo -e "      ####################################################################################################\n"

echo -e $yellow"###############################################################################################"
cat /etc/os-release | grep 'NAME\|VERSION' | grep -v 'VERSION_ID' | grep -v 'PRETTY_NAME' > /tmp/osrelease
echo -n -e '\E[32m'"OS Name :" $melkam  && cat /tmp/osrelease | grep -v "VERSION" | cut -f2 -d\"
echo -n -e '\E[32m'"OS Version :" $melkam && cat /tmp/osrelease | grep -v "NAME" | cut -f2 -d\"


# Check Architecture
architecture=$(uname -m)
echo -e '\E[32m'"Architecture :" $melkam $architecture


# Check Kernel Release
kernelrelease=$(uname -r)
echo -e '\E[32m'"Kernel Release :" $melkam $kernelrelease

# Check hostname
echo -e '\E[32m'"Hostname :" $melkam $HOSTNAME
echo -e $yellow"###############################################################################################"

# Check Internal IP
internalip=$(hostname -I)
echo -e '\E[32m'"Internal IP :" $melkam $internalip

# Check External IP
externalip=$(curl -s ipecho.net/plain;echo)
echo -e '\E[32m'"External IP : $melkam "$externalip

# Check DNS
nameservers=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')
echo -e '\E[32m'"Name Servers :" $melkam $nameservers 

# Check Logged In Users
who>/tmp/who
echo -e '\E[32m'"Logged In users :" $melkam && cat /tmp/who 
echo -e $yellow"###############################################################################################"

# Check RAM and SWAP Usages
free -h | grep -v + > /tmp/ramcache
echo -e '\E[32m'"Ram Usages :" $melkam
cat /tmp/ramcache | grep -v "Swap"
echo -e '\E[32m'"Swap Usages :" $melkam
cat /tmp/ramcache | grep -v "Mem"
echo -e $yellow"###############################################################################################"
# Check Disk Usages
df -h| grep 'Filesystem\|/dev/sda*' > /tmp/diskusage
echo -e '\E[32m'"Disk Usages :" $melkam 
cat /tmp/diskusage
echo -e $yellow"###############################################################################################"

# Check Load Average
loadaverage=$(top -n 1 -b | grep "load average:" | awk '{print $10 $11 $12}')
echo -e '\E[32m'"Load Average :" $melkam $loadaverage

# Check System Uptime
tecuptime=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)
echo -e '\E[32m'"System Uptime Days/(HH:MM) :" $melkam $tecuptime
echo -e $yellow"###############################################################################################"
# Unset Variables
unset melkam os architecture kernelrelease internalip externalip nameserver loadaverage

# Remove Temporary Files
rm /tmp/osrelease /tmp/who /tmp/ramcache /tmp/diskusage


}
fi
shift $(($OPTIND -1))

