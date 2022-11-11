0x05. Processes and signal

General
What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored

Tasks
0. What is my PID
Write a Bash script that displays its own PID.
1. List your processes
Write a Bash script that displays a list of currently running processes.
2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
4. To infinity and beyond
Write a Bash script that displays To infinity and beyond indefinitely.
5. Don't stop me now!
We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
Write a Bash script that stops 4-to_infinity_and_beyond process.
6. Stop me if you can
Write a Bash script that stops 4-to_infinity_and_beyond process.
7. Highlander
Write a Bash script that displays:
To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.
8. Beheaded process
Write a Bash script that kills the process 7-highlander.
I started 7-highlander in Terminal #0 and then run 8-beheaded_process in terminal #1 and we can see that the 7-highlander has been killed.
9. Process and PID file
Write a Bash script that:
Creates the file /var/run/myscript.pid containing its PID
Displays To infinity and beyond indefinitely
Displays I hate the kill command when receiving a SIGTERM signal
Displays Y U no love me?! when receiving a SIGINT signal
Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
10. Manage my process
Read:
&
init.d
Daemon
Positional parameters
Write a manage_my_process Bash script that:
Indefinitely writes I am alive! to the file /tmp/my_process
In between every I am alive! message, the program should pause for 2 seconds
Write Bash (init) script 101-manage_my_process that manages manage_my_process.
Requirements:

When passing the argument start:
Starts manage_my_process
Creates a file containing its PID in /var/run/my_process.pid
Displays manage_my_process started
When passing the argument stop:
Stops manage_my_process
Deletes the file /var/run/my_process.pid
Displays manage_my_process stopped
When passing the argument restart
Stops manage_my_process
Deletes the file /var/run/my_process.pid
Starts manage_my_process
Creates a file containing its PID in /var/run/my_process.pid
Displays manage_my_process restarted
Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed

11. Zombie
Read what a zombie process is.

Write a C program that creates 5 zombie processes.

Requirements:

For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
When your code is done creating the parent process and the zombies

In Terminal #0, I start by compiling 102-zombie.c and executing zombie which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing Z+.*<defunct> which catches zombie process
