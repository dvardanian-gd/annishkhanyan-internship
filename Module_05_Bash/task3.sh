#!/bin/bash

read -r -p "Input a number: " n  # get the number from the user

# Validate input
if [[ -z "$n" || ! "$n" =~ ^[0-9]+$ ]]; then
    echo "Please input a non-negative integer"
    exit 1
fi

fibonacci() {
    local n=$1
    if [ "$n" -eq 0 ]; then
        echo 0
    elif [ "$n" -eq 1 ]; then
        echo 1
    else
        local a
        a=$(fibonacci $((n - 1)))
        local b
        b=$(fibonacci $((n - 2)))
        echo $((a + b))
    fi
}

echo "The fibonacci number is $(fibonacci "$n")"