# Network Programming Midterm Project

**Project:** Python Socket Programming and TCP Port Scanner

**Student Email:** t.edafe9089@student.nu.edu  
**Programming Language:** Python  
**Operating System:** Windows  
**Version Control:** Git and GitHub

---

## 1. Project Introduction

This project demonstrates basic network programming using Python. It consists of two practical applications: a client-server communication application based on the TCP socket protocol and a TCP port scanner used to identify open and closed ports on authorised targets.

The project covers fundamental networking concepts, including establishing connections, transferring data, handling errors, and identifying available network services.

## 2. Project Objectives

The main objectives are to:

- Develop a TCP client-server application.
- Use Python sockets to establish communication between a client and a server.
- Implement error handling for connection failures and interruptions.
- Develop a TCP port scanner.
- Identify open and closed ports within a specified port range.
- Handle invalid inputs and network errors.
- Demonstrate responsible and ethical network scanning.
- Use Git and GitHub for version control and project submission.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Socket module | TCP network communication and port scanning |
| Git | Version control |
| GitHub | Source code hosting and project submission |
| Windows PowerShell | Running and testing the Python programs |

## 4. Part One: TCP Socket Programming

The first part of the project implements communication between a server and a client using TCP sockets.

### Server (`server.py`)

The server listens for client connections using the following configuration:

- **Host:** `127.0.0.1`
- **Port:** `5000`

The server accepts local client connections, receives messages, displays the messages received, and sends responses to the client. It also handles connection closure and interruptions.

### Client (`client.py`)

The client connects to the server using its IP address and port number. Users can send messages and receive responses from the server.

Error handling is implemented to manage situations where the server is unavailable or a connection cannot be established.

### How to Run

Open PowerShell and navigate to the project directory:

```powershell
cd Socket_Connection
```

Start the server:

```powershell
python server.py
```

Open another PowerShell window, navigate to the same project directory, and run:

```powershell
python client.py
```

The client can then exchange messages with the server. Enter `exit` to disconnect.

## 5. Part Two: TCP Port Scanner

The second part of the project implements a TCP port scanner using Python's socket module.

The scanner checks a specified range of ports and classifies the results as follows:

- **OPEN:** A TCP connection to the port was successful.
- **CLOSED:** The connection was refused, indicating that no service accepted the connection on that port.
- **FILTERED (TIMEOUT):** The connection attempt did not receive a response within the configured timeout period. A timeout alone does not confirm that a firewall is filtering the port.
- **ERROR:** Another socket or network error occurred.

### Key Features

- Target validation.
- Port range validation.
- Hostname resolution.
- Identification of open and closed ports.
- Timeout handling.
- Network error handling.
- Scan duration measurement.
- Summary of scan results.

### Authorised Targets

The scanner permits the following targets:

- `localhost`
- `127.0.0.1`
- `scanme.nmap.org`

The scanner is restricted to these specified targets to promote responsible and authorised testing.

### How to Run

Open PowerShell and navigate to the scanner directory:

```powershell
cd Port_Scanner
```

Run the scanner:

```powershell
python port_scanner.py
```

When prompted, enter an authorised target, followed by the starting and ending port numbers.

## 6. Testing and Results

Both applications were tested under different conditions to evaluate their functionality, error handling, and performance.

### 6.1 Socket Programming Tests

The client-server application was tested for:

- Successful server startup.
- Successful client connection.
- Message exchange between the client and server.
- Client disconnection.
- Connection failure when the server was unavailable.

The tests demonstrated that the client could connect to the server, exchange messages, receive responses, and close the connection successfully.

### 6.2 Port Scanner Tests

Different port ranges, target conditions, and input values were used to evaluate the scanner.

#### Localhost Performance Tests

| Test | Port Range | Ports Scanned | Open Ports | Time Taken |
|---|---|---:|---|---:|
| Test A | 5000–5005 | 6 | 5000 | 10.47 seconds |
| Test B | 5000–5020 | 21 | 5000 | 41.83 seconds |

Port `5000` was detected as open because the project's socket server was running on that port. The other ports in the tested ranges were closed.

#### Other Tests

Additional tests included:

- Common ports: 21–23, 80, and 443.
- Custom port range: 4998–5002.
- Invalid starting and ending port numbers.
- Hostname resolution failure.
- Scanning the authorised external target, `scanme.nmap.org`.
- Scanner behaviour when a port did not respond within the configured timeout.

During the external scan of `scanme.nmap.org` over ports 80–85, port 80 was identified as open, while ports 81–85 returned timeout results.

A timeout indicates that the connection attempt did not receive a response within the configured period. It does not independently establish that a firewall is blocking the port.

## 7. Security and Ethical Considerations

Port scanning can reveal information about network services and may affect systems when performed irresponsibly.

This project restricts scanning to the specified authorised targets. It also validates user input and uses connection timeouts and a short delay between scan attempts to manage network activity.

Port scanning should only be performed on systems for which permission has been obtained. Unauthorised scanning may violate organisational policies or applicable laws.

## 8. Project Structure

The project is organised into the following directories and files:

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
├── README.md
│
└── .gitignore
```

## 9. Conclusion

This project provided practical experience in Python network programming, TCP communication, socket management, error handling, and basic network reconnaissance.

It also demonstrated the importance of testing, responsible network activity, and version control using Git and GitHub.

The two applications provide a foundation for further exploration of network programming and cybersecurity concepts.
