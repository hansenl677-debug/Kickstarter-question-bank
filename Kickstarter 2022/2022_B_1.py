import math
R = int(input())
A = int(input())
B = int(input())
pi = math.pi
area = 0
# Calculate until radius is 0
while R > 0:
    # Add area (include original R)
    area += R ** 2 * pi
    # Times raidus of previous one by A
    R *= A
    # Add area
    area += R ** 2 * pi
    # Divides radius of previous one by B
    R //= B 
print(area)