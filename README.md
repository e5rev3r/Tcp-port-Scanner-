# TCP Port Scanner 🛡️

A compact and efficient TCP port scanner written in Python, designed for scanning individual IPs or entire /24 subnets. Ideal for network enumeration, penetration testing practice, and automation scripts.

## 📌 Project Highlights

- Scan a single host or an entire subnet (e.g., 192.168.1.0/24)
- Customizable port range scanning
- Minimal dependencies (uses only Python standard libraries)
- Fast execution with socket timeout tuning
- Clear and structured output for open ports

## 🔧 How It Works

This script uses Python's built-in `socket` module to perform TCP connect scans across a range of ports. It reports open ports in real time and gracefully handles timeouts and unreachable hosts.

## 💻 Usage

```bash
# Scan a single host
python3 portscanner.py <IP> <start_port> <end_port>

# Example:
python3 portscanner.py 192.168.1.10 1 100

# Scan a full /24 subnet
python3 portscanner.py <network_prefix> <start_port> <end_port> -n

# Example:
python3 portscanner.py 192.168.1 20 80 -n
```
## ⚠️ Disclaimer
Use this tool only on systems and networks you own or have explicit permission to scan. Unauthorized scanning is prohibited.
