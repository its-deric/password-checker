password = input("Enter your password: ")


# Step 2: Define the password criteria
def check_password():
    # Criteria flags
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=" for char in password)

    # Overall result
    if length and has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False
 # step 3: Provide feedback to the user
if check_password():
    print("Your password is strong!")
else:
    print("Your password is weak. Please ensure it meets the following criteria:")
    if len(password) < 8:
        print("- At least 8 characters long")
    if not any(char.isupper() for char in password):
        print("- Contains at least one uppercase letter")
    if not any(char.islower() for char in password):
        print("- Contains at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        print("- Includes at least one digit")
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        print("- Has at least one special character")





