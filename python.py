# #1st question

# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))

# sum = num1+num2
# diff = num1 - num2
# prod = num1 * num2
# quot = num1 / num2
# mud = num1 % num2

# print("sum:",sum , "datatype:",type(sum))
# print("diff:",diff , "datatype:",type(diff))
# print("prod:",prod , "datatype:",type(prod))
# print("quot:",quot , "datatype:",type(quot))
# print("mud:",mud , "datatype:",type(mud))


# #experiment 4

# num = int(input("Enter the number:"))


# if(num>0):
#     print("this is positive number.")

# elif(num<0):
#     print("this is negative number.")
# else:
#     print("this is zero.")
# #*experiment 5

# amount = int(input("Enter the amount to withdraw: "))

# notes_2000 = amount / 2000
# amount = amount % 2000

# notes_500 = amount / 500
# amount = amount % 500

# notes_200 = amount / 200
# amount = amount % 200

# notes_100 = amount / 100
# amount = amount % 100

# print("Minimum number of notes required:")
# print("2000 =", notes_2000)
# print("500  =", notes_500)
# print("200  =", notes_200)
# print("100  =", notes_100)


# #*experiment 6

# num=input("Enter the binary number:")

# count_1=num.count('0')
# count_2=num.count('1')

# if count_1 ==  1 or count_2 == 1:
#     print("yes")

# else:
#     print("no")


# !27-01-26
# i = 1
# sum=0

# while( i<=100):
    
#     sum=sum+i
#     i+=1

# print("sum=",sum)
# # *odd number

# for i in range(1,50,2):
#     print(i,end='')

# #*even number

# for i in range(2,51,2):
#      print(i,end='')




#!sum of reciprocal of first 100 natural number

# sum =0
# for i in range(1,101):
#     sum = sum + (1/i)
# print("sum=",sum)

#! tabel of a number

# num = int(input("Enter the number:"))

# # for i in range(1,11):
# #     print(num,"x",i,"=",num*i)

# i=1
# while i<=10:
#     print(num,"x",i, "=",num*i)
#     i+=1

# * check leap year or not

# year = int(input("Enter Year Here:"))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  
#         print("this is leap year")
# else:
#         print("this is not leap year")

# *Write a Python program to print all even numbers between 1 and 100. Also print the total count of even numbers.
# e=0
# for i in range(2, 101,2):
#     print(i, end="")
#     e+=1
# print("Total count of event number:",e)

# *Design a Password Validation System where A user is allowed 3 attempts to enter the correct password


# c_pass="python123"
# attempt=3

# while attempt > 0:
#     password = input("Enter your password:")
#     if(password == c_pass):
#         print("Access Granted")
#         break
#     else:
#         print("Access is not Granted ")
#         attempt-=1

# if attempt == 0:
#     print("Access Denied.")

# str="ritom"
# str1="kumar"


# print("i want t from str:",str[2])

# print("this is slicing:")
#*this is positional argument

# print("{3},{2},{0},{1}".format("megha","virat","messi","ritom")) 

#!this is key-word argument

# print("{d},{a},{c},{b}".format(a="megha",b="virat",c="messi",d="ritom")) 

# #*formating

# print("binary representation of {2} is {0:b}".format(13,44,55))

# print("Exponent representation : {0:e}".format(1566.345))

# print("one third is : {0:e}".format(1/3))

# print("|{:<10}|{:^10} | {:>10}".format('bhalle','papdi','chaat'))

#!change the given string

# s=input("Enter a string:")

# print("lower to upper",s.upper())
# # print("lower to upper",s.lower())


# #!is this little case or not 

# print("is this is lower case?",s.islower())

# #&replace a to @

# print("replace a to @",s.replace('a','@'))


# #!trim the 7 character from the string

# print("here the first character of this string:",s[0:8])

# #?split the i

# print("split:",s.split("i"))


#?

# a="ourhhshjsjhf@@@11122"


# alpa=0
# digit=0
# chatr=0
# if a.isalpha():
#     alpa+=1
# elif a.isdigit():
#     digit+=1
# else:
#     chatr+=1

