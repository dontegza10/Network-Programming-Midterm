
import socket
import time

# ==========================================
# PYTHON TCP PORT SCANNER
# Authorized targets only
# ==========================================

AUTHORIZED_TARGETS = {
    "localhost",
    "127.0.0.1",
    "scanme.nmap.org"
}

TIMEOUT = 3.0
SCAN_DELAY = 0.05


def validate_target(target):
    """Validate the authorized scanning target."""

    if target not in AUTHORIZED_TARGETS:
        raise ValueError(
            "Unauthorized target. Use localhost, "
            "127.0.0.1 or scanme.nmap.org."
        )


def validate_ports(start_port, end_port):
    """Validate the port range."""

    if not (1 <= start_port <= 65535):
        raise ValueError("Starting port must be between 1 and 65535.")

    if not (1 <= end_port <= 65535):
        raise ValueError("Ending port must be between 1 and 65535.")

    if start_port > end_port:
        raise ValueError("Starting port cannot exceed ending port.")


def scan_port(target_ip, port):
    """Identify open, closed and filtered TCP ports."""

    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(TIMEOUT)
            sock.connect((target_ip, port))

            return "OPEN"

    except OSError as error:

        # Windows error 10061 means connection refused.
        win_error = getattr(error, "winerror", None)

        if (
            isinstance(error, ConnectionRefusedError)
            or win_error == 10061
            or error.errno == 10061
        ):
            return "CLOSED"

        # Connection timeout means the port may be filtered.
        if (
            isinstance(error, socket.timeout)
            or win_error == 10060
        ):
            return "FILTERED (TIMEOUT)"

        return f"ERROR ({error})"


def start_scanner():
    """Execute the port scanning process."""

    print("=" * 55)
    print("             PYTHON TCP PORT SCANNER")
    print("=" * 55)

    try:
        target = input(
            "Enter target (localhost/127.0.0.1/scanme.nmap.org): "
        ).strip().lower()

        validate_target(target)

        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        validate_ports(start_port, end_port)

        # Resolve hostname to an IP address.
        try:
            target_ip = socket.gethostbyname(target)

        except socket.gaierror:
            print("\nNetwork error: Unable to resolve hostname.")
            return

        print(f"\nTarget: {target}")
        print(f"Resolved IP: {target_ip}")

        print(
            f"Scanning ports {start_port} to {end_port}..."
        )

        print("-" * 55)

        open_ports = []
        closed_ports = []
        filtered_ports = []
        error_ports = []

        start_time = time.perf_counter()

        # Scan every port in the selected range.
        for port in range(start_port, end_port + 1):

            status = scan_port(target_ip, port)

            print(f"Port {port}: {status}")

            if status == "OPEN":
                open_ports.append(port)

            elif status == "CLOSED":
                closed_ports.append(port)

            elif status.startswith("FILTERED"):
                filtered_ports.append(port)

            else:
                error_ports.append(port)

            # Apply a short delay between attempts.
            if port < end_port:
                time.sleep(SCAN_DELAY)

        elapsed_time = time.perf_counter() - start_time

        # Display the scanning summary.
        print("\n" + "=" * 55)
        print("                  SCAN SUMMARY")
        print("=" * 55)

        print(f"Target: {target}")
        print(f"Total ports scanned: {end_port - start_port + 1}")
        print(f"Open ports: {open_ports}")
        print(f"Closed ports: {len(closed_ports)}")
        print(f"Filtered ports: {len(filtered_ports)}")
        print(f"Other errors: {len(error_ports)}")
        print(f"Time taken: {elapsed_time:.2f} seconds")

        print("=" * 55)

    except ValueError as error:
        print(f"\nInput error: {error}")

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")

    except OSError as error:
        print(f"\nSystem error: {error}")


if __name__ == "__main__":
    start_scanner()
