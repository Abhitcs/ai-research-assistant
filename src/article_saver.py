"""
Article Saver - Phase 1
Saves articles to local files for later AI analysis.
Author: Abhi
Date: March 2026
"""

import os
from datetime import datetime


# Where we store all articles
ARTICLES_FOLDER = "articles"


def setup():
    """
    Create the articles folder if it doesn't exist.
    This runs every time the program starts.
    """
    os.makedirs(ARTICLES_FOLDER, exist_ok=True)


def save_article():
    """
    Ask user for title and content, then save to a file.
    """
    print("\n📝 SAVE NEW ARTICLE")
    print("-" * 30)

    # Get input from user
    title = input("Enter article title: ").strip()
    
    # Validate: title cannot be empty
    if not title:
        print("❌ Title cannot be empty!")
        return
    
    print("Enter article content (press Enter twice when done):")
    
    # Collect multiple lines of content
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    content = "\n".join(lines)
    
    # Validate: content cannot be empty
    if not content:
        print("❌ Content cannot be empty!")
        return

    # Create a safe filename from the title
    # Example: "Python Basics!" → "python_basics.txt"
    filename = title.lower().replace(" ", "_")
    filename = "".join(c for c in filename if c.isalnum() or c == "_")
    filename = filename + ".txt"

    # Full path to save the file
    filepath = os.path.join(ARTICLES_FOLDER, filename)

    # Save the file
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"TITLE: {title}\n")
            file.write(f"DATE: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            file.write("-" * 40 + "\n")
            file.write(content)
        
        print(f"✅ Article '{title}' saved successfully!")
    
    except Exception as e:
        print(f"❌ Error saving article: {e}")


def list_articles():
    """
    Show all saved articles.
    """
    print("\n📚 SAVED ARTICLES")
    print("-" * 30)

    # Get all .txt files in articles folder
    try:
        files = os.listdir(ARTICLES_FOLDER)
        txt_files = [f for f in files if f.endswith(".txt")]

        if not txt_files:
            print("No articles saved yet.")
            return

        for i, filename in enumerate(txt_files, start=1):
            # Clean up filename for display
            display_name = filename.replace("_", " ").replace(".txt", "").title()
            print(f"{i}. {display_name}")
    
    except Exception as e:
        print(f"❌ Error listing articles: {e}")


def read_article():
    """
    Read and display a saved article.
    """
    print("\n📄 READ ARTICLE")
    print("-" * 30)

    title = input("Enter article title to read: ").strip()
    
    if not title:
        print("❌ Title cannot be empty!")
        return

    # Convert title to filename
    filename = title.lower().replace(" ", "_")
    filename = "".join(c for c in filename if c.isalnum() or c == "_")
    filename = filename + ".txt"

    filepath = os.path.join(ARTICLES_FOLDER, filename)

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        print("\n" + "=" * 40)
        print(content)
        print("=" * 40)
    
    except FileNotFoundError:
        print(f"❌ Article '{title}' not found!")
    except Exception as e:
        print(f"❌ Error reading article: {e}")


def main():
    """
    Main program loop. Shows menu and handles user choice.
    """
    # Setup folders before anything else
    setup()

    print("=" * 40)
    print("  AI RESEARCH ASSISTANT - Phase 1")
    print("=" * 40)

    while True:
        print("\nWhat would you like to do?")
        print("1. Save new article")
        print("2. List all articles")
        print("3. Read an article")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            save_article()
        elif choice == "2":
            list_articles()
        elif choice == "3":
            read_article()
        elif choice == "4":
            print("\n👋 Goodbye! Keep learning!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()