# =========================================================
# FILE: 72_project_file_organizer.py
# PROJECT: FILE ORGANIZER
# =========================================================
#
# Skills Used:
# - pathlib
# - dictionaries
# - loops
# - file handling
# - safe dry-run design
#
# This script shows what would be moved.
# Change dry_run=False only when you understand the code.
#

from pathlib import Path
import shutil


EXTENSION_FOLDERS = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".csv": "data",
    ".json": "data",
    ".py": "python",
    ".zip": "archives",
}


def get_target_folder(file_path):
    extension = file_path.suffix.lower()
    folder_name = EXTENSION_FOLDERS.get(extension, "others")
    return file_path.parent / folder_name


def organize_folder(folder, dry_run=True):
    folder = Path(folder)
    moves = []

    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        target_folder = get_target_folder(file_path)
        target_path = target_folder / file_path.name

        moves.append((file_path, target_path))

        if not dry_run:
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(target_path))

    return moves


def display_moves(moves):
    if not moves:
        print("No files to organize.")
        return

    for source, target in moves:
        print(f"{source.name} -> {target.parent.name}/{target.name}")


def demo():
    print("File Organizer Demo")
    print("Dry run for current folder:")
    moves = organize_folder(".", dry_run=True)
    display_moves(moves[:10])


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add support for videos and audio files.
# 2. Add duplicate filename handling.
# 3. Add a log file.
# 4. Add argparse options.
# 5. Add undo support.
#
# =========================================================
# END OF 72_project_file_organizer.py
# =========================================================
