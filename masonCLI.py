# licensed under the Apache License 2.0
# github.com/masoncodes
# masoncodes.me
# v 2.1
# for core code, see core.py
# to add custom code in a safe way, see apps.py


import core
import apps

# version CHANGE THIS
version = "2.1"

print("masonCLI v " + version + ". Type 'help' for a list of commands.")

running = True  # wanna hear my longest yeah boi ever?

# !! anti-crash feature
lastCommand = ''

# prompt loop
while running:
    command = input("> ")
    # convert to lowercase
    command = command.lower()
    # run last command
    if command == "!!":
        command = lastCommand
        if lastCommand == '':
            print("No processes have been run yet.")

    # equal to bash echo
    elif command == 'echo':
        lastCommand = 'echo'
        core.echo()

    # exits masonCLI
    elif command == 'exit':
        # DO NOT ADD LASTCOMMAND HERE. there's no reason to, and it would take up space
        running = False
        exit()

    # help
    elif command == 'help':
        lastCommand = 'help'
        core.assist()

    # math
    elif command == 'math':
        lastCommand = 'math'
        core.climath()

    # apache
    elif command == 'info':
        lastCommand = 'info'
        core.info()

    # right triangle checker
    elif command == 'rightcheck':
        lastCommand = 'rightcheck'
        core.rightcheck()

    # quadratic formula
    elif command == 'quadratic':
        lastCommand = 'quadratic'
        core.quadratic()

    # find parts of right triangle
    elif command == 'pythagorean':
        lastCommand = 'pythagorean'
        core.pythagorean()

    # find midpoint
    elif command == 'midpoint':
        lastCommand = 'midpoint'
        core.midpoint()

    # find distance
    elif command == 'distance':
        lastCommand = 'distance'
        core.distance()

    # show apphelp
    elif command == 'apphelp':
        lastCommand = 'apphelp'
        apps.apphelp()

    # triangle angle finder
    elif command == 'trifind':
        lastCommand = 'trifind'
        core.trifind()

    # roots
    elif command == 'root':
        lastCommand = 'root'
        core.root()

    # factorial
    elif command == 'factorial':
        lastCommand = 'factorial'
        core.factorial()
    else:
        print(command, "is not a valid command.")