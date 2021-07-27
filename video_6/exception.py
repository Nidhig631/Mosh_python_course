# numbers = [1, 2]
# print(numbers[3])
# try:
#     with open("exception.py") as file:
#         print("file opened.")

#     age = int(input("age: "))
#     xfactor = 10/age
#     file.close()
# except (ValueError, ZeroDivisionError):
#     print("Please enter valid age")
# else:
#     print("No exceptions were thrown.")

from timeit import timeit

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor =    calculate_xfactor(-1)
if xfactor == None:
  pass
"""

print("first_code", timeit(code2, number=10))
