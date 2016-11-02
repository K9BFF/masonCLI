# licensed under the Apache License 2.0
# github.com/masoncodes
# masoncodes.me

import os
import shutil

print("This installer is PROOF OF CONCEPT AND IS NOT REQUIRED TO BE RUN.")
print("Before you begin, please ensure you have downloaded the latest version of masonCLI.")
print("Where should masonCLI be installed? (please specify a folder for masonCLI as well.)")
direc = input(">> ")
if not os.path.exists(direc):
    os.makedirs(direc)
    shutil.move("masonCLI.py", direc)
    shutil.move("apps.py", direc)
    shutil.move("core.py", direc)
    print("masonCLI has been successfully installed to:", direc+"!")
else:
    print("You already installed masonCLI!")
    exit(0)
