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
            word2="${!OPTIND}"   # optind keeps the index of the opt arguments, here we expand the next varialble
            shift                # and we need to skip it as we saved it in  word2
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
            echo "Invalid input"
            ;;
    esac
done

if [[ -z "$input_file" || -z "$output_file" || -z "$operation" ]]; then
    echo "Invalid input"
fi

if [[ ! -f "$input_file" ]]; then
    echo "invalid file"
    exit 1
fi

case "$operation" in
    v)
        tr 'a-zA-Z' 'A-Za-z' < "$input_file" > "$output_file"
        ;;
    s)
        if [[ -z "$word1" || -z "$word2" ]]; then
            echo "Invalid format, we need to words after -s"
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
        echo "Invalid input"
        ;;
esac
