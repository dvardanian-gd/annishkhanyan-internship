#!/bin/bash

operation="" # initialize variables
numbers=()
debug_state=false

while getopts "o:n:d" opt; do # parse command-line options
  case $opt in
    o) operation="$OPTARG" ;;
    n) 
      ((OPTIND--))  # step back to include the first number after -n
      while [[ $OPTIND -le $# && ${!OPTIND} != -* ]]; do
        numbers+=("${!OPTIND}") # add number to the list
        ((OPTIND++))
      done ;;
    d) debug_state=true ;;
    *) echo "Invalid input" >&2; exit 1 ;;
  esac
done

# validate required input
if [[ -z "$operation" || ${#numbers[@]} -eq 0 ]]; then
    echo "Invalid input" >&2
    exit 1
fi

result="${numbers[0]}" # start from the first number

# perform the operation
for num in "${numbers[@]:1}"; do
    case $operation in
        +) result=$((result + num)) ;;
        -) result=$((result - num)) ;;
        \*) result=$((result * num)) ;;
        %)
            if [[ $num -eq 0 ]]; then
                echo "Error: division by zero is not permitted" >&2
                exit 1
            fi
            result=$((result % num))
            ;;
        *) echo "Error" >&2; exit 1 ;;
    esac
done 

# debug information
if $debug_state; then
    echo "User: $USER"
    echo "Script: $0"
    echo "Operation: $operation"
    echo -n "Numbers: "
    printf "%s " "${numbers[@]}"
    echo
fi

echo "Result: $result"
