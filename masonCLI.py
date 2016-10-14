#licensed under the GNU GPL v3
#github.com/masoncodes
#v 1.0 (First Release)

import os
import subprocess
import math
import cmath
import apps

version = "1.0"

print("masonCLI v "+version+". Type 'help' for a list of commands.")

running = True #yeah boiiii

#!! anti-crash feature
lastcommand = ''

while (running == True):
    command = input("> ")
    #run last command
    if (command == "!!"):
        command = lastcommand
        if (lastcommand == ''):
            print("No processes have been run yet.")

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
        print("masonCLI is a math-oriented command-line interface.")
        print("\n> is a command prompt.")
        print(">> is an input prompt.")
        print("'exit' exits masonCLI.")
        print("'help' shows this help.")
        print("'info' shows license info for masonCLI.")
        print("'echo' returns input.")
        print("'math' does simple math. (add, subtract, divide, multiply, modulus)")
        print("'rightcheck' checks for a right triangle.")
        print("'quadratic' will solve for the roots of three numbers.")
        print("'pythagorean' will find the length of the sides of a triangle.")
        print("'midpoint' will find the midpoint of two points.")
        print("'distance will ifind the distance between two points.")
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

    #quadratic formula
    if (command == 'quadratic'):
        lastcommand = 'quadratic'
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        root1 = complex(-b + cmath.sqrt(b**2 - (4 * a * c) / 2 * a))
        root2 = complex(-b + cmath.sqrt(b**2 - (4 * a * c) / 2 * a))
        print("Root 1 = ",root1)
        print("Root 2 = ",root2)

    #find parts of right triangle
    if (command == 'pythagorean'):
        lastcommand = 'pythagorean'
        part = input("Solve for a, b, or c? ")
        if (part == 'a'):
            b = float(input("B = "))
            c = float(input("C = "))
            bb = float(b**2)
            cc = float(c**2)
            pre = cc-bb
            ans = math.sqrt(pre)
            print(ans)
        if (part == 'b'):
            a = float(input("A = "))
            c = float(input("C = "))
            aa = float(a**2)
            cc = float(c**2)
            pre = cc-aa
            ans = math.sqrt(pre)
            print(ans)
        if (part == 'c'):
            a = float(input("A = "))
            b = float(input("B = "))
            aa = float(a**2)
            bb = float(b**2)
            pre = bb+aa
            ans = math.sqrt(pre)
            print(ans)

    #find midpoint
    if (command == 'midpoint'):
        lastcommand = 'midpoint'
        x1 = float(input("X1 = "))
        y1 = float(input("Y1 = "))
        x2 = float(input("X2 = "))
        y2 = float(input("Y2 = "))
        a = x1+x2
        b = float(a)/2
        c = y1+y2
        d = float(b)/2
        print(b, ", ", d,)

    #find distance
    if(command == 'distance'):
        lastcommand = 'distance'
        x1 = float(input("X1 = "))
        y1 = float(input("Y1 = "))
        x2 = float(input("Y2 = "))
        y2 = float(input("Y2 = "))
        a = (float(x2) - float(x1))
        b = a*a
        c = (float(y2) - float(y1))
        d = c*c
        e = float(b) + float(c)
        f = math.sqrt(float(e))
        print(f)
