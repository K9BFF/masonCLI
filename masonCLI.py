# licensed under the Apache License 2.0
# github.com/masoncodes
# masoncodes.me
# v 2.5
# for core code, see core.py
# to add custom code in a safe way, see apps.py


import core
import apps

# version CHANGE THIS
version = "2.5"

print("masonCLI v" + version + ". Type 'help' for a list of commands.")

running = True  # wanna hear my longest yeah boi ever?

prompt = ">"

# prompt loop and commands
while running:
    # prompt
    command = input(prompt+" ").lower()

    if command == "prompt":
        prompt = input("Input the new prompt: ")

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

    # bad command
    else:
        if command == "":
            pass
        else:
            print("'"+command+"' is not a valid command.")
