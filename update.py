# licensed under the Apache License 2.0
# github.com/masoncodes
# masoncodes.me
# I cannot guarantee that this program will work properly if this is file is edited.

import os

print("This file updates masonCLI to its current form in github.")
print("For stable releases, install the releases from github.\n")

print("Unless you have Git installed on your computer,\n"
      "you will have to go to:\n"
      "https://github.com/masoncodes/masonCLI\n"
      "to download the newest version.")
print("Is git installed on this computer? (y/n)")
ask = input(">> ")
if ask == "y":
    print("Is masonCLI already installed on this computer (from github?) (y/n)")
    ask2 = input(">> ")
    if ask2 == "y":
        print("Where is the installation located?")
        path2 = input(">> ")
        os.chdir(path2)
        os.system("git pull")
        print("Pull complete.")
        input("Press [Enter] to finish. ")
    if ask2 == "n":
        print("Please specify a path for future versions of masonCLI.")
        path = input(">> ")
        if os.path.exists(path):
            os.chdir(path)
            os.chdir("masonCLI")
            os.system("git pull")
            print("Pull complete.")
            input("Press [Enter] to finish.")
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)
            os.system("git clone https://github.com/masoncodes/masonCLI")
            print("masonCLI has been updated.")
            input("Press [Enter] to finish. ")
elif ask == "n":
    print("Please use github to download the latest version of\n"
          "masonCLI.")
    input("Press [Enter] to exit the updater. ")
else:
    print("Invalid input.")
