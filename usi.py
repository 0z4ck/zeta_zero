#!/usr/bin/env python3


import multiprocessing
from game import Game


while True:
    command = input()

    if command == "quit" or command == "exit":
        break

    elif command == "usi":
        print("id name zetazero 0.0")
        print("id author by 0z4ck")
        print("option name BookFile type string default public.bin")
        print("option name UseBook type check default true")
        print("usiok")

    elif command == "isready":
        print("readyok")

    elif command == "usinewgame":
        gm = Game()
        pass

    elif command == "stop":
        p.terminate()
   
    elif command == "gameover":
        pass

    elif command.split(" ")[0] == "position":
        usimoves = command.split(" ")[2:]
        gm.loadPosition(usimoves)
    
    elif command.split(" ")[0] == "go":
        p = multiprocessing.Process(target=gm.go)
        p.start()
    else:
       print("command not known: '{}'".format(command))
