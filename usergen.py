#usergen
import random
import os
while True:
	USERINT1 = random.randint(1,500)
	U = str(USERINT1)
	os.system('echo '+ U)
	os.system('useradd ' + U)
	os.system('adduser ' + U + ' sudo')
	os.system('echo '+ U + ':Lolsecure2018! | chpasswd')
