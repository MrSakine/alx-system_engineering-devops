# 0x04. Loops, conditions and parsing

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
  - How to create SSH keys
  - What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
  - How to use while, until and for loops
  - How to use if, else, elif and case condition statements
  - How to use the cut command
  - What are files and other comparison operators, and how to use them

### 0-RSA_public_key.pub
#### Create a RSA key pair
Requirements:
  -Share your public key in your answer file 0-RSA_public_key.pub
  - Fill the SSH public key field of your intranet profile with the public key you just generated
  - Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are - - Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
  - If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

### 1-for_best_school
Write a Bash script that displays Best School 10 times

### 2-while_best_school
a Bash script that displays Best School 10 times through while loop

### 3-until_best_school
a Bash script that displays Best School 10 times through untip loop

### 4-if_9_say_hi
a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line

### 5-4_bad_luck_8_is_your_chance
a Bash script that loops from 1 to 10 and:
  - displays bad luck for the 4th loop iteration
  - displays good luck for the 8th loop iteration
  - displays Best School for the other iterations

### 6-superstitious_numbers
a Bash script that displays numbers from 1 to 20 and:
  - displays 4 and then bad luck from China for the 4th loop iteration
  - displays 9 and then bad luck from Japan for the 9th loop iteration
  - displays 17 and then bad luck from Italy for the 17th loop iteration

### 7-clock
a Bash script that displays the time for 12 hours and 59 minutes:
  - display hours from 0 to 12
  - display minutes from 1 to 59

### 8-for_ls
Write a Bash script that displays:
  - The content of the current directory
  - In a list format
  - Where only the part of the name after the first dash is displayed (refer to the example)

### 9-to_file_or_not_to_file
a Bash script that gives you information about the school file

### 10-fizzbuzz
a Bash script that displays numbers from 1 to 100

## 100-read_and_cut
a Bash script that displays the content of the file /etc/passwd.
Your script should only display:
  - username
  - user id
  - Home directory path for the user

### 101-tell_the_story_of_passwd
a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS
Format: The user `USERNAME` is part of the `GROUP_ID` gang, lives in `HOME_DIRECTORY` and rides `COMMAND/SHELL`. `USER ID's` place is protected by the passcode `PASSWORD`, more info about the user here: `USER` `ID` `INFO`

### 102-lets_parse_apache_logs
a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file

### 103-dig_the-data
a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file
Format:
  - OCCURENCE_NUMBER IP HTTP_CODE
