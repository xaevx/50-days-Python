# Bulk File Renamer

A simple command-line **Bulk File Renamer** built with Python. It automatically renames all files in a selected folder using a custom prefix while preserving their original file extensions.

## Features

- Rename Multiple Files at Once
- Automatic Numbering
- Preserves File Extensions
- Displays Rename Progress
- Simple Command-Line Interface

## Run the Project

```bash
python Bulk_File_Renamer.py
```

Example:

```text
Enter Folder Path:
C:\Users\YourName\Pictures

Enter File Prefix:
Vacation
```

Output:

```text
IMG_1024.jpg  →  Vacation_1.jpg
IMG_1025.jpg  →  Vacation_2.jpg
IMG_1026.jpg  →  Vacation_3.jpg
```

## Project Structure

```
Bulk-File-Renamer/
│
├── bulk_file_renamer.py
└── README.md
```

## Modules Used

- Python 3
- os module

## Wha i learned

- File Handling
- Directory Operations
- Loops
- String Formatting
- Functions
- File Renaming
- Path Handling

> **Note:** Existing filenames will be replaced. Make sure the selected folder contains only the files you want to rename.

---

⭐ Part of my **#50DaysOfPython** challenge.