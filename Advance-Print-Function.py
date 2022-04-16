""" ALL COPYRIGHT CLAIMS BELONG TO NORMAL1234 , RESPECTIVELY USING THIS CODE WITHOUT MY PERMISSION WILL RESULT IN STRICT ACTIONS


~~ thanks :D 
"""


#pylint:disable=W0613
#pylint:disable=E0213


# Given Value in For Loop is 1000 by default
# USAGE >>>


#Advance.print("idk")

# Or This Class can be imported into other file by using

#from current_file_name import Advance
# Advance.print()

version = 1.0
from colorama import Fore, Back, init, Style
 
init(autoreset=True)

class Advance():
        def print(data = "", loop = ""):
        	print(Fore.CYAN + Back.LIGHTYELLOW_EX + "THIS PROGRAM HAS BEEN PROGRAMMED BY NORMAL:\nKindly Please Give Me Credits if You share it anywhere.   ", sep= "\n")
        	print(Fore.GREEN + f"\nVerison: {version}\n")
        	if loop == "while":
        		while True:
        			print(data)
        	elif loop == "for":
        		for i in range(True):
        			i += True
        			print(data)
        	else:
        		print(Fore.BLUE + Back.LIGHTWHITE_EX +"\nNo Value is Entered for loop Type\n")
        		print(Fore.MAGENTA + Back.LIGHTGREEN_EX + "\nEnter Loop VALUE or program will be exited\n")
        		 
        		type1 = input(Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + "i.e = while,for\nentering no value will result in failure of program\nType LOOP : ")
        		if type1 == "while":
        			while True:
        				print(Fore.RED + data)
        		elif type1 == "for":
        			i = True
        			for i in range(1000):
        				print(Fore.LIGHTMAGENTA_EX + data)
        		elif loop == "" or None:
        			print(Style.RESET_ALL)
        			print(Fore.RED + "No Value is given either given value is invalid enter correct")
        		elif data == "" or None:
        			print(Fore.LIGHTCYAN_EX + "No Value is given or given value is invalid")
        			

Advance.print()



								
							
						
					