# print("hello world")

# ? single variabl lambda

# squaree = lambda x:x**2
# print(squaree(2))

# add = lambda x,y:x+y 
# print(add(2,4))

# !recarsion

# def rec(n):
#     if n == 0:
#         return 1
#     else:
#         return n*rec(n-1)
    
# print(rec(int(input("enter a number:"))))

# *lambda is used to define argumetns to higher order function

# &Lambda হলো anonymous function (নাম ছাড়া function)

# * map()
# ?map() use হয় list-এর সব element এর উপর একই operation apply করতে
# L=[1,2,3,4]

# p=list(map(lambda x:x+5,L))
# print(p)

# * filter()
# i=[1,2,3,4,5]

# p=list(filter(lambda x:x%2==0,i))

# print(p)

# # * reduce()
L=[1,2,3,4,5]

fruits = ['apple', 'cherry', 'gauva']

p=list(map(lambda x:x.upper(),fruits))
print(p)

items ={
    "rice":1000,
    "wheat":500,
    "pen":20,
    "vegetables":2000
}
l=(max(items,key=lambda x:items[x]))

print(l)
 









