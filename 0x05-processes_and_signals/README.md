# 0x05. Processes and signals

## Learning Objectives
  - What is a PID
  - What is a process
  - How to find a process’ PID
  - How to kill a process
  - What is a signal
  - What are the 2 signals that cannot be ignored

## Tasks
### 0-what-is-my-pid
a Bash script that displays its own PID

### 1-list_your_processes
a Bash script that displays a list of currently running processes

### 2-show_your_bash_pid
a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process

### 3-show_your_bash_pid_made_easy
a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash

### 4-to_infinity_and_beyond
a Bash script that displays `To infinity and beyond` indefinitely

### 5-dont_stop_me_now
a Bash script that stops 4-to_infinity_and_beyond process

### 6-stop_me_if_you_can
a Bash script that stops 4-to_infinity_and_beyond process

### 7-highlander, 67-stop_me_if_you_can
Write a Bash script that displays:
  - `To infinity and beyond` indefinitely
  - With a `sleep 2` in between each iteration
  - `I am invincible!!!` when receiving a `SIGTERM` signal

Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond one`

### 8-beheaded_process
a Bash script that kills the process `7-highlander`
