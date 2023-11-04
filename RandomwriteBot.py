import random 
import pyautogui as pg 
import time

animal = ('Vowki','Cukrzyk','Qwerciak')

time.sleep(8)

for i in range(500):
  a = random.choice(animal)
  pg.write("E cwele  " + a)
  pg.press('enter')