0x0D-web_stack_debugging_0

task
0. Give me a page!
In this first debugging project, you will need to get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it.
starting my Docker container, I curl the port 8080 mapped to the Docker container port 80, it does not return a page but an error message. Note that you might also get the error message curl: (52) Empty reply from server.
