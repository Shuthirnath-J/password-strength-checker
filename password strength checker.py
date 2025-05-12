import re

def check_strength(password):
    length_error = len(password)<8
    lower_error = re.search(r"[a-z]", password) is None
    upper_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[ !\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", password) is None
    
    errors = {
        'Too short' : length_error,
        'No lower case' : lower_error,
        'No upper case' : upper_error,
        'No numbers' : digit_error,
        'No special characters' : special_error
    }
    
    issues = [msg for msg, error in errors.items() if error]
    total_errors = sum(errors.values())
    
    if total_errors == 0:
        strength = "Strong"
    elif total_errors <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"
            
    return strength, issues
def loop():
    password = input("Please create a new password:  ")

    strength, issues = check_strength(password)

    print("password strength", strength)
    if issues:
        print("Issues:",issues)
    return strength
        
strength = "Weak"
while(strength == "Weak" or strength == "Moderate"):
    strength = loop()