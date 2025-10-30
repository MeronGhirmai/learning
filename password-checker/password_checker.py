import math

def entropy(password):
    pool = 0
    # rough charset size estimation
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(not c.isalnum() for c in password): pool += 32
    if pool == 0:
        return 0
    return len(password) * math.log2(pool)

if _name_ == "_main_":
    pwd = input("Password to evaluate: ")
    e = entropy(pwd)
    print(f"Estimated entropy: {e:.2f} bits")
    if e < 40:
        print("Weak")
    elif e < 60:
        print("Moderate")
    else:
        print("Strong")
