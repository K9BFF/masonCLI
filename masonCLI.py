# licensed under the Apache License 2.0
# github.com/masoncodes
# v 1.0.2

import math
import cmath
import apps

version = "1.0.2"

print("masonCLI v " + version + ". Type 'help' for a list of commands.")

running = True  # wanna hear my longest yeah boi ever?

# !! anti-crash feature
lastcommand = ''

# get it boiz
while running:
    command = input("> ")
    # run last command
    if command == "!!":
        valid = true
        command = lastcommand
        if lastcommand == '':
            print("No processes have been run yet.")

    # equal to bash echo
    if command == 'echo':
        lastcommand = 'echo'
        echocom = input(">> ")
        print(echocom)

    # exits masonCLI
    if command == 'exit':
        # DO NOT ADD LASTCOMMAND HERE. there's no reason to, and it would take up space
        running = False
        exit()

    # help
    if command == 'help':
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

    if command == 'math':
        lastcommand = 'math'
        n1 = float(input('n1 = '))
        print("Operation? (+, -, *, /, %)")
        op = input(">> ")
        if op == '+':
            n2 = float(input('n2 = '))
            n3 = float(n1 + n2)
            print(n3)
        if op == '-':
            n2 = float(input('n2 = '))
            n3 = float(n1 - n2)
            print(n3)
        if op == '*':
            n2 = float(input('n2 = '))
            n3 = float(n1 * n2)
            print(n3)
        if op == '/':
            n2 = float(input('n2 = '))
            if n1 == 0:
                print("Divide by Zero Error.")
            if n2 == 0:
                print("Divide by Zero Error.")
            n3 = float(n1 / n2)
            print(n3)
        if op == '%':
            n2 = float(input('n2 = '))
            if n1 == 0:
                print("Divide by Zero Error.")
            if n2 == 0:
                print("Divide by Zero Error.")
            n3 = float(n1 % n2)
            print(n3)

            # welp thats enough math. maybe it can solve linear equations too someday
            # YEEAH BOIII

    # apache
    if command == 'info':
        lastcommand = 'info'
        print("A Python CLI.")
        print("Copyright 2016 masoncodes")
        print("""
Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. See the License for the specific language governing permissions and limitations under
the License.
""")

        print("github.com/masoncodes")
        print("See the LICENSE file for more information.")

    # right triangle checker
    if command == 'rightcheck':
        lastcommand = 'rightcheck'
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        if (a ** 2) + (b ** 2) == (c ** 2):
            print("Its a right triangle.")
        else:
            print("It isn't a right triangle.")

    # quadratic formula
    if command == 'quadratic':
        lastcommand = 'quadratic'
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        root1 = complex(-b + cmath.sqrt(b ** 2 - (4 * a * c) / 2 * a))
        root2 = complex(-b + cmath.sqrt(b ** 2 - (4 * a * c) / 2 * a))
        print("Root 1 = ", root1)
        print("Root 2 = ", root2)

    # find parts of right triangle
    if command == 'pythagorean':
        lastcommand = 'pythagorean'
        part = input("Solve for a, b, or c? ")
        if part == 'a':
            b = float(input("B = "))
            c = float(input("C = "))
            bb = float(b ** 2)
            cc = float(c ** 2)
            pre = cc - bb
            ans = math.sqrt(pre)
            print(ans)
        if part == 'b':
            a = float(input("A = "))
            c = float(input("C = "))
            aa = float(a ** 2)
            cc = float(c ** 2)
            pre = cc - aa
            ans = math.sqrt(pre)
            print(ans)
        if part == 'c':
            a = float(input("A = "))
            b = float(input("B = "))
            aa = float(a ** 2)
            bb = float(b ** 2)
            pre = bb + aa
            ans = math.sqrt(pre)
            print(ans)

    # find midpoint
    if command == 'midpoint':
        lastcommand = 'midpoint'
        x1 = float(input("X1 = "))
        y1 = float(input("Y1 = "))
        x2 = float(input("X2 = "))
        y2 = float(input("Y2 = "))
        a = x1 + x2
        b = float(a) / 2
        c = y1 + y2
        d = float(b) / 2
        print(b, ", ", d, )

    # find distance
    if command == 'distance':
        lastcommand = 'distance'
        x1 = float(input("X1 = "))
        y1 = float(input("Y1 = "))
        x2 = float(input("Y2 = "))
        y2 = float(input("Y2 = "))
        a = (float(x2) - float(x1))
        b = a * a
        c = (float(y2) - float(y1))
        d = c * c
        e = float(b) + float(c)
        f = math.sqrt(float(e))
        print(f)
    if command == 'apphelp':
        lastcommand = apphelp
        print("See 'apps.py' for more information on apps."")
              
