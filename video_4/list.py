# list = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + list
# print(combined)

# number = list(range(20))
# print(number)
# chars = list("hello world")
# print(chars)

# operation in list
# letters = ["a", "b", "c", "d"]
# print(letters[0::2])

# numbers = list(range(20))
# print(numbers[::-1])

# list unpacking
# numbers = [1, 2, 3, 4, 5, 6, 7]
# first, second, third, *other = numbers
# print(numbers)

# loop in list
# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     print(index, letter)

# letters = ["a", "b", "c"]
# print(letters)
# # add
# letters.append("d")
# print(letters)
# letters.insert(0, "ele ")
# print(letters)
# letters.pop(0)
# print(letters)
# letters.remove("b")
# print(letters)
# del letters[0:2]
# print(letters)
# letters.clear()
# print(letters)

# letters = ["a", "b", "c"]
# if "c" in letters:
#     print(letters.index("c"))
#     print(letters.count("c"))
# else:
#     print("element not exists")

# sorting
# numbers = [3, 51, 2, 8, 6]
# print(sorted(numbers, reverse=True))
# print(numbers)

# lambda expression
# items = [
#     ("Product1", 10), ("Product2", 9),
#     ("Product3", 12)
# ]

# items.sort(key=lambda item: item[1])
# print(items)

# map
# items = [
#     ("Product1", 10), ("Product2", 9),
#     ("Product3", 12)
# ]
# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)
# prices = map(lambda item: item[1], items)
# print(prices)

# filter
# items = [
#     ("Product1", 10), ("Product2", 9),
#     ("Product3", 12)
# ]
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)
# comprehension
# items = [
#     ("Product1", 10), ("Product2", 9),
#     ("Product3", 12)
# ]

# Zip
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(list(zip(list1, list2)))

# from collections import deque
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# browsing_session.append(4)
# print(browsing_session)
# browsing_session.pop()
# print(browsing_session)
# print(browsing_session)
# browsing_session.pop()
# print(browsing_session)
# if not browsing_session:
#     browsing_session[-1]

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# swapping varibales in [python]
# x = 10
# y = 11
# x, y = y, x
# print("x", x)
# print("y", y)

# from array import array

# sets
# numbers = [1, 2, 3, 1, 1, 1, 2, 3, 4]
# first = set(numbers)
# # print(uniques)
# # second = {1, 4}
# # second.add(5)
# # second.remove(5)
# # print(len(second))
# second = {1, 5}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# print(point)


# values = []
# for x in range(5):
#     values.append(x*2)
# print(values)

# unpacking
# numbers = [1, 2, 3]
# print(*numbers)

# from pprint import pprint
# sentence = "This is a common interview question"
# char_freq = {}
# for char in sentence:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
# print(sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True))
