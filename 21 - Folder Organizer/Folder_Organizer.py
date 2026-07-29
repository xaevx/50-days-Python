import os
import shutil


FOLDER_PATH = input("Enter Folder Path: ").strip()

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
}


def organize_folder(folder):

    if not os.path.exists(folder):
        print("Folder not found.")
        return

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        for category, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination = os.path.join(folder, category)

                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, file))

                print(f"Moved: {file} → {category}")

                moved = True
                break

        if not moved:

            destination = os.path.join(folder, "Others")

            os.makedirs(destination, exist_ok=True)

            shutil.move(file_path, os.path.join(destination, file))

            print(f"Moved: {file} → Others")


print("=" * 45)
print("        FOLDER ORGANIZER")
print("=" * 45)

organize_folder(FOLDER_PATH)

print("\nFolder Organized Successfully!")