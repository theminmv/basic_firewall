# Basic Python Firewall

A basic Python-based packet filtering firewall using `scapy`.

## Features
- Block network packets based on IP or port.
- Logs blocked packets to `firewall.log`.
- Configurable via JSON file.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/simple_firewall.git
    cd simple_firewall
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Important:** Run with root/admin privileges to allow packet sniffing:
    ```bash
    sudo python3 run.py
    ```

## Configuration

Edit `firewall/config.json` to add IPs or ports you want to block.

Example:

```json
{
  "blocked_ports": [80, 23],
  "blocked_ips": ["192.168.1.100"]
}
