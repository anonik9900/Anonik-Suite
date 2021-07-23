#!/usr/bin/env python3
import random
import string
import subprocess #Process commands
import socket #Process socket data
import pyfiglet
import sys
import os
from subprocess import call


def MenuShell():
	ascii_banner = pyfiglet.figlet_format("Anonik Suite")
	print(ascii_banner)
	print ("{< Devolved By Anonik V 0.1>}")
	print("")


def SplashScreen():
	print ("         .            )        )")
	print ("                  (  (|              .")
	print ("              )   )\/ ( ( (")
	print ("      *  (   ((  /     ))\))  (  )    )")
	print ("    (     \   )\(          |  ))( )  (|")
	print ("    >)     ))/   |          )/  \((  ) \ ")
	print ("    (     (      .        -.     V )/   )(    ( ")
	print ("    \   /     .   \            .       \))   ))")
	print ("       )(      (  | |   )            .    (  /")
	print ("      )(    ,'))     \ /          \( `.    )")
	print ("      (\>  ,'/__      ))            __`.  /")
	print ("     ( \   | /  ___   ( \/     ___   \ | ( (")
	print ("      \.)  |/  /   \__      __/   \   \|  ))")
	print ("     .  \. |>  \      | __ |      /   <|  /")
	print ("          )/    \____/ :..: \____/     \ <")
	print ("   )   \ (|__  .      / ;: \          __| )  (")
	print ("  ((    )\)  ~--_     --  --      _--~    /  ))")
	print ("   \    (    |  ||               ||  |   (  /")
	print ("         \.  |  ||_             _||  |  /")
	print ("           > :  |  ~V+-I_I_I-+V~  |  : (.")
	print ("          (  \:  T\   _     _   /T  : ./")
	print ("           \  :    T^T T-+-T T^T    ;<")
	print ("            \..`_       -+-       _'  )")
	print ("  )            . `--=.._____..=--'. ./         (")




def listatool():
	
	
	print("YouTube Downloader | digita - ytdown \n")
	print("Backdoor Backfucker | digita - backfucker \n")
	print("Password Generator | digita - makepsw \n")
	
	
	return MenuPrincipale()
	

def Funzioni():
	print ("Ciao")
	




def MenuPrincipale():
	ascii_banner = pyfiglet.figlet_format("Anonik Suite")
	print(ascii_banner)
	print("")
	print ("============================================")
	print("               MENU PRINCIPALE               ")
	print ("")
	print ("Seleziona (1) per la lista dei tools")
	print("")
	print ("Altrimenti digita il comando da lanciare")
	print ("")
	print ("============================================")
	
	sceltaMenu = input("root@anoniksuite: ")
	

	
	if sceltaMenu == str("1"):
		return (listatool())
		
		
	if sceltaMenu == str("ytdown"):
		print("")
		call(["python3", "tools/ytd.py"])	
		#xec(open('test1.py').read())	
		#call(["python3", "test/test1.py"])
		
	if sceltaMenu == str("backfucker"):
		print("")
		call(["python3", "tools/backfucker.py"])
		
	if sceltaMenu == str("makepsw"):
		print("")
		call(["python3", "tools/pswf.py"])
		
	else:
		print("Errore: Invalid Input")
		os.system('clear')
		return MenuPrincipale()




print (MenuShell())
print (SplashScreen())
print (MenuPrincipale())
