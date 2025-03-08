import os
import sys
import subprocess

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m]\x1b[0m \x1b[32m> \x1b[33mRunning: {command}\x1b[0m")
        subprocess.run(command, shell=True, check=True)
        print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m]\x1b[0m \x1b[32m> \x1b[33mCommand executed successfully\x1b[0m")
    except subprocess.CalledProcessError as e:
        print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m]\x1b[0m \x1b[31m> \x1b[33mError executing command: {e}\x1b[0m")
        sys.exit(1)

def main():
    commands = [
        'apt update',
        'apt install -y npm',
        'apt install -y curl',
        'curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash',
        'nvm install --lts'
    ]

    for command in commands:
        run_command(command)

    print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m]\x1b[0m \x1b[32m> \x1b[33mInstallation Successful\x1b[0m")

if __name__ == "__main__":
    main()