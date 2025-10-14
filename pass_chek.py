def pass_chak(password):
    if len(password)<8:
        return "password must be 8 characters"
    if not any(char.isdigit() for char in password):
        return "Digit missing from the password"
    if not any(char.islower() for char in password):
        return "use atlist one lowercase character"
    if not any(char.isupper() for char in password):
        return "atlist one uppercase characater"
    if not any(char in '!@#$%^&+*' for char in password):
        return "special character missing"       
    else:
        return "password is perfect"

print(pass_chak('weakPass'))
print(pass_chak('!paSS0Str'))