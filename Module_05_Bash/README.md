# Module 05 — Bash

Short exercises and scripts for Module 05 (Bash) of the internship. This module contains small scripts that demonstrate common shell scripting tasks: arithmetic and option parsing, file/text processing, simple algorithms, and system reporting.

## Contents

- scripts in repository:
  - task1.sh — interactive Fibonacci calculator  
    ![task1 screenshot](task1.png)
  - task2.sh — simple command-line calculator with option parsing and optional debug output  
    ![task2 screenshot](task2.png)
  - task3.sh — FizzBuzz (1..100)  
    ![task3 screenshot](task3.png)
  - task4.sh — Caesar cipher  
    ![task4 screenshot](task4.png)
  - task5.sh — text utilities: view, replace, reverse, lower, upper  
    ![task5 screenshot](task5.png)
  - task6.sh — generate a small system report (writes report.txt)  
    ![task6 screenshot](task6.png)

## Script summaries and usage examples

### task1.sh
- Interactive: prompts for a non-negative integer and prints the Fibonacci number.  
  ![task1 output](task1.png)

### task2.sh
- Calculator with options:
  - `-o` operator: `+`, `-`, `*`, `%`
  - `-n` one or more numbers (put numbers after `-n`, parser collects until next flag)
  - `-d` debug mode: prints User, Script, Operation, Numbers  
- Example:
  ```bash
  ./task2.sh -o + -n 3 5 7 -d
