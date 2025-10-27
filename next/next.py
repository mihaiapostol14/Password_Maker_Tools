# next.py

from pywebio.input import (
    input,
    NUMBER,
    input_group,
    checkbox
)
from pywebio.output import (
    put_html,
    put_table,
    span,
    put_button
)
from pywebio.session import run_js

from .generator import Generator


class Next(Generator): # README: Next 👈
    def __init__(self):
        super().__init__()
        self.add_widgets()

    def add_widgets(self):
        self.make_html('<h1>Generator Password</h1>')
        self.make_input()
        self.make_table()

    def make_html(self, text: str = ''):
        return put_html(text)

    def make_input(self):
        def validate(data):
            if not data["modes"]:
                return (
                    "modes",
                    "Select at least one character type"
                )

            if not data["length"]:
                return (
                    "length",
                    "Password length is required"
                )

            if data["length"] <= 0:
                return (
                    "length",
                    "Length must be greater than 0"
                )

            if data["length"] > 2048:
                return (
                    "length",
                    "Maximum password length is 2048"
                )

        data = input_group(
            "Password Options",
            [
                checkbox(
                    "Character types",
                    name="modes",
                    options=[
                        "upper",
                        "lower",
                        "number",
                        "special"
                    ]
                ),

                input(
                    "Password Length",
                    type=NUMBER,
                    name="length",
                    help_text="Maximum password length: 2048",
                    required=True
                )
            ],
            validate=validate
        )

        # Generate password
        self.password = self.generate(
            length=data["length"],
            use_uppercase="upper" in data["modes"],
            use_lowercase="lower" in data["modes"],
            use_numbers="number" in data["modes"],
            use_symbols="special" in data["modes"]
        )

    def make_table(self):
        return put_table([
            [
                span(
                    f'Your Password: {self.get_password()}',
                    col=3
                )
            ],
            [
                put_button(
                    'Copy Password',
                    onclick=self.copy_password
                ),

                put_button(
                    'Export File',
                    onclick=self.download_password
                ),

                put_button(
                    'Refresh',
                    onclick=lambda: run_js(
                        'window.location.reload()'
                    )
                )
            ],
        ])