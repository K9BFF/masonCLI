# licensed under the Apache License 2.0
# github.com/masoncodes
# masoncodes.me
# I cannot guarantee that this program will work properly if this is file is edited.


import math
import cmath


def echo():
    echocom = input(">> ")
    print(echocom)


def assist():
    print("\nmasonCLI is a math-oriented command-line interface.")
    print("> is a command prompt.")
    print(">> is an input prompt.\n")
    print("'exit' exits masonCLI.")
    print("'help' shows this help.")
    print("'info' shows license info for masonCLI.")
    print("'echo' returns input.")
    print("'prompt' will change the prompt for the current session.")
    print("'math' does simple math. (Add, Subtract, Divide, Multiply, Modulus, Exponents.)")
    print("'rightcheck' checks for a right triangle.")
    print("'quadratic' will solve for the roots of three numbers.")
    print("'pythagorean' will find the length of a side on a triangle.")
    print("'tritheorem' will use the Triangle Inequality Theorem.")
    print("'midpoint' will find the midpoint of two points.")
    print("'distance will find the distance between two points.")
    print("'trifind' will find the missing angle of a triangle.")
    print("'root' will find the x root of a number.")
    print("'factorial' will find the factorial of a number.")
    print("'splitwork' will solve a split-work problem.")
    print("'missingangle' will solve for a missing angle.\n")


def climath():
    print("Choose an operation (+, -, *, /, %, ^), and input two numbers. (ex. 1 + 1)")
    n1, operator, n2 = input(">> ").split()
    if n1.isalpha():
        print("n1 is not a numerical value.")
    elif n2.isalpha():
        print("n2 is not a numerical value.")
    else:
        n1 = float(n1)
        n2 = float(n2)
        if operator == '+':
            print(n1 + n2)
        elif operator == '-':
            print(n1 - n2)
        elif operator == '*':
            print(n1 * n2)
        elif operator == '/':
            if n1 == 0:
                print("Divide by Zero Error.")
            elif n2 == 0:
                print("Divide by Zero Error.")
            else:
                print(n1 / n2)
        elif operator == '%':
            if n1 == 0:
                print("Divide by Zero Error.")
            elif n2 == 0:
                print("Divide by Zero Error.")
            else:
                print(n1 % n2)
        elif operator == '^':
            print(n1 ** n2)
        else:
            print("'" + operator + "' isn't an operation.")
# welp that's enough math. maybe it can solve linear equations too someday


def info():
    print("A Python CLI.")
    print("Copyright 2016 masoncodes")
    print("""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
        """)

    print("masoncodes.me")
    print("See the LICENSE file for more information.")


def rightcheck():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if (a ** 2) + (b ** 2) == (c ** 2):
        print("Its a right triangle.")
    else:
        print("It isn't a right triangle.")


def quadratic():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    root1 = complex(-b + cmath.sqrt(b ** 2 - (4 * a * c) / 2 * a))
    root2 = complex(-b - cmath.sqrt(b ** 2 - (4 * a * c) / 2 * a))
    print("Root 1 = ", root1)
    print("Root 2 = ", root2)


def pythagorean():
    print("Solve for (a), (b), or (c)?")
    part = input(">> ").lower()
    if part == 'a':
        b = float(input("b = "))
        c = float(input("c = "))
        bb = float(b ** 2)
        cc = float(c ** 2)
        pre = cc - bb
        ans = math.sqrt(pre)
        print(ans)
    elif part == 'b':
        a = float(input("a = "))
        c = float(input("c = "))
        aa = float(a ** 2)
        cc = float(c ** 2)
        pre = cc - aa
        ans = math.sqrt(pre)
        print(ans)
    elif part == 'c':
        a = float(input("a = "))
        b = float(input("b = "))
        aa = float(a ** 2)
        bb = float(b ** 2)
        pre = bb + aa
        ans = math.sqrt(pre)
        print(ans)
    else:
        print("Invalid input.")


def midpoint():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    a = x1 + x2
    b = float(a) / 2
    c = y1 + y2
    d = float(c) / 2
    print(b, ", ", d, )


def distance():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    a = (float(x2) - float(x1))
    b = a * a
    c = (float(y2) - float(y1))
    d = c * c
    e = float(b) + float(d)
    f = math.sqrt(float(e))
    print(f)


def trifind():
    angle1 = float(input("n1 = "))
    angle2 = float(input("n2 = "))
    not_total = (angle1 + angle2)
    total = (180 - not_total)
    print(total, "Degrees")


def root():
    index = float(input("Index = "))
    n1 = float(input("n1 = "))
    rooter = (1 / index)
    n2 = (n1 ** rooter)
    print(n2)


def factorial():
    n1 = float(input("n1 = "))
    n2 = math.factorial(n1)
    print(n2)


def splitwork():
    print("Solve for time, or n1?")
    solve = input(">> ")
    if solve == 'time':
        n1 = float(input("n1 = "))
        n2 = float(input("n2 = "))
        n1 = (n1 ** -1)
        n2 = (n2 ** -1)
        n3 = n1 + n2
        print(n3)
    elif solve == 'n1':
        time = float(input("time = "))
        n2 = float(input("n2 = "))
        time = (time ** -1)
        n2 = (n2 ** -1)
        n3 = (time + n2)
        print(n3)
    else:
        print("Input invalid.")


def missingangle():
    n1 = float(input("n1 = "))
    n2 = float(input("n2 = "))
    if n1 > 180:
        print("Not possible.")
    elif n2 > 180:
        print("Not possible.")
    else:
        n3 = n1 + n2
        n4 = 180 - n3
        print(n4, "Degrees")


def triangle_ineq_theorem():
    print("Find (triangle) or (range)?")
    kind = input(">> ").lower()
    if kind == 'triangle':
        n1 = float(input("side1 = "))
        n2 = float(input("side2 = "))
        n3 = float(input("side3 = "))
        n4 = (n1 + n2)
        if n4 > n3:
            print("It is a triangle.")
        else:
            print("Not a triangle.")
    elif kind == 'range':
        n1 = float(input("n1 = "))
        n2 = float(input("n2 = "))
        p1 = (n2 - n1)
        p2 = (n2 + n1)
        print(p1, '< x <', p2)
    else:
        print("Invalid input.")
