from random import randint as r
from time import sleep
from Madonna_3_0 import engine

for _ in range(r(1, 100)):
    print(engine() + '\n')
    sleep(0.8)
