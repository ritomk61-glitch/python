# print("hello world")

# ?Write a recursive function to generate the first n terms of the Fibonacci sequence

# rec = lambda n:n if n<=1 else rec(n-1)+rec(n-2)

# n = int(input("enter any number:"))

# for i in range(n):
#     print(rec(i))

# *Using map() and lambda expression write a program to convert the following list of temperatures to Fahrenheit. Celsius=[34.56,23.67,45.67,67,34]

c = [34.56,23.67,45.67,67,34]

f = list(map(lambda x:1.8*x+32,c))

print(f)

# &Write a program to calculate simple interest. Suppose the customer is a senior citizen. He is being offered 12% rate of interest: for all other customers ROI is 10%. 3. Define an anonymous function (lambda function) that squares a give number. Use the lambda function to square the numbers 1 to 5 and print the results

# ? first

# amount = float(input("Enter your amout:"))

# time = float(input("Enter your time:"))

# age = int(input("Enter your age:"))

# if age>=60:
#     r=12
# else:
#     r=10

# si = (amount*r*time)/100

# print(si)

# !second

# sq = lambda x:x**2

# for i in range(1,6):
#     print(sq(i))