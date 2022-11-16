0x07. Networking basics #0
OSI Model
What it is
How many layers it has
How it is organized
What is a LAN
Typical usage
Typical geographical size
What is a WAN
Typical usage
Typical geographical size
What is the Internet
What is an IP address
What are the 2 types of IP address
What is localhost
What is a subnet
Why IPv6 was created
TCP/UDP
What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
What is the main difference between TCP and UDP
What is a port
Memorize SSH, HTTP and HTTPS port numbers
What tool/protocol is often used to check if a device is connected to a network

General
Allowed editors: vi, vim, emacs
All your Bash script files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass shellcheck without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

TASKS
0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.
It is organized from the lowest level to the highest level:
The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
In this project we will mainly focus on:

The Transport layer and especially TCP/UDP
On the Network layer with IP and ICMP

Questions:

What is the OSI model?

Set of specifications that network hardware manufacturers must respect
The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology
How is the OSI model organized?

Alphabetically
From the lowest to the highest level
Randomly

1. Types of network
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:
What type of network a computer in local is connected to?
Internet
WAN
LAN
What type of network could connect an office in one building to another office in a building a few streets away?
Internet
WAN
LAN
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?
Internet
WAN
LAN

2. MAC and IP address
What is a MAC address?
The name of a network interface
The unique identifier of a network interface
A network interface
What is an IP address?
Is to devices connected to a network what postal address is to houses
The unique identifier of a network interface
Is a number that network devices use to connect to networks

3. UDP and TCP
4. TCP and UDP ports
Write a Bash script that displays listening ports:
That only shows listening sockets
That shows the PID and name of the program to which each socket belongs
5. Is the host on the network
The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.
Write a Bash script that pings an IP address passed as an argument.
Requirements:
Accepts a string as an argument
Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
Ping the IP 5 times
