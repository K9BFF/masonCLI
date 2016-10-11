#licensed under the GNU GPL v3
#github.com/masoncodes
#v 0.0.2 (Alpha)

import os
import subprocess

version = "0.0.2 (Alpha)"

print("masonCLI v "+version+". Type 'help' for a list of commands.")

running = True #yeah boiiii

#!! anti-crash feature
lastcommand = ''

while (running == True):
    command = input("> ")

    #run last command
    if (command == "!!"):
        command =lastcommand
        if (lastcommand == ''):
            print("Nothing has been run yet.")

    #equal to bash echo
    if (command == 'echo'):
        lastcommand = 'echo'
        echocom = input(">> ")
        print(echocom)

    #exits masonCLI    
    if (command == 'exit'):
        #DO NOT ADD LASTCOMMAND HERE. there's no reason to, and it would take up space
        running = False
        os._exit(0)

    #help
    if (command == 'help'):
        lastcommand = 'help'
        print("\n> is a command prompt.")
        print(">> is an input prompt.")
        print("'exit' exits masonCLI.")
        print("'help' shows this help.")
        print("'info' shows license info for masonCLI.")
        print("'echo' returns input.")
        print("'math' does simple math. (add, subtract, divide, multiply, modulus)")
        print("'rightcheck' checks for a right triangle.")
        print("!! runs the previous command.")

    #math
    if (command == 'math'):
        lastcommand = 'math'
        print("Operation? (+, -, /, *, %)")
        operation = input(">> ")
        #add
        if (operation == '+'):
            n1 = float(input("n1 = "))
            n2 = float(input("n2 = "))
            add = (n1 + n2)
            print(add)
        #subtract      
        if (operation == '-'):
            n1 = float(input("n1 = "))
            n2 = float(input("n2 = "))
            diff = (n1 - n2)
            print(diff)
        #divide    
        if (operation == '/'):
            n1 = float(input("n1 = "))
            n2 = float(input("n2 = "))
            #no dividing by zero. its the rules
            if (n1 == 0):
                print("Divide by zero error.")
            if (n2 == 0):
                print("Divide by zero error.")
            else:
                quo = (n1 / n2)
                print(quo)
        #multiply    
        if (operation == '*'):
            n1 = float(input("n1 = "))
            n2 = float(input("n2 = "))
            pro = (n1 * n2)
            print(pro)
        #modulus
        if (operation == '%'):
            n1 = float(input("n1 = "))
            n2 = float(input("n2 = "))
            if (n1 == 0):
                print("Divide by zero error.")
            if (n2 == 0):
                print("Divide by zero error.")
            else:
                mod = (n1 % n2)
                print(mod)
        #welp thats enough math. maybe it can solve linear equations too someday

    #GNU GPL information
    if (command == 'info'):
        lastcommand = 'info'
        print("A Python CLI.")
        print("Copyright (C) 2016  masoncodes")
        print("""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
""")
        
        print("github.com/masoncodes")
        print("See the LICENSE file for more information.")

    #right triangle checker
    if (command == 'rightcheck'):
        lastcommand = 'rightcheck'
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        if ((a**2) + (b**2) == (c**2)):
            print("Its a right triangle.")
        else:
            print("It isn't a right triangle.")
