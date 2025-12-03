from pathlib import Path
from helpers.files_helper import is_file_copyable, copy_file_to_extension_dir

def move_sort_files(source_path: Path, destination_path: Path) -> list[str]:
    errors_list = []
    for item in source_path.iterdir():
        try:
            if item.is_dir():
                results_list = move_sort_files(item, destination_path)
                if len(results_list) > 0:
                    errors_list.extend(results_list)
            elif item.is_file():
                if is_file_copyable(item):
                    copying_file_errors = copy_file_to_extension_dir(item, destination_path, source_path)
                    if len(copying_file_errors) > 0:
                        errors_list.extend(copying_file_errors)
                else:
                    errors_list.append(f"File is not available for copying: {item.name}")
        except (PermissionError, OSError) as e:
            errors_list.append(f"Error accessing file '{item.name}': {e}")
            continue
    return errors_list