#!/bin/zsh
# dir.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

OUTPUT_FILE="$SCRIPT_DIR/directories.txt"

rm -f "$OUTPUT_FILE"

echo "Generated $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT_FILE"
echo "\nListing all files and folders in project root (excluding env/, hidden files, and __pycache__):\n" >> "$OUTPUT_FILE"

print_tree() {
    local dir="$1"
    local indent="$2"

    for f in "$dir"/*; do
        [[ "$(basename "$f")" == .* ]] && continue
        [[ "$(basename "$f")" == "env" ]] && continue
        [[ "$(basename "$f")" == "__pycache__" ]] && continue

        echo "${indent}${f#$PROJECT_ROOT/}" >> "$OUTPUT_FILE"

        [[ -d "$f" ]] && print_tree "$f" "${indent}    "
    done
}

print_tree "$PROJECT_ROOT" ""
echo "\nDone → $OUTPUT_FILE generated"
