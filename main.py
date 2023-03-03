import os
import sys
import platform

def help():
    cmds = ["help", "exit", "os", "neofetch", "weather"]
    print("Commands: \n")

    for command in cmds:
        print(command)


if __name__ == "__main__":
    print("Welcome to LightSH!")

    while 1 == 1:
        temp = input("$ ")
        cmd = temp.lower()

        if cmd in ["help", "?"]:
            help()

        if cmd == "exit":
            print("Exiting..")
            sys.exit(0)

        if cmd == "os":
            print(platform.version())

        if cmd == "neofetch":
            os.system("neofetch")

        if cmd == "weather":
            city = input("Enter a city: ")

            os.system(f"curl wttr.in/{city}")

