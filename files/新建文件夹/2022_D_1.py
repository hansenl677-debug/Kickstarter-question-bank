import statistics
N = int(input())
M = int(input())
A = list(map(int, input().split()))
# The largest possible value is that group top M - 1 largest numbers as a category one by one
# Then let remained N - (M - 1) numbers as a single category
# e.g. N = 5, M = 3, A = [1,2,3,4,5], the the largest value is: [5], [4], [3,2,1]
A.sort()
# Calculate the top M-1 numbers median, which is themselves
result = sum(A[N - M + 1:])
# Calculate the median remained N - (M - 1) numbers
result += statistics.median(A[:N - M + 1])
print(result)