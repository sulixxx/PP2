import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            except OSError as e:
                print(f"Error: {e}")
        else:
            print(f"No write access to '{file_path}'. Cannot delete the file.")
    else:
        print(f"File '{file_path}' does not exist.")

file_path = input("Enter the file path: ")

delete_file(file_path)
