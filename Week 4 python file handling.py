try:
    # Open the original file in read mode
    with open('input.txt', 'r') as file:
        content = file.read()

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open('output.txt', 'w') as new_file:
        new_file.write(modified_content)

    print("File has been modified and saved as 'output.txt'.")

except FileNotFoundError:
    print("The input file does not exist.")
except IOError:
    print("An error occurred while reading or writing the file.")
