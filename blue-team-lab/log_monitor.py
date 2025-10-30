# simple failed login detector for an auth log
from collections import Counter

def parse_auth_log(path="/var/log/auth.log"):
    ips = []
    with open(path, errors='ignore') as f:
        for line in f:
            if "Failed password" in line or "authentication failure" in line:
                parts = line.split()
                # naive IP extraction
                for p in parts:
                    if p.count('.') == 3:
                        ips.append(p)
    return Counter(ips)

if _name_ == "_main_":
    counts = parse_auth_log("sample_auth.log")  # use a sample file
    for ip, c in counts.most_common(10):
        print(ip, c)
