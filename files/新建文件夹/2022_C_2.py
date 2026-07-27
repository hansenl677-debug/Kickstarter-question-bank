N = int(input())
X = int(input())
Y = int(input())
# Total sum (T) of all numbers 1 to N, Alan's numbers' sum (A)
sum = N * (N + 1) // 2
# For T / (T - A) = X / Y 
# <=> A * Y = (T − A) * X 
# <=> A * (X + Y) = T * X
# <=> A = (T * X) / (X + Y)
if (sum * X) % (X + Y) != 0:
    print("IMPOSSIBLE")
else:
    alan_sum = (sum * X) // (X + Y)
    result = []
    # Start form the largest number and test if it satisfied requirement
    for i in reversed(range(1, N + 1)):
        if i <= alan_sum:
            result.append(i)
            alan_sum -= i
    print("POSSIBLE")
    print(len(result))
    print(result)