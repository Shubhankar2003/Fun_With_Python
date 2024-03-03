import re

def is_strong_password(password):
    if len(password) < 8:
        print('''Invalid (must be 8 digits or more)''')
        return False
    
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        print('''WEAK (must contain uppercase and lowercase letters)''')
        return False
    
    if not re.search(r'\d', password):
        print('''WEAK (must contain a number)''')
        return False

    if not re.search(r'[!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]', password):
        print('''WEAK (must contain a special character)''')
        return False
    
    else:
        print("Its a STRONG password")
        return True


#Test cases
is_strong_password('abCd@123')
is_strong_password('jnd')
is_strong_password('Shubhankae201')