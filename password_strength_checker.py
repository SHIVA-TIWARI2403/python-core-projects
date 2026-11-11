def check_password(password):
    if len(password) < 6:
        return "❌ Password must be at least 8 characters long."

    if not any(char.isupper() for char in password):
        return "❌ Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "❌ Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return "❌ Password must contain at least one digit."

    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

    if not any(char in special_characters for char in password):
        return "❌ Password must contain at least one special character."

    return "✅ Password is strong."


password = input("Enter your password: ")
print(check_password(password))