import sys

def fix_markup(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Iterate through the lines and find the target line containing "publication_types:"
    for i in range(len(lines)):
        if "publication_types:" in lines[i]:
            # Ensure we are not at the last line to avoid IndexError
            if i + 1 < len(lines):
                lines[i + 1] = "- '1'\n"
            break

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_markup.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    fix_markup(file_path)