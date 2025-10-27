# generator.py

from os import read
import string
import secrets
from pyperclip import copy
from pywebio.output import put_file, toast


# generator.py

import string
import secrets
from pyperclip import copy
from pywebio.output import put_file, toast


class Generator: # README: generator 👈
    def __init__(self):
        self.password = None

    def generate(
        self,
        length: int = 0,
        use_uppercase: bool = False,
        use_lowercase: bool = False,
        use_numbers: bool = False,
        use_symbols: bool = False,
    ):
        """
        Generate a password using selected character sets.
        """

        char_pool = ''

        if use_uppercase:
            char_pool += string.ascii_uppercase

        if use_lowercase:
            char_pool += string.ascii_lowercase

        if use_numbers:
            char_pool += string.digits

        if use_symbols:
            char_pool += string.punctuation

        # Fallback if nothing selected
        if not char_pool:
            char_pool = (
                string.ascii_letters
                + string.digits
                + string.punctuation
            )

        self.password = ''.join(
            secrets.choice(char_pool)
            for _ in range(length)
        )

        return self.password

    def get_password(self):
        return self.password

    def copy_password(self):
        if self.password:
            copy(self.password)
            toast("Copied to clipboard")
        else:
            toast("No password generated")

    def download_password(self):
        if self.password:
            pwd = self.password.encode("utf-8")
            filename = "your_password.txt"
            put_file(filename, pwd)
            toast("Download started")
        else:
            toast("No password generated")