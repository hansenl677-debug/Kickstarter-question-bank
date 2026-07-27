N = int(input())
list = []
n = 0
# Split every digit of integer
for i in range(len(str(N)) + 1):
    split = 10 ** i
    # Record left and right of splitted integer
    L = N // split
    R = N % split
    # Insert and test every numbers 0 to 9
    for j in range(0,10):
        # Insert new number and test if it divisible by 9, if yes add it in a list
        n = L * (10 ** (i + 1)) + j * (10 ** i) + R
        if n % 9 == 0:
            list.append(n)
# Take the smallest number in the list
print(min(list))