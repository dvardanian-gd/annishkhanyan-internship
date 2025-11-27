#!/bin/bash

read -r -p "Input a number: " n  # get the number from the user

# validate input
if [[ -z "$n" || ! "$n" =~ ^[0-9]+$ ]]; then
    echo "Please input a non-negative integer" >&2
    exit 1
fi

fib() {
    local n=$1
    if [ "$n" -eq 0 ]; then
        echo 0
    elif [ "$n" -eq 1 ]; then
        echo 1
    else
        local a
        a=0
        local b
        b=1
        local i
        for ((i = 2; i <= n; i++)); do
            local temp=$((a + b))
            a=$b
            b=$temp
        done
        echo "$b"
    fi
}

echo "The fibonacci number is $(fib "$n")"
