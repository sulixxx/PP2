def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One or both files not found.")

# Input the source and destination file paths
source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

copy_file(source_file, destination_file)
