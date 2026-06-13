import random
import string
import json
from datetime import datetime, timedelta
url_database = {}
def save_database():
    with open("urls.json", "w") as file:
        json.dump(url_database, file, indent=2)

def load_database():
    global url_database
    try:
        with open("urls.json", "r") as file:
            url_database = json.load(file)
    except FileNotFoundError:
        try:
            with open("urls.txt", "r") as file:
                for line in file:
                    short_code, original_url = line.strip().split(",", 1)
                    url_database[short_code] = {"url": original_url, "clicks": 0, "expiry": None}
            save_database()
        except FileNotFoundError:
            pass

def is_expired(entry):
    if entry.get("expiry") is None:
        return False
    return datetime.now() > datetime.fromisoformat(entry["expiry"])

def format_entry(code, entry):
    expiry_str = entry.get("expiry")
    if expiry_str:
        expiry_dt = datetime.fromisoformat(expiry_str)
        if datetime.now() > expiry_dt:
            expiry_label = "EXPIRED"
        else:
            remaining = expiry_dt - datetime.now()
            days = remaining.days
            hours, rem = divmod(remaining.seconds, 3600)
            expiry_label = f"expires in {days}d {hours}h"
    else:
        expiry_label = "no expiry"
    clicks = entry.get("clicks", 0)
    return f"short.ly/{code}  ->  {entry['url']}  |  clicks: {clicks}  |  {expiry_label}"

load_database()
while True:
    print("\n===== URL Shortener =====")
    print("1. Shorten URL")
    print("2. Retrieve URL")
    print("3. View All URLs")
    print("4. Total URLs Stored")
    print("5. Delete URL")
    print("6. Search URLs by Keyword")
    print("7. View URL Stats")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        original_url = input("Enter the URL to shorten: ")
        found = False
        for code, entry in url_database.items():
            if entry["url"] == original_url and not is_expired(entry):
                print(f"URL already exists: short.ly/{code}")
                found = True
                break
        if not found:
            expiry_input = input("Set expiry? (e.g. 7d, 24h, or press Enter to skip): ").strip()
            expiry_dt = None
            if expiry_input:
                try:
                    if expiry_input.endswith("d"):
                        expiry_dt = datetime.now() + timedelta(days=int(expiry_input[:-1]))
                    elif expiry_input.endswith("h"):
                        expiry_dt = datetime.now() + timedelta(hours=int(expiry_input[:-1]))
                    else:
                        print("Invalid format. No expiry set.")
                except ValueError:
                    print("Invalid value. No expiry set.")
            short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            url_database[short_code] = {"url": original_url, "clicks": 0, "expiry": expiry_dt.isoformat() if expiry_dt else None}
            save_database()
            expiry_msg = f" (expires: {expiry_dt.strftime('%Y-%m-%d %H:%M')})" if expiry_dt else ""
            print(f"Shortened URL: short.ly/{short_code}{expiry_msg}") 
    elif choice == "2":
        short_code = input("Enter the short code: ")
        if short_code in url_database:
            entry = url_database[short_code]
            if is_expired(entry):
                print("This short URL has expired.")
            else:
                entry["clicks"] += 1
                save_database()
                print(f"Original URL: {entry['url']}")
                print(f"Total clicks: {entry['clicks']}")
        else:
            print("URL not found.")
    elif choice == "3":
        if url_database:
            print("\nAll URLs:")
            for code, entry in url_database.items():
                status = " [EXPIRED]" if is_expired(entry) else ""
                print(f"{format_entry(code, entry)}{status}")
        else:
            print("No URLs stored.")
    elif choice == "4":
        active = sum(1 for e in url_database.values() if not is_expired(e))
        expired = len(url_database) - active
        print(f"Total URLs stored: {len(url_database)}  (active: {active}, expired: {expired})") 
    elif choice == "5":
        short_code = input("Enter the short code to delete: ")
        if short_code in url_database:
            save_database()
            print("URL deleted successfully.")
        else:
            print("URL not found.")
    elif choice == "6":
        keyword = input("Enter a keyword: ")
        found = False
        for code, entry in url_database.items():
            if keyword.lower() in entry["url"].lower():
                status = " [EXPIRED]" if is_expired(entry) else ""
                print(f"{format_entry(code, entry)}{status}")
                found = True
        if not found:
            print("No URLs found.")
    elif choice == "7":
        short_code = input("Enter the short code to view stats: ")
        if short_code in url_database:
            entry = url_database[short_code]
            print(f"\n--- Stats for short.ly/{short_code} ---")
            print(f"Original URL : {entry['url']}")
            print(f"Click count  : {entry.get('clicks', 0)}")
            if entry.get("expiry"):
                expiry_dt = datetime.fromisoformat(entry["expiry"])
                status = "EXPIRED" if datetime.now() > expiry_dt else expiry_dt.strftime('%Y-%m-%d %H:%M')
                print(f"Expiry       : {status}")
            else:
                print(f"Expiry       : None (never expires)")
        else:
            print("URL not found.")

    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")