"""
My first Python program in this journey.
Author: [Your Name]
Date: [Today's Date]
"""

def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to your AI Research Assistant journey."

def main():
    print("=" * 50)
    print("AI RESEARCH ASSISTANT - Version 0.1")
    print("=" * 50)
    
    my_name = "Abhi"  # Change this to your name
    message = greet(my_name)
    print(message)
    
    print("\nSetup complete! Ready to build something amazing.")
    print("=" * 50)

if __name__ == "__main__":
    main()