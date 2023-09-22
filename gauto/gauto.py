import click
import datetime
import os

@click.group()
def gauto():
    'gauto is a automated git upload assistend.'
    pass


@gauto.command()
@click.option('-m', '--message', default=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), show_default=True)
@click.option('-b', '--branch', default='master', show_default=True)
def upload(message, branch):
    if message is None:
        message = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    click.echo(message)
    os.system('git add .')
    os.system(f'git commit -m {message}')
    os.system(f'git push -u origin {branch}')


if __name__ == '__main__':
    gauto()
