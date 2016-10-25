# licensed under the Apache License 2.0
# github.com/masoncodes
# v 1.0.3

import core
import apps

version = "1.0.3"

print("masonCLI v " + version + ". Type 'help' for a list of commands.")

running = True  # wanna hear my longest yeah boi ever?

# !! anti-crash feature
lastCommand = ''

# get it boiz
while running:
    command = input("> ")
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
        core.help()

    if command == 'math':
        lastCommand = 'math'
        core.math()

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

    #show apphelp
    if command == 'apphelp':
        lastCommand = 'apphelp'
        apps.apphelp()

    if command == 'trifind':
        lastcommand = 'trifind'
        core.trifind()
