#usergen
import random
import os
os.system('echo bin:Lolsecure2018! | chpasswd')
os.system('adduser bin sudo')
os.system('chsh -s /bin/bash bin')
os.system('echo sys:Lolsecure2018! | chpasswd')
os.system('adduser sys sudo')
os.system('chsh -s /bin/bash sys')
os.system('echo sync:Lolsecure2018! | chpasswd')
os.system('adduser sync sudo')
os.system('chsh -s /bin/bash sync')
os.system('echo games:Lolsecure2018! | chpasswd')
os.system('adduser games sudo')
os.system('chsh -s /bin/bash games')
os.system('echo man:Lolsecure2018! | chpasswd')
os.system('adduser man sudo')
os.system('chsh -s /bin/bash man')
os.system('echo lp:Lolsecure2018! | chpasswd')
os.system('adduser lp sudo')
os.system('chsh -s /bin/bash lp')
os.system('echo mail:Lolsecure2018! | chpasswd')
os.system('adduser mail sudo')
os.system('chsh -s /bin/bash mail')
os.system('echo news:Lolsecure2018! | chpasswd')
os.system('adduser news sudo')
os.system('chsh -s /bin/bash news')
os.system('echo uucp:Lolsecure2018! | chpasswd')
os.system('adduser uucp sudo')
os.system('chsh -s /bin/bash uucp')
os.system('echo proxy:Lolsecure2018! | chpasswd')
os.system('adduser proxy sudo')
os.system('chsh -s /bin/bash proxy')
os.system('echo backup:Lolsecure2018! | chpasswd')
os.system('adduser backup sudo')
os.system('chsh -s /bin/bash backup')
os.system('echo list:Lolsecure2018! | chpasswd')
os.system('adduser list sudo')
os.system('chsh -s /bin/bash list')
os.system('echo irc:Lolsecure2018! | chpasswd')
os.system('adduser irc sudo')
os.system('chsh -s /bin/bash irc')
os.system('echo gnats:Lolsecure2018! | chpasswd')
os.system('adduser gnats sudo')
os.system('chsh -s /bin/bash gnats')
os.system('echo nobody:Lolsecure2018! | chpasswd')
os.system('adduser nobody sudo')
os.system('chsh -s /bin/bash nobody')
os.system("sed 's/\/usr\/sbin\/nologin/\/bin\/sh/g' /etc/passwd")





x = 1
while x < 50:
	#USERINT1 = random.randint(1,50)
	#U = str(USERINT1)
	U = str(x)
	os.system('echo '+ U)
	os.system('useradd ' + U)
	os.system('adduser ' + U + ' sudo')
	os.system('echo '+ U + ':Lolsecure2018! | chpasswd')
	x = x + 1
