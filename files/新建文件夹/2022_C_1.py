N = input()
# Check if N length at least 7 or not
if len(N) < 7:
    N += "qW&8Aab"
# Check if N has uppercase letters
if not any(i.isupper() for i in N):
    N += "A"
# Check if N has lowercase letters
if not any(i.islower() for i in N):
    N += "b"
# Check if N has numbers
if not any(i.isdigit() for i in N):
    N += "1"
# Check if N has special characters
if not any(i in ["&", "@", "#", "*"] for i in N):
    N += "#"
print(N)