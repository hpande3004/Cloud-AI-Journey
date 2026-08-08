import Package_Modules
print (Package_Modules.add(10,15))
print (Package_Modules.subt(59,14))

from Package_Modules import add, subt
print(add(72, 56))
print(subt(9, 3))

from Package_Modules import *                   #Asterick to import everything

#Build in modules

import math                                     
print(math.sqrt(25))
print(math.pi)

import random
num = random.randint(1,10)
print(num)

import datetime
today = datetime.date.today()
print(today)