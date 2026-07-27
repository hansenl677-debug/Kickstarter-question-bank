# Only for Test Set 1 (K = 1) ...
# If there is thief, then the guests that is not thief must be innocent 
# => Their statements are true 
# => A guest is a thief <=> No one but himself says "he didn't steal".
# => If A_i ≠ B，then A_j ≠ B. 
# => Count how many times each person is pointed at by others.
N, M = list(map(int, input().split()))
guests = [0] * (N + 1)
for i in range(N):
    x, y = map(int, input().split())
    if x != y:
        guests[y] += 1
result = 0
for j in range(1, N + 1):
    if guests[i] > 0:
        result += 1
print(result)