#!/bin/bash

operation="" # initializing variables
numbers=()
debug_state=false

while getopts "o:n:d" opt; do # checking the options
  case $opt in
    o) operation="$OPTARG" ;;
    n) 
      ((OPTIND--))  # step back to include the first number after -n
      while [[ $OPTIND -le $# && ${!OPTIND} != -* ]]; do # loop undtill the end of line and the next flag
        numbers+=("${!OPTIND}") # expand the variables under the opt indices
        ((OPTIND++))
      done ;;
    d) debug_state=true ;;
    *) echo "Invalid input"; exit 1 ;;
  esac
done

if [[ -z "$operation" || ${#numbers[@]} -eq 0 ]]; then # validating the input
    echo "Invalid input"
    exit 1
fi

result="${numbers[0]}" # starting from the first one
for num in "${numbers[@]:1}"; do # doing the operations
    case $operation in
        +) result=$((result + num)) ;;
        -) result=$((result - num)) ;;
        \*) result=$((result * num)) ;;
        %) result=$((result % num)) ;;
        *) echo "Error while performing the operation"; exit 1 ;;
    esac
done 

if $debug_state; then # printing the addiotional information if debug state is true
    echo "User: $USER"
    echo "Script: $0"
    echo "Operation: $operation"
    echo -n "Numbers: "
    printf "%s " "${numbers[@]}"
    echo
fi

echo "Result: $result" 
