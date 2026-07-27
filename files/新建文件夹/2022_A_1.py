# The sentence that user needs to type
I = "HelloWorld"
print(I)
# The sentence that user typed
P = input()
i = 0
str = ""
# If letter of P same with I, record that letter of P in to str
# If not, jumps over the next letter of I then compare again
# Keep doing until all letters in I finish comparison
for letter in P:
    if i < len(I) and I[i] == letter:
        str += letter
        i += 1
# If the str same with I, count the # of excess letters of P
# If not, means user mis-typed some letters
if str == I:
    print(len(P) - len(I))
else:
    print("Impossible")