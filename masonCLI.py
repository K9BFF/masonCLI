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
    if command == 'echo':
        lastCommand = 'echo'
        core.echo()

    # exits masonCLI
    if command == 'exit':
        # DO NOT ADD LASTCOMMAND HERE. there's no reason to, and it would take up space
        running = False
        exit()

    # help
    if command == 'help':
        lastCommand = 'help'
        core.assist()

    # math
    if command == 'math':
        lastCommand = 'math'
        core.climath()

    # apache
    if command == 'info':
        lastCommand = 'info'
        core.info()

    # right triangle checker
    if command == 'rightcheck':
        lastCommand = 'rightcheck'
        core.rightcheck()

    # quadratic formula
    if command == 'quadratic':
        lastCommand = 'quadratic'
        core.quadratic()

    # find parts of right triangle
    if command == 'pythagorean':
        lastCommand = 'pythagorean'
        core.pythagorean()

    # find midpoint
    if command == 'midpoint':
        lastCommand = 'midpoint'
        core.midpoint()

    # find distance
    if command == 'distance':
        lastCommand = 'distance'
        core.distance()

    # show apphelp
    if command == 'apphelp':
        lastCommand = 'apphelp'
        apps.apphelp()

    # triangle angle finder
    if command == 'trifind':
        lastCommand = 'trifind'
        core.trifind()

    # roots
    if command == 'root':
        lastCommand = 'root'
        core.root()

    # factorial
    if command == 'factorial':
        lastCommand = 'factorial'
        core.factorial()
