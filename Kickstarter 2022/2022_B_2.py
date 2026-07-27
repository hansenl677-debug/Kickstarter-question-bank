A = int(input())
result = 0
i = 1
# The divisors always come in pairs such as 6 = 2 x 3.
# So we can just check half of them
while i * i <= A:
    # Checking the small part
    if A % i == 0:
        # Check palindrome
        if str(i) == str(i)[::-1]:
            result += 1
        # Checking the big part against i
        j = A // i
        # Check palindrome
        if j != i and str(j) == str(j)[::-1]:
            result += 1
    i += 1
print(result)
