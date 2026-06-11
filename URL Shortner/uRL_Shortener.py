import random
import string
url_database = {}
try:
    with open("urls.txt", "r") as file:
        for line in file:
            short_code, original_url = line.strip().split(",", 1)
            url_database[short_code] = original_url
except FileNotFoundError:
    pass
while True:
    print("\n===== URL Shortener =====")
    print("1. Shorten URL")
    print("2. Retrieve URL")
    print("3. View All URLs")
    print("4. Total URLs Stored")
    print("5. Delete URL")
    print("6. Search URLs by Keyword")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        original_url = input("Enter the URL to shorten: ")
        found = False
        for code, url in url_database.items():
            if url == original_url:
                print(f"URL already exists: short.ly/{code}")
                found = True
                break
        if not found:
            short_code = ''.join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=6
                )
            )
            url_database[short_code] = original_url
            with open("urls.txt", "a") as file:
                file.write(f"{short_code},{original_url}\n")
            print(f"Shortened URL: short.ly/{short_code}")
    elif choice == "2":
        short_code = input("Enter the short code: ")
        if short_code in url_database:
            print(f"Original URL: {url_database[short_code]}")
        else:
            print("URL not found.")
    elif choice == "3":
        if url_database:
            print("\nAll URLs:")
            for code, url in url_database.items():
                print(f"{code} -> {url}")
        else:
            print("No URLs stored.")
    elif choice == "4":
        print(f"Total URLs stored: {len(url_database)}")
    elif choice == "5":
        short_code = input("Enter the short code to delete: ")
        if short_code in url_database:
            del url_database[short_code]
            with open("urls.txt", "w") as file:
                for code, url in url_database.items():
                    file.write(f"{code},{url}\n")
            print("URL deleted successfully.")
        else:
            print("URL not found.")
    elif choice == "6":
        keyword = input("Enter a keyword: ")
        found = False
        for code, url in url_database.items():
            if keyword.lower() in url.lower():
                print(f"{code} -> {url}")
                found = True
        if not found:
            print("No URLs found.")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")