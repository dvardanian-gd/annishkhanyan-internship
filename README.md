# Bandit Tasks

## Level 0

Just used the given port to SSH connect.
![Image not found](screenshots/b00.png)

## Level 0 -> Level 1

Just used the cat command to get the password.
![Image not found](screenshots/b0.png)

## Level 1 -> Level 2

Used ls command to list the files and used ./ to cat the file because it starts with -.
![Image not found](screenshots/b1.png)

## Level 2 -> Level 3

Same here, but the file name contains spaces, so we enclose the whole name in quotes ("filename with spaces") and then use ./.
![Image not found](screenshots/b2.png)

## Level 3 -> Level 4

To see hidden files, we use the -a flag with ls.
![Image not found](screenshots/b3.png)

## Level 4 -> Level 5

We use the file command to check the type of the file and then get the password.
![Image not found](screenshots/b4.png)

## Level 5 -> Level 6

We use find, then specify the directory where we want to search, use the flag -type f to mention the file type, then -size 1033c to match the size, and finally get the password.
![Image not found](screenshots/b5.png)

## Level 6 -> Level 7

We use find again, also specifying the user and group. Since we get many errors, we use 2>/dev/null to suppress them.
![Image not found](screenshots/b6.png)

## Level 7 -> Level 8

We use grep to find the strings containing “millionth.”
![Image not found](screenshots/b7.png)

## Level 8 -> Level 9

Using sort | uniq -u, we print only the strings that appear once.
![Image not found](screenshots/b8.png)

## Level 9 -> Level 10

We use the ls command with the -h flag to print human-readable file sizes.
![Image not found](screenshots/b9.png)

## Level 10 -> Level 11

We use base64 -d to decode.
![Image not found](screenshots/b10.png)

## Level 11 -> Level 12

We use tr to translate ASCII values to the ones mentioned, shifted by 13. On the expressions we specify which letters to change.
![Image not found](screenshots/b11.png)

## Level 12 -> Level 13

We check the type of the file, move it to a file with the corresponding suffix, and decode each step according to the instructions until the password.
![Image not found](screenshots/b12.12.png)
![Image not found](screenshots/b12.1.png)
![Image not found](screenshots/b12.png)

## Level 13 -> Level 14

We use the key in the mentioned directory to connect to the server.
![Image not found](screenshots/b13.png)

## Level 14 -> Level 15

We directly send the password using echo "password" | nc -N localhost 3000. Here, nc connects to the local server on port 3000. -N closes the connection after sending the input so the server gives the next password.
![Image not found](screenshots/b14.png)

## Level 15 -> Level 16

We open an SSL connection on the mentioned port using openssl, paste the password and get the password for the next level.
![Image not found](screenshots/b15.png)

## Level 16 -> Level 17

We open an SSL connection using the -quiet option to avoid   extra debug info. We save the key in a temporary file, edit it to remove redundant parts  and establish a connection using the key file, specifying the port explicitly if required.
![Image not found](screenshots/b16.png)
![Image not found](screenshots/b16.1.png)
![Image not found](screenshots/b16.12.png)
![Image not found](screenshots/b16.123.png)
![Image not found](screenshots/b16.1234.png)

## Level 17 -> Level 18

We use diff to compare two files and find the line that changed which is the password of 18.
![Image not found](screenshots/b17.png)
![Image not found](screenshots/b18.png)

# SadServers Task

## Task 1

We use ps -e | grep py to list all processes containing "py", got their PIDs and killed the process.
![Image not found](screenshots/task1.png)
![Image not found](screenshots/task11.png)

## Task 13

We go to the mentioned directory, use grep -r to search recursively for files containing secret while ignoring permission errors find the line with the secret, then save the secret to the mentioned file.
![Image not found](screenshots/task2.png)
![Image not found](screenshots/task22.png)
![Image not found](screenshots/completed.png)
