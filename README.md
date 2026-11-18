Project : Network Programming Midterm Project

 In this tutorial, we will explore how to use Python socket programming to build a TCP port scanner.

Student Email: t.edafe9089@student.nu.edu  
Programming Language: Python  
Operating System: Windows  
Version Control: Git and GitHub is the course.Version Control: Git and GitHub is the course.

---

 1. Project Introduction

This is a project of basic network programming in Python. It is composed of two practical examples: one example is a client-server communication application based on the TCP socket protocol and the other is a TCP port scanner to identify the open and close ports of a targeted machine that is authorised.

The project covers the fundamental concepts of network applications in creating links, transferring data, handling errors, and probing network services.

 2. Project Objectives

The main objectives are to:

- Develop a TCP client-server application.
- Use Python sockets to establish a connection between a client and server.
- Add error handling and connections.
- Develop a TCP port scanner.
- Locate open and closed ports on a range of ports.
- Address invalid inputs and network issues.
- Demonstrate responsible and ethical network scanning.
Use Git & GitHub for version control and project submission.

 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
Network communication | Socket module | |
Enforcing rules that trigger a program to run or test |
| Git | Version control |
Hosting source code on GitHub |

 The first part discusses socket programming.Part One is about socket programming.

The first part of the project is implemented with the help of communication between server and client by TCP sockets.

 Server (`server.py`)

The server is waiting for clients to connect on:

- Host: `127.0.0.1`
- Port: `5000`

It is able to accept connecting remote users, receive messages, present received messages and send out messages. It is also responsible for handling connection closure and interruption.

 Client (`client.py`)

The client accesses the server with its IP address and port number. Users can send and get responses.

Error handling is in place to ensure that things don't go wrong if the server is not available or there is an issue with connecting to it.

 How to Run

Open PowerShell and go to the project directory:

```powershell
cd Socket_Connection
```

Start the server:

```powershell
python server.py
```

Open another PowerShell window, navigate to the same directory and run:

```powershell
python client.py
```

The client can then exchange messages with the server.

 Select Part Two: TCP Port Scanner.Click Part Two: TCP Port Scanner.

The second part is a python port scanner with the socket module that is implemented.

The scanner scans the port range and classifies the results as:

- OPEN: A connection to the port was successful.
- CLOSED: The connection was refused.
An attempt was made to connect to an already closed filter.
- ERROR: Another socket or network error occurred.

 Key Features

- Target validation.
- Port range validation.
- Hostname resolution.
- Identification of open and closed ports.
- Timeout handling.
- Network error handling.
- Scan duration measurement.
- Summary of the results of the scans.

 Authorised Targets

The scanner allows the following targets:

- `localhost`
- `127.0.0.1`
- `scanme.nmap.org`

The project is limited to these authorized targets for the scan.

 How to Run

Launch PowerShell and go to the location of the scanner:

```powershell
cd Port_Scanner
```

Run:

```powershell
python port_scanner.py
```

On being prompted, enter the authorised target to be followed, followed by the starting port and ending port.

 6. Testing and Results

Local and external targets used to test programs.

 Socket Programming Tests

Testing of the client-server application was conducted on the following:

- Successful server startup.
- Client connection.
- Message exchange.
- Client disconnection.
Could not connect when the server was not available.

 Port Scanner Tests

Various port ranges and input conditions were used for the scanner's testing.

Localhost performance tests:

Test | Port Range | Ports Scanned | Open Ports | Time |
|---|---|---:|---|---:|
| Test A | 5000–5005 | 6 | 5000 | 10.47 seconds |
| Test B | 5000–5020 | 21 | 5000 | 41.83 seconds |

The reason for the port 5000 being open was due to the socket server existing. All other ports tested were closed.

Other tests included for common ports, custom ports, invalid port numbers, unauthorised target, hostname resolution failures and the authorised external scanning target.

A timeout is an event reported as filtered, it is not an event that implies a port is filtered by a firewall.

 7. Security and ethical issues

Port scanning can uncover the information on network services and can have impact on the system if done irresponsibly.

This project only scanned the targets that were explicitly allowed. The scanner also checks user input and applies unnecessary network delays/timeout to help reduce network traffic.

Scanning should be done only on systems where permission has been obtained.

 8. Project Structure

```text
Network_Programming_Midterm/
│
├── Socket_Connection/
│   ├── server.py
│   └── client.py
│
├── Port_Scanner/
│   └── port_scanner.py
│
└── .gitignore
```

 9. Conclusion

This project provided practical experience in Python network programming, TCP communication, socket management, error handling and basic network reconnaissance.

It was also a showcase for testing and responsible network activity and version control using Git and GitHub.

The two applications serve as a starting point for more in-depth exploration of network programming and cybersecurity topics.