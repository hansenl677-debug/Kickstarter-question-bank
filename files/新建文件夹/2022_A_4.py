A = int(input())
B = int(input())
sum = 0
product = 1
list = []
result = 0
# Test every integer between A and B
for n in range(min(A,B), max(A,B) + 1):
    i = n
    # Take each digit of each number
    while n > 0:
        digit = n % 10
        n //= 10
        list.append(digit)
    # Calculate the sum and product of digits
    for m in list:
        sum += m
        product *= m
    # Test if product divides sum
    if product % sum == 0:
        result += 1
    # Reset the sum, product and digits 
    sum = 0
    product = 1
    list.clear()
print(result)