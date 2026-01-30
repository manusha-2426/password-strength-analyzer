import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    return score, feedback


def strength_level(score):
    if score == 5:
        return "Very Strong 💪"
    elif score == 4:
        return "Strong 👍"
    elif score == 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"


# Main Program
password = input("Enter your password: ")

score, tips = check_password_strength(password)
level = strength_level(score)

print("\nPassword Strength:", level)

if tips:
    print("\nSuggestions to improve:")
    for tip in tips:
        print("-", tip)
else:
    print("Your password is secure! ✅")
