import os

def block_ip(ip):
    os.system(f"netsh advfirewall firewall add rule name='Block {ip}' dir=in action=block remoteip={ip}")
    print(f"Blocked IP: {ip}")
