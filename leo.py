#!/usr/bin/env python3 -[v]S

expert = "informatique"

import openai
from colorama import Fore
import os
import time
import socket

print(Fore.MAGENTA + "test de connexion...")
time.sleep(0.5)
try:
    socket.create_connection(("www.google.com", 80))
    print(Fore.GREEN + "connexion reussite")
except OSError:
    print(Fore.RED + "[error] Vous n'êtes pas connecté à Internet")
    quit()
time.sleep(1.5)
os.system('cls' if os.name=='nt' else 'clear')

def logo():
    print(Fore.BLUE + ".__                 .___   _____   ")
    print("|  |   ____  ____   |   | /  _  \  ")
    print("|  | _/ __ \/  _ \  |   |/  /_\  \ ")
    print("|  |_\  ___(  <_> ) |   /    |    \ ")
    print("|____/\___  >____/  |___\____|__  / ")
    print("          \/                    \/ ")
    print("Intelligence artificielle basée sur \"text-davinci-003\"")
    print()
logo()
openai.api_key = "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"

def chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "tu est une intelligence artificiel qui s'appelle leo et qui est en expert en " + expert + " et ma question est :" + prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:
    prompt = input(Fore.CYAN + "Vous: ")
    if(prompt == 'exit'):
        quit()
    elif(prompt == 'set-expert'):
        expert = input(Fore.LIGHTMAGENTA_EX + "[set-expert] leo vas devenir un expert en ")
    elif(prompt == 'clear'):
        os.system('cls' if os.name=='nt' else 'clear')
        logo()
    elif(prompt == 'help'):
        print(Fore.MAGENTA + "[exit] pour fermer le programme")
        print("[clear] pour effacer la console")
        print("[help] pour obtenir de l'aide")
        print()
    else:
        response = chat(prompt)
        print(Fore.GREEN + f"leo: {response}")
        print()
