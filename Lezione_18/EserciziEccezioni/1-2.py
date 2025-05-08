'''2- Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria (i.e., 
minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
'''

def validate_password(password:str = input("inserisci password: ")):
    
    uppercheck: int = 0
    specialcheck: int = 0
    
    for word in password:
        if word.isupper():
            uppercheck += 1
        if not word.isalnum():
            specialcheck += 1
    if uppercheck >= 3 and specialcheck >=4 and len(password) >= 20:
        print(password)
    
    else:
        raise ValueError("invalid password error")

validate_password()



