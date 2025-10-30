# example recon commands (install tools separately)
# find subdomains (example only)
subfinder -d example.com -o subdomains.txt

# nmap scan top ports on discovered host
nmap -sV -Pn -p- -T4 target.example.com -oN nmap_results.txt
