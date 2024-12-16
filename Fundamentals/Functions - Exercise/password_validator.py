def password_validator(password):
  password_valid = True
  
  if not (6 <= len(password) <= 10):
    print("Password must be between 6 and 10 characters")
    password_valid = False
  
  if not password.isalnum():
    print("Password must consist only of letters and digits")
    password_valid = False
    
  digits = [char for char in password if char.isnumeric()]
  
  if not len(digits) >= 2:
    print("Password must have at least 2 digits")
    password_valid = False
    
  if password_valid:
    print("Password is valid")

user_password = input()

password_validator(user_password)
