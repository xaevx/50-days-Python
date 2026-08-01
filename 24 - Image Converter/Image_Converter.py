from PIL import Image
import os


def convert_images(folder_path, output_format):

    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    supported_formats = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"]

    converted = 0

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        if extension not in supported_formats:
            continue

        try:

            image = Image.open(file_path)

            if output_format.upper() == "JPEG":
                image = image.convert("RGB")

            new_name = os.path.splitext(file)[0] + "." + output_format.lower()
            output_path = os.path.join(folder_path, new_name)

            image.save(output_path, output_format.upper())

            converted += 1

            print(f"Converted: {file} → {new_name}")

        except Exception as error:
            print(f"Failed: {file} ({error})")

    print(f"\n{converted} image(s) converted successfully!")


print("=" * 45)
print("        IMAGE CONVERTER")
print("=" * 45)

folder = input("Enter Folder Path: ").strip()

print("\nAvailable Formats:")
print("JPEG")
print("PNG")
print("BMP")
print("GIF")
print("WEBP")

format_choice = input("\nConvert To: ").strip().upper()

convert_images(folder, format_choice)