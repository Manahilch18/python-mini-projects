import os
import shutil

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print(" Folder not found!")
    exit()

print("\n===== BEFORE ORGANIZING =====")

for item in os.listdir(folder_path):
    print(item)

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}
moved_files = 0

# Organize files
for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        for folder_name, extensions in folders.items():

            if extension in extensions:

                destination_folder = os.path.join(
                    folder_path,
                    folder_name
                )

                # Create folder only when needed
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                destination = os.path.join(
                    destination_folder,
                    file
                )

                shutil.move(file_path, destination)

                print(f" Moved: {file} → {folder_name}")

                moved_files += 1
                break

print("\n===== AFTER ORGANIZING =====")

for item in os.listdir(folder_path):

    item_path = os.path.join(folder_path, item)

    if os.path.isdir(item_path):

        print(f"\n {item}")

        for sub_file in os.listdir(item_path):
            print(f"   └── {sub_file}")

    else:
        print(f" {item}")

print("\n===== SUMMARY =====")
print(f"Total files moved: {moved_files}")

print("\n Files organized successfully!")