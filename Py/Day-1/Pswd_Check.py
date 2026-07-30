# PASSWORD CHECKER

password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short")
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter")
    if not any(char == "!" or char == "@" or char == "#" or char == "$" for char in password):
        print("Password must contain at least one special character (!, @, #, $)")
else:
    print("Password is valid")