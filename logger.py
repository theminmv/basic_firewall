import datetime

def log_blocked_packet(packet):
    with open("firewall.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - BLOCKED: {packet.summary()}\n")
