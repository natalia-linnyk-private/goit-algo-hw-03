from pathlib import Path

def validate_folder_exists(path: Path) -> None:
    if not path.exists() or not path.is_dir():
        raise ValueError(f"The provided path '{path}' is not a valid directory or this directory does not exist.")

def validate_or_create_destination_folder(destination_root: str, source_path: Path) -> Path: 
    destination_path = Path(destination_root) if destination_root else None
    if destination_path is None:
        destination_path = source_path.parent / "dist"
        if not destination_path.exists():
            destination_path.mkdir(parents=True)
    else:
        validate_folder_exists(destination_path)
    return destination_path

def validate_source_folder(source_root: str) -> Path:
    if len(source_root) == 0:
        raise ValueError("Source path cannot be empty.")
    source_path = Path(source_root)
    validate_folder_exists(source_path)
    return source_path