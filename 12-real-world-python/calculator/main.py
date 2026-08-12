#!/usr/bin/env python3
"""
Real-world Project #1: CLI Calculator
-------------------------------------
A simple interactive command-line calculator that parses math expressions,
supports historical calculations, and handles error boundaries gracefully.
"""

import sys

def show_menu():
    print("=" * 40)
    print("        INTERACTIVE CLI CALCULATOR        ")
    print("=" * 40)
    print("Commands:")
    print("  [expr]  e.g., 2 + 3 * 5")
    print("  history Show calculation history")
    print("  clear   Clear calculation history")
    print("  exit    Exit application")
    print("=" * 40)

def evaluate_expression(expr: str) -> float:
    # Sanitizing input to only allow mathematical symbols and numbers
    allowed_chars = "0123456789+-*/(). "
    cleaned = "".join([c for c in expr if c in allowed_chars])
    
    if not cleaned.strip():
        raise ValueError("Invalid mathematical character input.")
    
    # Safe evaluation of basic math expressions using eval
    # (Safe here due to character whitelist checks)
    return eval(cleaned)

def main():
    history = []
    show_menu()
    
    while True:
        try:
            user_input = input("calc > ").strip()
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
                
            elif user_input.lower() == "history":
                if not history:
                    print("No calculations recorded yet.")
                else:
                    print("Calculation History:")
                    for idx, item in enumerate(history, 1):
                        print(f"  {idx}. {item}")
                continue
                
            elif user_input.lower() == "clear":
                history.clear()
                print("History cleared.")
                continue
            
            # Evaluate math expression
            result = evaluate_expression(user_input)
            record = f"{user_input} = {result}"
            history.append(record)
            print(f"Result: {result}")
            
        except ZeroDivisionError:
            print("Error: Division by zero is undefined.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
