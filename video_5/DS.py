# swappimg two variable in python
# using third variable
# z = 0
# x = int(input("enter the value of x"))
# y = int(input("enter the value of y"))
# z = x
# x = y
# y = z
# print("x", x)
# print("y", y)

# without using third varibale
# x = int(input("enter the value of x"))
# y = int(input("enter the value of y"))
# x, y = y, x
# print("x", x)
# print("y", y)

# arrays in python

# from array import array
# numbers = array("i", [1, 2, 3])
# print(numbers)
# numbers.remove(2)
# print(numbers)
# print(numbers[0])

# unpacking operator
# numbers = [1, 2, 3]
# print(*numbers)


# values = list(range(5))
# print(*values)
# output:-0 1 2 3 4

# unpack two list together
# first = [1, 2]
# second = [3]
# values = [*first, *second]
# print(*values)

# unpack two  dict
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combine = {**first, **second, "z": 1}
# print( combine)

# write a program for most repeated character in an senten
from pprint import pprint
sentence = "Nidhi"
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
# pprint(char_freq, width=1)
freq_sorted = sorted(
    char_freq.items(),
    key=lambda kv: kv[1],
    reverse=True
)
print(freq_sorted[0])
