A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = int(input())
def best(list):
    n = len(list)
    # Calculate the sum of the first i elements of a list
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + list[i]
    # Calculate the sum of the last i elements of a list
    suf = [0] * (n + 1)
    for i in range(n):
        suf[i + 1] = suf[i] + list[n - 1 - i]
    # Test and choose the way that best score can reach combining the first (t) and last (t-l) elements
    max_i = [0] * (n + 1)
    for t in range(n + 1):
        best_score = 0
        for l in range(t + 1):
            r = t - l
            if l <= n and r <= n:
                best_score = max(best_score, pre[l] + suf[r])
        max_i[t] = best_score
    return max_i
# Assign the function to both A and B
FA = best(A)
FB = best(B)
result = 0
# Calculate the best score
for x in range(K + 1):
    if x <= len(A) and K - x <= len(B):
        result = max(result, FA[x] + FB[K - x])
print(result)