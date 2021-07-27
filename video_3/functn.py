# def greet(first_name, last_name):
#     print(f"Hi {first_name}")
#     print(f"Welcome aboard {last_name}")


# greet("Nidhi", "gupta")

# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("mosh")
# print(message)
# # open to write content into a file
# file = open("content.txt", "w")
# file.write(message)

# def increment(number, by=1):
#     return number + by


# # print(increment(number=3, by=3))
# print(increment(2, 5))


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total = total * number
#     return total


# print("start")
# print(multiply(1, 2, 3))


# print(multiply(2, 3, 4, 5, 6))


# def save_user(**user):
#     print(user)
#     print(user["name"])


# save_user(id=1, name="nidhi", age=22)
# message = "a"


# def greet(name):
#     message = "b"


# greet("nidhi")
# print(message)


def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    if(input % 3 == 0):
        return "Fizz"
    if(input % 5 == 0):
        return "Buzz"

    return input


print(fizz_buzz(15))
