# Password Maker Tools

Password Maker Tools is a Python-based web application designed to generate secure and customizable passwords. With an interactive interface powered by PyWebIO, the tool provides users with options to create passwords tailored to their needs, including character types and lengths.

## Features

### 1. Password Generator
- **Customizable Character Types:** Choose from upper case, lower case, numbers, and special characters.
- **Adjustable Length:** Specify the desired length of your password (up to a maximum of 2048 characters).
- **Validation:** Ensures that the user selects at least one character type and provides a positive number for the password length.

### 2. Interactive Interface
- **Dynamic Table Display:** View your generated password with interactive options:
  - Copy the password to your clipboard.
  - Download the password as a text file (`your_password.txt`).
  - Refresh to generate a new password.
- **User-Friendly Widgets:** Includes input groups, checkboxes, and buttons for seamless interaction.

### 3. Secure and Efficient
- **Random Password Generation:** Utilizes a list of predefined symbols and character filters to create strong passwords.
- **Clipboard Support:** Easily copy generated passwords to your clipboard.
- **File Download:** Save passwords securely on your device.

## Project Structure

- **`main.py`:** Entry point of the application. Sets up the PyWebIO server and initializes the interface.
- **`next/`:** Contains the core modules for password generation and UI components.
  - `next.py`: Implements the `Next` class, extends the `Generator` class, and manages the UI widgets.
  - `generator.py`: Defines the `Generator` class and the logic for generating passwords.
  - `symbols.py`: Provides a list of symbols and characters used in password generation.
  - `char_filter.py`: (Imported but not included in the current codebase) Likely filters characters based on the selected modes.

## How to Run

### 1. Clone the repository:
   ```bash
   git clone https://github.com/mihaiapostol14/Password_Maker_Tools.git
   cd Password_Maker_Tools
   ```

### 2. Create and Activate a Virtual Environment

**Install Python**

If you don't have Python installed, follow [this link](https://www.python.org/downloads/) and download the latest version of Python. Then you can check your version of Python using the command lines below:

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Open your browser and navigate to from down below
`http://localhost:8000`

## Technology Stack

- **Python:** Backend logic and password generation.
- **PyWebIO:** Frontend rendering and interactive components.
- **Random & os Modules:** Randomized password generation and file handling.

## Future Enhancements

- **Advanced Filters:** Add more options for customizing password patterns.
- **Themes:** Provide multiple themes for the interface.
- **Integration:** Extend the tool for use with browser extensions or mobile apps.

## License

MIT License. See [LICENSE](LICENSE) for details.

---
**Author:** [Mihai Apostol](https://github.com/mihaiapostol14)