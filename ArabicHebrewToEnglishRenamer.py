import os

# Define the folder path here
folder_path = "/run/media/jawdat/Lenovo 64G/358"

print("Started renaming process...")

# Mapping of Arabic and Hebrew characters to English
char_map = {
    'ء': '2','ا': 'a','أ': 'a','آ': 'a', 'ب': 'b', 'ت': 't','ة': 't', 'ث': 'th',
    'ج': 'j', 'ح': '7', 'خ': 'kh', 'ؤ': 'ao', 
    'د': 'd', 'ذ': 'th', 'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'sh', 'ص': 's', 
    'ط': 't', 'ظ': 'th', 'ع': '3', 'غ': '5', 'ف': 'f', 'ق': 'k', 'ك': 'k', 
    'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h', 'و': 'o', 'ي': 'y',
    'א': 'a', 'ב': 'b', 'ג': 'c', 'ד': 'd', 'ה': 'h', 'ו': 'o', 'ז': 'z',
    'ח': '7', 'ט': 't', 'י': 'y', 'כ': 'kh', 'ל': 'l', 'מ': 'm', 'נ': 'n', 
    'צ': 's', 'ע': '3', 'פ': 'f', 'ס': 's', 'ק': 'k', 'ר': 'r', 'ש': 'sh', 'ת': 't'
}


def translate_name(name):
    """Translate the name of the file from Arabic/Hebrew to English based on the mapping."""
    return ''.join(char_map.get(char, char) for char in name)

def rename_files_and_folders(root_folder):
    """Rename all files and folders in the specified root folder and its subfolders."""
    for root, dirs, files in os.walk(root_folder, topdown=False):
        # Rename files
        for file in files:
            if any(char in char_map for char in file):
                new_name = translate_name(file)
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)
                new_path = attempt_rename(old_path, new_path)

        # Rename directories
        for dir in dirs:
            if any(char in char_map for char in dir):
                new_name = translate_name(dir)
                old_path = os.path.join(root, dir)
                new_path = os.path.join(root, new_name)
                new_path = attempt_rename(old_path, new_path)

def attempt_rename(old_path, new_path):
    """Attempt to rename the file or directory, adding a suffix if the name already exists."""
    suffix = 1
    original_new_path = new_path
    while os.path.exists(new_path):
        # Add a suffix if the file/directory exists
        new_path = f"{original_new_path}({suffix})"
        suffix += 1
    try:
        os.rename(old_path, new_path)
        print(f"Renamed '{old_path}' to '{new_path}'")
    except Exception as e:
        print(f"Error renaming '{old_path}': {e}")
    return new_path

# Start the renaming process using the defined folder path
rename_files_and_folders(folder_path)