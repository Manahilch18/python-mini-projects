# 🗂️ File Organizer

A lightweight **command-line file organizer** written in pure Python that automatically sorts files in any folder into categorized subfolders by file type.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 📁 **Auto-sorts files** into categorized subfolders (Images, PDFs, Documents, Audio, Videos)
- 👀 **Before & after view** — lists folder contents before and after organizing
- 📊 **Summary report** — shows total number of files moved
- ⚡ **Zero dependencies** — uses only Python's built-in `os` and `shutil` modules
- 🛡️ **Safe execution** — creates subfolders only when needed, skips non-file items

---

## 📂 Folder Categories

| Folder | File Extensions |
|---|---|
| 🖼️ Images | `.jpg` `.jpeg` `.png` `.gif` |
| 📄 PDFs | `.pdf` |
| 📝 Documents | `.doc` `.docx` `.txt` |
| 🎵 Audio | `.mp3` `.wav` |
| 🎬 Videos | `.mp4` `.mkv` |

> Files with extensions not in the above list are left in place.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the Script

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/file-organizer.git
cd file-organizer

# 2. Run the script
python file_organizer.py
```

Then enter the full path to the folder you want to organize when prompted.

---

## 📁 Project Structure

```
file-organizer/
├── file_organizer.py   # Main script
└── README.md           # This file
```

---

## 💡 Example Usage

```
Enter folder path: C:\Users\John\Downloads

===== BEFORE ORGANIZING =====
photo.jpg
report.pdf
song.mp3
notes.txt
movie.mp4

 Moved: photo.jpg → Images
 Moved: report.pdf → PDFs
 Moved: song.mp3 → Audio
 Moved: notes.txt → Documents
 Moved: movie.mp4 → Videos

===== AFTER ORGANIZING =====

 Images
   └── photo.jpg

 PDFs
   └── report.pdf

 Audio
   └── song.mp3

 Documents
   └── notes.txt

 Videos
   └── movie.mp4

===== SUMMARY =====
Total files moved: 5

 Files organized successfully!
```

---

## ⚠️ Notes

- The script only moves **files**, not subfolders already present in the directory.
- If a destination subfolder (e.g. `Images/`) already exists, it will be reused — not overwritten.
- Files with **unrecognized extensions** are left untouched in the original folder.

---

## 🔮 Future Improvements

- [ ] Add support for more file types (Spreadsheets, Archives, Code files)
- [ ] Undo/restore functionality to move files back
- [ ] Dry-run mode to preview changes before applying
- [ ] GUI version using Tkinter or a web interface
- [ ] Watch a folder and auto-organize on new file additions

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).