# Arabic-Hebrew to English File Renamer

## Overview
This script is designed to rename files and folders by translating Arabic and Hebrew characters to their corresponding English letters based on a predefined character map. It's particularly useful for ensuring compatibility of file and folder names on systems that do not support Unicode or specific character sets like Arabic or Hebrew.

## How to Use
### General Setup
1. **Setting Up**: Clone this repository or download the script `ArabicHebrewToEnglishRenamer.py` to your local machine.

2. **Prerequisites**: Ensure you have Python installed on your system. This script was developed and tested with Python 3.x.

3. **Configure the Script**: Edit the `ArabicHebrewToEnglishRenamer.py` file to set the `folder_path` variable to the path of the folder containing the files and subfolders you wish to rename.

### Running the Script
- **On Linux**:
  - Open a terminal in the directory containing the script.
  - Execute the script with Python:
    ```bash
    python3 ArabicHebrewToEnglishRenamer.py
    ```
  - If necessary, run the script with `sudo` for the required permissions.

- **On Windows**:
  - Open Command Prompt or PowerShell in the directory containing the script.
  - Execute the script with Python:
    ```bash
    python ArabicHebrewToEnglishRenamer.py
    ```

- **On macOS**:
  - Open Terminal in the directory containing the script.
  - Execute the script with Python:
    ```bash
    python3 ArabicHebrewToEnglishRenamer.py
    ```

5. **Check the Output**: The script will output the progress of the renaming process, including any files or directories it renames, and any errors encountered.

## Important Notes
- **Backup Your Data**: Always backup your files and directories before running this script to prevent accidental data loss.
- **Use with Caution**: Be cautious when running this script on system directories or critical data, as incorrect renaming can disrupt system functionality.
- **Permission Requirements**: On Linux, you might need elevated permissions to rename files in certain directories. Windows and macOS users typically won't need special permissions for personal files.

## Character Mapping
The script uses the following character mappings for translation:
- Arabic: `{'ا': 'a', 'ب': 'b', ...}`
- Hebrew: `{'א': 'a', 'ב': 'b', ...}`

(Complete the character mapping list here)

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact
Jawdat Abdullah - Jawdat.89@gmail.com

Project Link: [https://github.com/jawdat89/ArabicHebrewToEnglishRename](https://github.com/jawdat89/ArabicHebrewToEnglishRename)