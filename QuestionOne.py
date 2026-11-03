import time
import random
randomvar1=random.randrange(50,80)
randomvar2=random.randrange(50,80)
randomvar3=random.randrange(50,80)
randomvar4=random.randrange(50,80)
randomvar5=random.randrange(50,80)
randomvar6=random.randrange(50,80)
local_now = time.localtime()
timevar=(time.strftime("%A, %B %d" , local_now))

print(f"The lucky numbers for {timevar} are ---> {randomvar1} {randomvar2} {randomvar3} {randomvar4} {randomvar5} {randomvar6} ")
