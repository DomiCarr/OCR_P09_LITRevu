#!/bin/zsh

# Output file
output_file="directories.txt"

# Reset output
rm -f "$output_file"

# Header
echo "Generated $(date '+%Y-%m-%d %H:%M:%S')" >> "$output_file"
echo "\nListing all files and folders in '.' (excluding env/, hidden files, and __pycache__):\n" >> "$output_file"

# Recursive function
print_tree() {
    local dir="$1"
    local indent="$2"

    for f in "$dir"/*; do
        # Skip hidden files, env folder, and __pycache__
        [[ "$(basename "$f")" == .* ]] && continue
        [[ "$(basename "$f")" == "env" ]] && continue
        [[ "$(basename "$f")" == "__pycache__" ]] && continue

        # Print file or folder
        echo "${indent}$f" >> "$output_file"

        # Recurse if directory
        [[ -d "$f" ]] && print_tree "$f" "${indent}    "
    done
}

# Start recursion
print_tree "." ""
echo "\nDone → $output_file generated"
