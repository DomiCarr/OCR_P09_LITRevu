#!/bin/zsh

# Output file
output_file="code.txt"

# Reset output
rm -f "$output_file"

# Header
echo "Generated $(date '+%Y-%m-%d %H:%M:%S')" >> "$output_file"
echo "\n\n" >> "$output_file"

# Extensions to include
exts=("py" "html" "css")

# Loop through extensions
for ext in $exts; do
    find reviews -type f -name "*.$ext" | sort | while IFS= read -r f; do
        echo "===============================================================================" >> "$output_file"
        echo "    $f " >> "$output_file"
        echo "===============================================================================" >> "$output_file"
        cat "$f" >> "$output_file"
        echo "\n\n" >> "$output_file"
    done
done

echo "Concaténation terminée → $output_file généré"
