from pathlib import Path
import shutil
import logging

#Source folder
source_folder = Path("Downloads")

#File Categories
categories = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents" : [".pdf", ".doc", ".docx", ".txt", ".xlsx",".pptx"],
    "Videos" : [".mp4", ".mkv", ".avi", ".mov"],
    "Audio" : [".mp3", ".wav", ".aac"],
    "Archives" : [".zip", ".rar", ".7z", ".tar", ".gz"]
}

#Configure logging
logging.basicConfig(
    filename = "file_organizer.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def organize_files():
    if not source_folder.exists():
        print(f"Folder '{source_folder}' does not exist.")
        logging.error(f"Soruce folder not found: {source_folder}")
        return

    moved_files = 0
    skipped_files = 0

    for file_path in source_folder.iterdir():

        #Ignore folders
        if not file_path.is_file():
            continue

        extension = file_path.suffix.lower()

        category = "Others"

        #Find category
        for folder, extensions in categories.items():
            if extension in extensions:
                category = folder
                break

        #Create destination folder
        destination_folder = source_folder / category
        destination_folder.mkdir(exist_ok=True)

        destination_path = destination_folder / file_path.name

        #Handle duplicate filenames
        if destination_path.exists():
            print(f"Skipped: {file_path.name} (already exists)")
            logging.warning(
                f"Skipped duplicate files: {file_path.name}"
            ) 
            skipped_files += 1
            continue

        try:
            shutil.move(str(file_path), str(destination_path))

            print(f"Moved {file_path.name} → {category}")

            logging.info(
                f"Moved {file_path.name} →  {category}"
            )

            moved_files += 1

        except Exception as error:
            print(f"Could not move {file_path.name}: {error}")

            logging.error(
                f"Failed to move {file_path.name}: {error}"
            )

    print("\n-----------------------------")
    print("Organization complete!")
    print(f"Files moved: {moved_files}")
    print(f"Files skipped: {skipped_files}")
    print("-----------------------------")


if __name__ == "__main__":
    organize_files()