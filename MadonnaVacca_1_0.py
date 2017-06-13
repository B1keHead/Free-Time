from random import randint as r
from os import system
from time import sleep
from Madonna_3_0 import engine

vbs_template = ("Set sapi=CreateObject(\"sapi.spvoice\")\n"
                "' Set sapi.voice = sapi.getvoices.item(2)\n"
                "sapi.Speak \"{}\"""")

final = ''
for _ in range(r(1, 100)):
    final += engine()

with open('vaccamadonna.vbs', 'w+') as file:
    file.write(vbs_template.format(final))

system('start vaccamadonna.vbs')
sleep(1)
system('del vaccamadonna.vbs')
