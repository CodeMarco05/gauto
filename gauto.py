import click
import datetime
import os
import sys

import utils


class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'


@click.group()
def gauto():
    'gauto is an automated git upload assistend.'
    pass


# for generating a exe with pyinstaller
# pyinstaller gauto.py --onefile

# Upload command for git
@gauto.command()
@click.option('-m', '--message', default=utils.get_default_push_message(), show_default=True)
@click.option('-b', '--branch', default=utils.get_default_push_branch(), show_default=True)
def upload(message, branch):
    os.system('git add .')
    os.system(f'git commit -m "{str(message)}"')
    os.system(f'git push -u origin {str(branch)}')
    print(style.GREEN + 'Upload command finished. Please look for errors during the Process!' + style.RESET)


# Download command for git
@gauto.command()
@click.option('-b', '--branch', default=utils.get_default_pull_branch(), show_default=True)
def pull():
    print()


if __name__ == '__main__':
    gauto()
