import os

import pywebio
from pywebio import start_server
from pywebio.output import (
    clear,
    put_image
)

from next import Next


class Interface: # README: Interface 👈
    def __init__(self):
        # README:  here we setup  window with title and theme properties 
        pywebio.config(title='Generator Password', theme='dark')

    def run(self):
        clear()
        logo_path = os.path.join('./assets/image', 'logo.png')
        put_image(open(file=logo_path, mode='rb').read())
        Next()


if __name__ == '__main__':
    interface = Interface()
    start_server(interface.run, port=8000, debug=True)
