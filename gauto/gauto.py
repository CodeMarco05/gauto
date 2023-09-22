import click
import datetime
import os


class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'


@click.group()
def gauto():
    'gauto is a automated git upload assistend.'
    pass


# Upload command for git
@gauto.command()
@click.option('-m', '--message', default=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), show_default=True)
@click.option('-b', '--branch', default='master', show_default=True)
def upload(message, branch):
    if message is None:
        message = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    os.system('git add .')
    os.system(f'git commit -m "{str(message)}"')
    os.system(f'git push -u origin {str(branch)}')
    print()
    print(style.GREEN + 'Upload command finished. Please look for errors during the Process!' + style.RESET)

# Download command for git
@gauto.command()
def pull():
    print()

if __name__ == '__main__':
    gauto()