# print("alpa:",alpa)
# print("digit:",digit)
# print("chatr:",chatr)

#*Write a Python program to concatenate two lists and then perform element-wise multiplication of the resulting list by 3.

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]


# combined_list = list1 + list2

# for element in combined_list:

#  result = [element * 3 ]


# print("Concatenated list:", combined_list)
# print("After element-wise multiplication by 3:", result)

#*You are provided with a list of grocery items purchased by a customer. As shown below. Write python code to print the name of the item and its quantity (occurrences in the list).

# L=["pen","ball","eraser","pen","band","pen","pencil","ball"]
   
# for i in set(L):
#  print(i,":",L.count(i))

#*Given a nested list, extract and print the last element of each inner list using list indexing.

# list=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# for i in list:
#     print("the last element of each inner list:",i[3])

# !13Given a list of tuples representing books with (title, author, publication year), create a Python function that sorts the list based on the publication year in ascending order. Return the sorted list.
# books = [
#     ('Book 1', 'Author A', 1990),
#     ('Book 2', 'Author B', 2005),
#     ('Book 3', 'Author C', 1985)
# ]

# books.sort(key=lambda book: book[2]) #!Lambda হলো small function যা একটা value return করে,

# print(books)



#!Create a Python program that initializes a tuple of tuples, where each inner tuple represents a student with (name, age, grade). Sort the students based on their grades in descending order and return the sorted list.

# students = (
#     ("Ritom", 20, 85),
#     ("Amit", 21, 90),
#     ("Suman", 19, 78)
# )

# sorted_students = sorted(students,key=lambda x:x[2],reverse=True)

# print(sorted_students)

#!You are provided with following data consisting of grocery items and their cost.

# price = [('item1', '17.20'), ('item2', '15.10'), ('item3', '24.5')]


# price.sort(key=lambda x: float(x[1]))


# print("Sorted items by price:", price)


# second_costliest = price[-2]
# print("Second costliest item:", second_costliest[0])

#!Write a python program that takes a string as input and returns a new string where each word is reversed. For example, if the input is "Hello World," the output should be "olleH dlroW."


# text = input("Enter a string: ")

# words = text.split()


# reversed_words = [word[::-1] for word in words]


# result = " ".join(reversed_words)

# print("Output:", result)

#! 17 Write a Python function that takes a list of strings as input and returns a new list containing only the strings with more than five characters. Additionally, reverse the characters in each string.

# def filter_and_reverse(strings):
#     result = []
#     for s in strings:
#         if len(s) > 5:
#             result.append(s[::-1])
#     return result

# new = filter_and_reverse(["hiijskjslkhs", "computer", "python"])
# print(new)

#

#!13
# books = [
#     ("t1", "p1", 300),
#     ("t2", "p2", 250)
# ]

# list1 = []

# for t, p, y in books:
#     list1.append((t, p, y))

# list1.sort()


# list2 = [(t, p, y) for t, p, y in list1]

# print(list2)

#!18 Write a Python program to check the strength of a password entered by the user. Implement conditions to check for the following: Length of at least 8 characters. Presence of both uppercase and lowercase letters. Presence of at least one digit. Presence of at least one special character (!@#$%^&*).

# p=input("enter your pass:")
# upper = False
# lower = False
# digit = False
# special = False
# specialc="!@#$%^&*"


     


# if(len(p)<8):
#     print("enter up to")
# else:
#     if p.isupper():
#        upper=True
#     elif p.lower():
#         lower=True
#     elif p.digit():
#         digit=True
#     elif p in special:
#         special=True
    
#     if upper and lower and digit and special :
#         print("password strong")

#     else:
#         print("password is poor")


#!21 You are given with a list of dictionaries having keys (name, marks). Write a program to filter the name of students on the basis of marks value given by user. Example display names of all the students having marks >95.

student = [
    {"name":"ritom","marks":88},
    {"name":"pappu","marks":99}
]

mar = int (input("enter student mark:"))

for s in student:
    if s["marks"]>mar:
        print(s["name"])
    