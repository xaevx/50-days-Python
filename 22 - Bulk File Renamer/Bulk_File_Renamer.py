import os


def rename_files(folder_path, prefix):

    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    files = [
        file for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]

    if not files:
        print("No files found.")
        return

    files.sort()

    for count, file in enumerate(files, start=1):

        old_path = os.path.join(folder_path, file)

        _, extension = os.path.splitext(file)

        new_name = f"{prefix}_{count}{extension}"

        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"{file}  →  {new_name}")

    print("\nAll files renamed successfully!")


print("=" * 45)
print("      BULK FILE RENAMER")
print("=" * 45)

folder = input("Enter Folder Path: ").strip()
prefix = input("Enter File Prefix: ").strip()

rename_files(folder, prefix)