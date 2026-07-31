from PyPDF2 import PdfMerger
import os


def merge_pdfs(folder_path, output_name):

    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    merger = PdfMerger()

    pdf_files = [
        file for file in os.listdir(folder_path)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("No PDF files found.")
        return

    pdf_files.sort()

    for pdf in pdf_files:

        pdf_path = os.path.join(folder_path, pdf)
        merger.append(pdf_path)

        print(f"Added: {pdf}")

    output_path = os.path.join(folder_path, output_name)

    merger.write(output_path)
    merger.close()

    print(f"\nPDF merged successfully!")
    print(f"Saved as: {output_path}")


print("=" * 45)
print("           PDF MERGER")
print("=" * 45)

folder = input("Enter Folder Path: ").strip()
output = input("Output File Name (with .pdf): ").strip()

merge_pdfs(folder, output)