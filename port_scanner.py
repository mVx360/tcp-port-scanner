import socket

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def validate_port(port):
    return 0 <= port <= 65535

def validate_input (host, start_port, end_port=None):
    if not validate_ip(host):
        print("Invalid IP address: {}.\n".format(host))
        return False
    if not validate_port(start_port):
        print("Invalid port number: {}.\n".format(start_port))
        return False
    if end_port is not None:
        if not validate_port(end_port):
            print("Invalid port number: {}.\n".format(end_port))
            return False
        if start_port > end_port:
            print("Starting port can't be greater than ending port.\n")
            return False
    return True

def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0


def scan_range(host, start_port, end_port):
    for p in range(start_port, end_port+1):
        if scan(host, p):
            print("Port {} is open".format(p))
        else:
            print("Port {} is closed".format(p))

def view_open_ports_in_range(host, start_port, end_port):
    open_ports = []
    print("Checking for open ports...")
    for p in range(start_port, end_port+1):
        if scan(host, p):
            open_ports.append(p)
    if len(open_ports) > 0:
        print("Open ports: {}".format(open_ports))
    else:
        print("No open ports found between ports {} and {}".format(start_port, end_port))

def main():
    choice = 0
    while choice != 'q':
        choice = input("Select action: \n[1] scan a single port \n[2] scan a range of ports \n[3] view open ports in a range \n[q] exit \ninput: ")

        if choice == '1':
            host = input("Enter host address (IPv4): ")
            try:
                port = int(input("Enter port number: "))
            except ValueError:
                print("Port must be a number.\n")
                continue
            if not validate_input(host, port):
                continue

            if scan(host, port):
                print("Port {} is open".format(port))
            else:
                print("Port {} is closed".format(port))
            print("\n")

        elif choice == '2':
            host = input("Enter host address (IPv4): ")
            try:
                p1 = int(input("Enter starting port number: "))
                p2 = int(input("Enter ending port number: "))
            except ValueError:
                print("Ports must be numbers.\n")
                continue
            if not validate_input(host, p1, p2):
                continue

            scan_range(host, p1, p2)
            print("\n")

        elif choice == '3':
            host = input("Enter host address (IPv4): ")
            try:
                p1 = int(input("Enter starting port number: "))
                p2 = int(input("Enter ending port number: "))
            except ValueError:
                print("Ports must be numbers.\n")
                continue
            if not validate_input(host, p1, p2):
                continue

            view_open_ports_in_range(host, p1, p2)
            print("\n")

        elif choice == 'q':
            print("Closing program...")

        else:
            print("Please enter a valid choice.")
            print("\n")


if __name__ == '__main__':
    main()