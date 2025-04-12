import os
from pathlib import Path

def get_all_filenames_without_ext(folder_path):
    """Get a set of filenames (without extensions) from a folder and its subfolders."""
    return {f.stem for f in Path(folder_path).rglob('*') if f.is_file()}

def delete_duplicate_files(source_folder, target_folder):
    """
    Delete files in target_folder that have the same base name (ignoring extension)
    as files in source_folder. Checks all subfolders recursively.
    """
    # Convert to absolute paths to avoid relative path issues
    source_folder = os.path.abspath(source_folder)
    target_folder = os.path.abspath(target_folder)

    # Get all filenames (without extensions) from source folder
    source_filenames = get_all_filenames_without_ext(source_folder)

    # Walk through target folder and delete duplicates
    for root, _, files in os.walk(target_folder):
        for file in files:
            # Get the base name without extension
            base_name = Path(file).stem
            if base_name in source_filenames:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

def main():
    # Define your folder paths
    source_folder = input("Enter the source folder path: ")
    target_folder = input("Enter the target folder path (where duplicates will be deleted): ")

    # Verify folders exist
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist!")
        return
    if not os.path.exists(target_folder):
        print(f"Target folder '{target_folder}' does not exist!")
        return

    # Confirm deletion
    print(f"\nThis will delete files in {target_folder} that have matching base names (ignoring extensions) in {source_folder}")
    confirm = input("Are you sure you want to proceed? (yes/no): ").lower()

    if confirm != 'yes':
        print("Operation cancelled.")
        return

    # Execute deletion
    print("\nChecking for duplicates...")
    delete_duplicate_files(source_folder, target_folder)
    print("\nOperation completed.")

if __name__ == "__main__":
    main()
