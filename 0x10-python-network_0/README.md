# 0x10. Python - Network #0
## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application 
## Requirements

### General

- Allowed editors: vi, vim, emacs
- A README.md file is mandatory at the root of the project folder.
- All Bash scripts should be exactly 3 lines long.
- All files should end with a new line.
- All files must be executable.
- The first line of all Bash files should be `#!/bin/bash`.
- The second line of all Bash scripts should be a comment explaining what the script is doing.
- All curl commands must have the option `-s` (silent mode).
- All Python files should use `#!/usr/bin/python3`.
- Code should use pycodestyle (version 2.8.*).
- All modules, classes, and functions should be documented.

## Tasks

### 0. cURL body size

- Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
- The size must be displayed in bytes.
- You have to use curl.
- Test your script in the provided sandbox, using the web server running on port 5000.

```bash
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$

