# licensed under the Apache License 2.0
# github.com/masoncodes
# masoncodes.me
# v 3.0
# for core code, see core.py
# to add custom code in a safe way, see apps.py


import core
import apps

# version CHANGE THIS
version = "3.0"

print("masonCLI v" + version + ". Type 'help' for a list of commands.")

running = True  # wanna hear my longest yeah boi ever?

prompt = ">"

# prompt loop and commands
while running:
    # prompt
    command = input(prompt+" ").lower()

    if command == "prompt":
        print("Input the new prompt.")
        prompt = input(">> ")

    # echo
    elif command == 'echo':
        core.echo()

    # exits masonCLI
    elif command == 'exit':
        running = False
        exit()

    # help
    elif command == 'help':
        core.assist()

    # syshelp
    elif command == 'help -sys':
        core.assist_sys()

    # geom help
    elif command == 'help -geom':
        core.assist_geom()

    # math
    elif command == 'math':
        core.climath()

    # apache
    elif command == 'info':
        core.info()

    # right triangle checker
    elif command == 'rightcheck':
        core.rightcheck()

    # quadratic formula
    elif command == 'quadratic':
        core.quadratic()

    # find parts of right triangle
    elif command == 'pythagorean':
        core.pythagorean()

    # find midpoint
    elif command == 'midpoint':
        core.midpoint()

    # find distance
    elif command == 'distance':
        core.distance()

    # show apphelp
    elif command == 'apphelp':
        apps.apphelp()

    # triangle angle finder
    elif command == 'trifind':
        core.trifind()

    # roots
    elif command == 'root':
        core.root()

    # factorial
    elif command == 'factorial':
        core.factorial()

    # split-work problems
    elif command == 'splitwork':
        core.splitwork()

    # find missing angle
    elif command == 'missingangle':
        core.missingangle()

    # triangle inequality theorem
    elif command == 'tritheorem':
        core.triangle_ineq_theorem()

    # print in order
    elif command == 'order':
        core.order()

    # bad command
    else:
        if command == "":
            pass
        else:
            print("'"+command+"' is not a valid command.")
