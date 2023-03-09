import os
import sys
import platform
import time


def cmds_help():
    cmds = ["help", "exit", "os", "neofetch", "weather", "search"]
    print("Commands: \n")

    for command in cmds:
        print(command)


if __name__ == "__main__":
    print("Welcome to LightSH!")

    try:
        while 1 == 1:
            temp = input("LightSH $ ")
            cmd = temp.lower()

            if cmd in ["help", "?"]:
                cmds_help()

            if cmd in ["exit", "kick me out"]:
                print("Exiting..")
                sys.exit(0)

            if cmd == "os":
                print(platform.version())

            if cmd == "neofetch":
                os.system("neofetch")

            if cmd == "weather":
                city = input("Enter a city: ")

                os.system(f"curl wttr.in/{city}")

    except KeyboardInterrupt:
        print("Exiting..")
        sys.exit(0)
