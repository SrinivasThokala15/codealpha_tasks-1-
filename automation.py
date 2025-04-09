import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"],
}

FOLDER_PATH = "C:/Users/YourName/Downloads"

def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print("Folder does not exist!")
        return

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                category_path = os.path.join(FOLDER_PATH, category)

                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                shutil.move(file_path, os.path.join(category_path, file))
                print(f"Moved {file} to {category}/")
                break  

    print("File organization complete!")

if __name__=="__main__":
    organize_files()