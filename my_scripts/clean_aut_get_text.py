import os

# Folder containing the publications
BASE_DIR = "../content/publication"

# The exact string to remove
PLACEHOLDER_TEXT = "Add the **full text** or **supplementary notes** for the publication here using Markdown formatting."

def clean_markdown_files(base_dir, placeholder):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".md"):
                file_path = os.path.join(root, file)

                # Read file content
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check and remove placeholder if present
                if placeholder in content:
                    new_content = content.replace(placeholder, "")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Cleaned placeholder from: {file_path}")

if __name__ == "__main__":
    clean_markdown_files(BASE_DIR, PLACEHOLDER_TEXT)
