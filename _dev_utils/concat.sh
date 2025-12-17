#!/bin/zsh
# concat.sh

# Absolute path to this script directory (_dev_utils)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Project root = parent of _dev_utils
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Output file in _dev_utils
OUTPUT_FILE="$SCRIPT_DIR/code.txt"

# Reset output
rm -f "$OUTPUT_FILE"

# Header
echo "Generated $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT_FILE"
echo "\n\n" >> "$OUTPUT_FILE"

# Extensions to include
EXTS=("py" "html" "css" "js")

# Directories to scan (relative to project root)
DIRS=("reviews" "reviews/static")

cd "$PROJECT_ROOT" || exit 1

for dir in "${DIRS[@]}"; do
    for ext in "${EXTS[@]}"; do
        find "$dir" -type f -name "*.$ext" | sort | while IFS= read -r f; do
            echo "===============================================================================" >> "$OUTPUT_FILE"
            echo "    $f" >> "$OUTPUT_FILE"
            echo "===============================================================================" >> "$OUTPUT_FILE"
            cat "$f" >> "$OUTPUT_FILE"
            echo "\n\n" >> "$OUTPUT_FILE"
        done
    done
done

echo "Concaténation terminée → $OUTPUT_FILE généré"
