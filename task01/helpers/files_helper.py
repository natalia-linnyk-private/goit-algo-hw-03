import os
import shutil

FILE_NAME_MAX_LENGTH = 250
FOLDER_NAME_FOR_NO_EXTENTION_FILES = "no_extension"

def is_file_copyable(file_path):
    try:
        if not os.access(file_path, os.R_OK):
            return False
        return True
    except (OSError, PermissionError):
        return False

def copy_file_to_extension_dir(file_path, destination_path, source_path) -> list[str]:
    errors_list = []
    try:
        extension = file_path.suffix.lower()
        if not extension:
            extension_dir_name = FOLDER_NAME_FOR_NO_EXTENTION_FILES
        else:
            extension_dir_name = extension[1:] if extension.startswith('.') else extension
            extension_dir_name = "".join(
                    c if c.isalnum() or c in "._-" else "_" 
                    for c in extension_dir_name)
            
        extension_dir = destination_path / extension_dir_name
        if not extension_dir.exists():
            extension_dir.mkdir(parents=True)
            
        relative_path = file_path.relative_to(source_path)
        safe_name = str(relative_path).replace(os.sep, "_").replace("/", "_").replace("\\", "_")
            
        max_length = FILE_NAME_MAX_LENGTH
        if len(safe_name) > max_length:
            if extension:
                name_part = safe_name[:-len(extension)] if safe_name.endswith(extension) else safe_name
                safe_name = name_part[:max_length - len(extension)] + extension
            else:
                safe_name = safe_name[:max_length]

        new_file_path = extension_dir / safe_name
        
        #Avoid file name duplication if we face them
        counter = 1
        while new_file_path.exists():
            stem = new_file_path.stem
            suffix = new_file_path.suffix
            new_file_path = extension_dir / f"{stem}_{counter}{suffix}"
            counter += 1
            
        shutil.copy2(file_path, new_file_path)
            
    except Exception as e:
        errors_list.append(f"Error copying file '{file_path}': {e}")
        pass
    return errors_list