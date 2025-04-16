filename = input("Enter the filename: ")

try:
    # Try to open the file
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except IOError:
    print(f"An error occurred while reading the file '{filename}'.")

