from scapy.all import sniff
import json
from .logger import log_blocked_packet

# Load configuration file
with open('firewall/config.json') as f:
    config = json.load(f)

def packet_filter(packet):
    if packet.haslayer("IP"):
        ip = packet["IP"].src
        dport = packet["IP"].dport if hasattr(packet["IP"], 'dport') else None

        # Check for blocked IPs or ports
        if ip in config["blocked_ips"] or dport in config["blocked_ports"]:
            log_blocked_packet(packet)
            print(f"Blocked: {packet.summary()}")

def run_firewall():
    print("Firewall is now monitoring traffic...")
    sniff(prn=packet_filter, store=0)
