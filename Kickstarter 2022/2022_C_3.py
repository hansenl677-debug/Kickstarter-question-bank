N, L = map(int, input().split())
ants = []
# Input every ants and save info: position, direction,number
for i in range(N):
    P, D = map(int, input().split())
    # Start form ant #1 (i + 1)
    ants.append((P, D, i + 1))
# Sort ants by left to right
ants.sort()
order = []
# Get number of each ant
for P, D, id in ants:
    order.append(id)
# Save all drop time and drop direction (0 left, 1 right)
events = []
# Check when ant drops
for P, D, id in ants:
    # Left
    if D == 0:
        events.append((P, 0))
    # Right
    else:
        events.append((L - P, 1))
# Sort drop times
events.sort()
# Most left number
l = 0
# Most right number
r = N - 1
ans = []
i = 0
while i < N:
    # The timing of this batch of events
    cur_time = events[i][0]
    # Save all the numbers that fell at this moment
    cur = []
    # Multiple ants drop
    while i < N and events[i][0] == cur_time:
        # Drop form left
        if events[i][1] == 0:
            cur.append(order[l])
            l += 1
        # Drop form right
        else:
            cur.append(order[r])
            r -= 1
        i += 1
    cur.sort()
    ans.extend(cur)
print(ans)