import os
import shutil

source_folder = "Downloads"

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}


def organize_files():
    if not os.path.exists(source_folder):
        print(f"Folder '{source_folder}' does not exist.")
        return

    moved_files = 0

    for filename in os.listdir(source_folder):

        file_path = os.path.join(source_folder, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        category = "Others"

        for folder, extensions in categories.items():
            if extension in extensions:
                category = folder
                break

        destination_folder = os.path.join(source_folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)

        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename} → {category}")
            moved_files += 1

        except Exception as error:
            print(f"Could not move {filename}: {error}")

    print("\n-----------------------------")
    print("Organization complete!")
    print(f"Files moved: {moved_files}")
    print("-----------------------------")


organize_files()