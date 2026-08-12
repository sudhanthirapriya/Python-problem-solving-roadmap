#!/usr/bin/env python3
"""
Real-world Project #3: Password Generator
-----------------------------------------
Interactive CLI tool that generates strong, customizable random passwords
with length control, character set selections, and password strength feedback.
"""

import random
import string

def check_strength(length, has_upper, has_lower, has_digits, has_special):
    score = 0
    if length >= 12: score += 2
    elif length >= 8: score += 1
    
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digits: score += 1
    if has_special: score += 1
    
    if score >= 5: return "Very Strong 💪"
    if score >= 4: return "Strong 👍"
    if score >= 3: return "Moderate 😐"
    return "Weak ⚠️"

def main():
    print("=" * 40)
    print("        SECURE PASSWORD GENERATOR        ")
    print("=" * 40)
    
    try:
        length = int(input("Enter password length (default 12): ") or "12")
    except ValueError:
        print("Invalid input, using default length of 12.")
        length = 12
        
    if length < 4:
        print("Length must be at least 4 characters for security. Resetting to 4.")
        length = 4
        
    use_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
    use_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
    use_digits = input("Include numbers? (y/n, default y): ").lower() != 'n'
    use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'
    
    # Building character pool
    char_pool = ""
    guaranteed = []
    
    if use_upper:
        char_pool += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        guaranteed.append(random.choice(string.digits))
    if use_special:
        char_pool += string.punctuation
        guaranteed.append(random.choice(string.punctuation))
        
    if not char_pool:
        print("Error: You must select at least one character set. Defaulting to lowercase + numbers.")
        char_pool = string.ascii_lowercase + string.digits
        guaranteed = [random.choice(string.ascii_lowercase), random.choice(string.digits)]
        use_lower, use_digits = True, True
        
    # Generate password
    remaining_len = length - len(guaranteed)
    password_chars = guaranteed + [random.choice(char_pool) for _ in range(remaining_len)]
    random.shuffle(password_chars)
    password = "".join(password_chars)
    
    print("=" * 40)
    print(f"Generated Password: {password}")
    print(f"Password Strength:  {check_strength(length, use_upper, use_lower, use_digits, use_special)}")
    print("=" * 40)

if __name__ == "__main__":
    main()
