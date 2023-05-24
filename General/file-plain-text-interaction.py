filename = "output.txt"

# Open the file in write mode
with open(filename, "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.")


# Open the file in read mode
with open(filename, "r") as file:
    file_content = file.read()
    
    # Line by line
    for index, line in enumerate(file_content.split("\n")):
        print(f"Line {index}: {line}")

    # All file content
    print(file_content)
