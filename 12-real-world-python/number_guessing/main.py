#!/usr/bin/env python3
"""
Real-world Project #2: Number Guessing Game
-------------------------------------------
An interactive CLI game where the user guesses a randomly generated number
within customized limits, receiving helpful hints and score stats.
"""

import random

def main():
    print("=" * 40)
    print("      CLI NUMBER GUESSING GAME      ")
    print("=" * 40)
    
    try:
        lower = int(input("Enter lower limit (default 1): ") or "1")
        upper = int(input("Enter upper limit (default 100): ") or "100")
    except ValueError:
        print("Invalid inputs, defaulting to 1 - 100.")
        lower, upper = 1, 100
        
    if lower >= upper:
        print("Invalid bounds. Lower must be less than upper. Resetting to 1 - 100.")
        lower, upper = 1, 100
        
    secret_number = random.randint(lower, upper)
    attempts = 0
    max_attempts = int(abs(upper - lower) ** 0.5) + 3
    
    print(f"I've chosen a number between {lower} and {upper}.")
    print(f"You have maximum {max_attempts} attempts to guess it.")
    print("=" * 40)
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
            # Additional hint for remaining turns
            if attempts < max_attempts and abs(guess - secret_number) <= 3:
                print("Hint: You are extremely close (within 3 numbers)!")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    else:
        print(f"Game Over! The number was {secret_number}.")

if __name__ == "__main__":
    main()
