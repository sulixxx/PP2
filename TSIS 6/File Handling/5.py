def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

# Input the file path and the list
file_path = input("Enter the file path: ")
data = input("Enter the list (comma-separated): ").split(',')

# Write the list to the file
write_list_to_file(file_path, data)
print(f"The list has been written to the file '{file_path}'.")
