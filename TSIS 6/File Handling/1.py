import os

def display_directories_and_files(path):
    print("List of directories and files:")
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        for directory in dirs:
            print(f"    {directory}/")
        for file in files:
            print(f"    {file}")

specified_path = input("Enter the path: ")

display_directories_and_files(specified_path)
