#!/usr/bin/python3
import socket
import sys


def scanHost(ip, startPort, endPort):
    print('[*] Scanning host:', ip)
    open_ports = tcp_scan(ip, startPort, endPort)

    if open_ports:
        for port in open_ports:
            print('[+] %s:%d/TCP Open' % (ip, port))
    else:
        print('[-] No open ports found on', ip)


def scanRange(network, startPort, endPort):
    print('[*] Scanning network: %s.0/24' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        open_ports = tcp_scan(ip, startPort, endPort)

        if open_ports:
            print('[+] Host %s:' % ip)
            for port in open_ports:
                print('    - Port %d/TCP Open' % port)


def tcp_scan(ip, startPort, endPort):
    open_ports = []
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = tcp.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            tcp.close()
        except Exception:
            pass
    return open_ports


if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('Usage:')
        print('  ./portscanner.py <IP> <start_port> <end_port>')
        print('  ./portscanner.py <network_prefix> <start_port> <end_port> -n')
        print('\nExamples:')
        print('  ./portscanner.py 192.168.1.10 1 100')
        print('  ./portscanner.py 192.168.1 20 80 -n')
        sys.exit(1)

    target = sys.argv[1]
    startPort = int(sys.argv[2])
    endPort = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(target, startPort, endPort)
    elif len(sys.argv) == 5 and sys.argv[4] == '-n':
        scanRange(target, startPort, endPort)
