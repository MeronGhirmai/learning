#!/usr/bin/env python3
import socket

def scan_host(target):
    print(f"Scanning {target} from port 20 to 1024 ...")
    for port in range(20, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.25)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN]  Port {port}")
        except Exception as e:
            pass
        finally:
            s.close()

if _name_ == "_main_":
    host = input("Target host or IP: ").strip()
    scan_host(host)
