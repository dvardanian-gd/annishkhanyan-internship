#!/bin/bash

operation="" # initializing the variables used
word1=""
word2=""
input_file=""
output_file=""

while getopts ":vs:rli:o:u" opt; do
    case "$opt" in
        v)
            operation="v"
            ;;
        s)
            operation="s"
            word1="$OPTARG"
            word2="${!OPTIND}"   # get the next argument after -s
            ((OPTIND++))         # increment OPTIND to skip it
            ;;
        r)
            operation="r"
            ;;
        l)
            operation="l"
            ;;
        u)
            operation="u"
            ;;
        i)
            input_file="$OPTARG"
            ;;
        o)
            output_file="$OPTARG"
            ;;
        *)
            echo "Invalid input" >&2
            exit 1
            ;;
    esac
done

# Validate required arguments
if [[ -z "$input_file" || -z "$output_file" || -z "$operation" ]]; then
    echo "Invalid input: missing -i, -o, or operation flag" >&2
    exit 1
fi

# Check if input file exists
if [[ ! -f "$input_file" ]]; then
    echo "Invalid file: $input_file not found" >&2
    exit 1
fi

# Main logic
case "$operation" in
    v)
        tr 'a-zA-Z' 'A-Za-z' < "$input_file" > "$output_file"
        ;;
    s)
        if [[ -z "$word1" || -z "$word2" ]]; then
            echo "Invalid format: two words required after -s" >&2
            exit 1
        fi
        sed "s/${word1}/${word2}/g" "$input_file" > "$output_file"
        ;;
    r)
        tac "$input_file" > "$output_file"
        ;;
    l)
        tr '[:upper:]' '[:lower:]' < "$input_file" > "$output_file"
        ;;
    u)
        tr '[:lower:]' '[:upper:]' < "$input_file" > "$output_file"
        ;;
    *)
        echo "Invalid operation" >&2
        exit 1
        ;;
esac
