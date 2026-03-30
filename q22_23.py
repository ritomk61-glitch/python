# print("hello world")

# ?Write a recursive function to generate the first n terms of the Fibonacci sequence

# def fib(n):
#    if n <=1:
#       return n
#    else:
#       return fib(n-1) + fib(n-2)
   
# n = int(input("enter a number:"))
# for i in range(n):
#     print(fib(i))

# *Using map() and lambda expression write a program to convert the following list of temperatures to Fahrenheit. Celsius=[34.56,23.67,45.67,67,34]

# c = [34.56,23.67,45.67,67,34]

# f = list(map(lambda x:1.8*x+32,c))

# print(f)

# def ctof(c): 
#   return 1.8*c+32
# c = [34.56,23.67,45.67,67,34]
# f = list(map(lambda x:ctof(x),c))
# print(f)



# &Write a program to calculate simple interest. Suppose the customer is a senior citizen. He is being offered 12% rate of interest: for all other customers ROI is 10%. 3. Define an anonymous function (lambda function) that squares a give number. Use the lambda function to square the numbers 1 to 5 and print the results

# ? first

# amount = float(input("Enter your amout:"))

# time = float(input("Enter your time:"))

# age = int(input("Enter your age:"))

# def si(amount , time , age):
#   if age>=60:
#     r=12
#   else:
#     r=10

#   return (amount*r*time)/100

# print(si(amount,time,age))

# !second

   
# sq = lambda x:x**2

# for i in range(1,6):
#     print(sq(i))

# x=10
# def add ():
#    global x
#    x+=1
#    print(x)
# add()
# print(x)

# def f():
#     x=10
#     def f1():
#         print(x)
#     f1()
#     print(x)


#  write all in one program global,nonlocal and local variable

x=10
def f():
    x=20
    def f1():
        nonlocal x
        x+=1
        print(x)
    f1()
    print(x)

