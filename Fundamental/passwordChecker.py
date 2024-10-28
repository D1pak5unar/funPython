# Objective: Write a script that evaluates a password based on criteria like length, 
# use of uppercase/lowercase letters, numbers, and special characters.
# Details: Include checks for weak passwords like 'password123'. 
# Output the password strength as 'Weak', 'Moderate', or 'Strong'.

# re = regular expression
import re # allows for pattern matching in strings 

def check_password_strength(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"[0-9]", password) is not None
    special_criteria = re.search(r"[@#$%^&+=]", password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine the strength based on the number of criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Print the result
    print(f"Password: {password}")
    print(f"Strength: {strength}")
    print("Criteria Met:")
    print(f"- Length (8+ chars): {'Yes' if length_criteria else 'No'}")
    print(f"- Uppercase Letter: {'Yes' if upper_criteria else 'No'}")
    print(f"- Lowercase Letter: {'Yes' if lower_criteria else 'No'}")
    print(f"- Number: {'Yes' if digit_criteria else 'No'}")
    print(f"- Special Character: {'Yes' if special_criteria else 'No'}")

# Test the function
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    check_password_strength(password)
