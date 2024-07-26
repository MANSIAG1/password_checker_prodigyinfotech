import string
import secrets

def check_password_strength(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = ('That\'s a very bad password. Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password. You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess. But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one hell of a strong password!!! Hackers don\'t have a chance guessing that password!')

    return f'Your password has:\n{lower_count} lowercase letters\n{upper_count} uppercase letters\n{num_count} digits\n{wspace_count} whitespaces\n{special_count} special characters\nPassword Score: {strength}/5\nRemarks: {remarks}', strength

def generate_password():
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
    return password

if __name__ == "__main__":
    user_choice = input("Do you want to generate a new password? (yes/no): ").strip().lower()
    if user_choice == 'yes':
        new_password = generate_password()
        print(f"Generated Password: {new_password}")
        print("Strength of generated password:")
        result, strength = check_password_strength(new_password)
        print(result)
    else:
        password = input("Enter the password to check: ")
        result, strength = check_password_strength(password)
        print(result)
