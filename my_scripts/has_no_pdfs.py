import os

# Path to your publications folder
base_path = "../content/publication"

# Ensure the path exists
if not os.path.exists(base_path):
    print(f"The folder '{base_path}' does not exist.")
    exit()

# List to store folders missing PDF files
folders_missing_pdfs = []

# Walk through each subfolder in content/publication
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    if os.path.isdir(folder_path):
        # Check for any PDF in this folder
        has_pdf = any(file.lower().endswith('.pdf') for file in os.listdir(folder_path))
        if not has_pdf:
            folders_missing_pdfs.append(folder_name)

# Report results
if folders_missing_pdfs:
    print("Folders without PDF files:")
    for folder in folders_missing_pdfs:
        print(f"- {folder}")
else:
    print("✅ All folders contain at least one PDF file.")
