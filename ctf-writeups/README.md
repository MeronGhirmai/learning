# CTF Writeups
Writeups for rooms and challenges from TryHackMe/HackTheBox.

## Example
### Room: Brute It (TryHackMe)
- Tools used: nmap, hydra
- Steps:
  1. nmap -sV to find open ssh
  2. used hydra with a small wordlist
  3. obtained credentials -> escalated to root using sudo misconfig
