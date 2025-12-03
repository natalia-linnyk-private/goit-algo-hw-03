from helpers.folders_helper import validate_source_folder, validate_or_create_destination_folder
from helpers.sorting_helper import move_sort_files

def main():
    while True:
        source_root = input("Enter the source root directory path (or print 'exit' to quit) >>>: ")
        if source_root.lower() == 'exit':
            break
        try:
            source_path = validate_source_folder(source_root)
            destination_root = input("Enter the destination root directory path or leave it empty >>> ")
            destination_path = validate_or_create_destination_folder(destination_root, source_path)
            errors_list = move_sort_files(source_path, destination_path)
            print("Processing completed.")
            if len(errors_list) > 0:
                print("The following errors occurred during file processing:")
                for error in errors_list:
                    print(error)
            else:
                print("All files have been successfully sorted and moved.")
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main()