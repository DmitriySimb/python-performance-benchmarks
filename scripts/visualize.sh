#!/bin/sh

path="$(cd "$(dirname "$0")" && pwd)"
project_root="$(cd "${path}/.." && pwd)"
data_dir="${project_root}/data"

if [ "$#" -ne 1 ]; then
    echo "Usage: sh scripts/visualize.sh <data_file>"
    echo "Example: sh scripts/visualize.sh email_filtering.dat"
    exit 1
fi

file_name="$1"
file_path="${data_dir}/${file_name}"

if [ ! -f "$file_path" ]; then
    echo "Error: file not found: ${file_path}"
    exit 1
fi

header="$(head -n 1 "$file_path")"

case "$header" in
    @*)
        ;;
    *)
        echo "Error: invalid data format. The first line must start with '@'."
        exit 1
        ;;
esac

categories=$(echo "$header" | sed 's/^@ //' | tr ',' '\n' | wc -l | tr -d ' ')

colors="red blue green magenta yellow cyan black"

set -- $colors
count=$#

selected_colors=""

seed=$(date +%s)

i=0
while [ "$i" -lt "$categories" ]; do
    index=$(( (seed + i) % count + 1 ))

    j=1
    for color in "$@"; do
        if [ "$j" -eq "$index" ]; then
            selected_colors="${selected_colors} ${color}"
            break
        fi
        j=$((j + 1))
    done

    i=$((i + 1))
done

termgraph "$file_path" --color $selected_colors