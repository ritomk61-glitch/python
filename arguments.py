# print("hello world")
# # !variable length arguments

# # ?postitional variaable length arguments
# def print_values(*args):
#     for arg in args:
#         print(arg)

# print_values("apple", "banana", "cherry")

# # ? keyword variable length arguments
# def print_key_values(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_key_values(name="Alice", age=30, city="New York")


# ?keyword arguments

# def print_info(name,age):
#     print(f"name:{name}, age:{age}")

# print_info("ritom",44)
# print_info("pias",44)



# !default argumetns

# def print_info(name,age=33):
#     print(f"name:{name},age:{age}")

# print_info("ritom")
# print_info("ritom",55)

#* *args and **kwargs

# *argus tupels

# def info(*args):
#     return max(args)


# print(info(1,2,9))
# print(info(6,10))


# !**kwargs dictionary

# def print_info(**kwargs):
#     for k , v in kwargs.items():
#         print(f"{k}:{v}")

# print_info(name="ritom",age=44)



