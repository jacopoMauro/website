#!/bin/bash

# Define the base directory and the Python script to be executed
BASE_DIR="../content/publication"

# Find all directories in the BASE_DIR that belong to root
ROOT_OWNED_DIRS=$(find "$BASE_DIR" -maxdepth 1 -type d -user root)

# Loop through each directory
for DIR in $ROOT_OWNED_DIRS; 
do
    # Skip the base directory itself
    if [ "$DIR" != "$BASE_DIR" ]; then
        echo "Processing directory: $DIR"

        # Run the Python script on the directory
        python3 fix_markup.py "$DIR"/index.md

        # Change ownership of the directory and its contents to user 'mauro' and group 'mauro'
        chown -R mauro:mauro "$DIR"
    fi
done

# Generate git command
# Remove the base directory from the list
ROOT_OWNED_DIRS=$(echo "$ROOT_OWNED_DIRS" | grep -v "^$BASE_DIR$")
# Print the remaining directories, space-separated
echo "Rember to add the changes to git running"
echo "git add $(echo "$ROOT_OWNED_DIRS" | tr '\n' ' ')"