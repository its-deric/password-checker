# password-checker

Project Description
The Password Strength Checker is a Python script designed to evaluate the strength of a user's password based on several criteria. It ensures that the password meets essential security standards, such as length and character diversity, helping users create strong, secure passwords.

The script checks if the password:

Is at least 8 characters long
Contains both uppercase and lowercase letters
Includes at least one digit
Contains at least one special character (e.g., !@#$%^&*()-_+=)
This project is ideal for learning basic Python programming, and user input validation.

Features
Length Validation: Password must be at least 8 characters long.
Uppercase/Lowercase Check: Ensures the password contains both uppercase and lowercase letters.
Digit Check: Validates the inclusion of at least one number.
Special Character Validation: Confirms that at least one special character is included.

Installation

To run this script on your local machine, follow these steps:

1. Clone the Repository
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/its-deric/password-checker.git

2.  Navigate to the project directory:
cd password-checker

3. Run the script:
python password_checker.py

Usage
After running the script, you'll be prompted to enter a password. The script will then analyze your password based on the criteria listed above and provide feedback on its strength.

For Example:
Enter your password: Password123!
Your password is strong!

If your password does not meet the criteria, you'll receive feedback on what is missing:
Enter your password: pass123
Your password is weak. Please ensure it meets the following criteria:
- At least 8 characters long
- Contains at least one uppercase letter
- Has at least one special character

Technologies Used
Python: The project is built using Python 3, which provides simple and clean handling of string manipulations and user input.

