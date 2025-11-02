#!/bin/bash

while getopts ":s:i:o:" opt; do 
    case $opt in
        s) shift_val=$OPTARG ;;
        i) input_val=$OPTARG ;;
        o) output_file=$OPTARG ;;
        *) echo "Invalid input" >&2; exit 1 ;;
    esac
done

if [[ -z "$shift_val" || -z "$input_val" || -z "$output_file" ]]; then # check the input
    echo "invalid input format"
    exit 1
fi

caesar() {
    local text="$1"
    local shift=$((shift_val % 26))
    local res=""

    for ((i=0; i<${#text}; i++)); do
        char="${text:i:1}"
        asc=$(printf "%d" "'$char")

        if [[ $char =~ [A-Z] ]]; then
            upd=$((asc + shift))
            ((upd > 90)) && upd=$((upd - 26))
            res+=$(printf "%b" "\\$(printf '%03o' "$upd")")

        elif [[ $char =~ [a-z] ]]; then
            upd=$((asc + shift))
            ((upd > 122)) && upd=$((upd - 26))
            res+=$(printf "%b" "\\$(printf '%03o' "$upd")")

        else
            res+="$char"
        fi
    done

    echo "$res"
}

: > "$output_file" # clear the output file before writing

while IFS= read -r line; do
    caesar "$line" >> "$output_file" # reading each line of input file
done < "$input_val"
