# 🔗 URL Shortener

A lightweight **command-line URL shortener** built with pure Python. Generate short codes for long URLs, retrieve originals, search, delete, and persist everything to a local file — no external services needed.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🔀 **Generate short codes** — random 6-character alphanumeric codes
- 🔁 **Duplicate detection** — reuses existing short code if URL already exists
- 🔍 **Retrieve original URL** by short code
- 📋 **View all stored URLs** in one list
- 🔢 **Count total URLs** stored
- 🗑️ **Delete a URL** by short code
- 🔎 **Search URLs** by keyword (case-insensitive)
- 💾 **Auto-save & auto-load** — data persists across sessions via `urls.txt`
- ⚡ **Zero dependencies** — uses only built-in Python modules

---

## 🗂️ Menu Options

```
===== URL Shortener =====
1. Shorten URL
2. Retrieve URL
3. View All URLs
4. Total URLs Stored
5. Delete URL
6. Search URLs by Keyword
7. Exit
```

| Option | Description |
|---|---|
| 1 | Shorten a long URL and get a `short.ly/xxxxxx` link |
| 2 | Enter a short code to get the original URL back |
| 3 | List all stored short code → URL mappings |
| 4 | Display the total count of stored URLs |
| 5 | Delete a URL entry by its short code |
| 6 | Search all stored URLs by a keyword |
| 7 | Exit the program |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the App

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/url-shortener.git
cd url-shortener

# 2. Run the script
python url_shortener.py
```

---

## 📁 Project Structure

```
url-shortener/
├── url_shortener.py   # Main application script
├── urls.txt           # Auto-generated URL storage file
└── README.md          # This file
```

---

## 💡 Example Usage

```
===== URL Shortener =====
Enter your choice: 1
Enter the URL to shorten: https://www.github.com/Manahilch/my-chatbot
Shortened URL: short.ly/aB3kR9

Enter your choice: 2
Enter the short code: aB3kR9
Original URL: https://www.youtub.com/803479hhchld/wtyn

Enter your choice: 6
Enter a keyword: github
aB3kR9 -> https://www.github.com/hdguelw/my-4442

Enter your choice: 4
Total URLs stored: 1

Enter your choice: 5
Enter the short code to delete: aB3kR9
URL deleted successfully.
```

---

## 💾 Data File Format

URLs are saved to `urls.txt` automatically:

```
aB3kR9,https://www.github.com/your-username/my-project
xK7mPq,https://www.python.org/downloads/
Tz2wLn,https://docs.streamlit.io/
```

Each line follows the format: `short_code,original_url`

> The file is loaded automatically on startup so your URLs are always available between sessions.

---

## 🔮 Future Improvements

- [ ] Track click count per short URL
- [ ] Add expiry dates for short links
- [ ] Custom short codes chosen by the user
- [ ] Store data in SQLite for better scalability
- [ ] Web interface using Flask or Streamlit
- [ ] QR code generation for each short URL

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).