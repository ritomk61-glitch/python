#!Write a Python program to concatenate two lists and then perform element-wise multiplication of the resulting list by 3.


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]


# combined_list = list1 + list2

# for element in combined_list:

#  result = [element * 3 ]


# print("Concatenated list:", combined_list)
# print("After element-wise multiplication by 3:", result)


# k={1,3,True,4.4,"hello"}
# # k={"hello","slide",True,1,88,55}
# # k.add("ritom")
# # k.update([3,4],[6,7],["hi","messi"],("shard","messi1"),[1,2,9,8],["ritom"+"kumar"])
# k.remove(1)
# print(k)

# set1={22,555,66,777,888}
# set2={33,22,555}

# # u=set1.union(set2)
# # i=set1.intersection(set2)

# # i= set1 | set2

# i=set1.difference(set2)

# # i=set1 & set2 
# print(i)

#!17-02-26

# squares = {x:x+5 for x in range(8)}

# new=squares.copy()

# new[3]=5
# new_alias=squares

# new_alias[1]=4
# print(new)
# print(squares)

#?list comprehension

# squares = [x*x for x in range(9)]
# print(squares)

# odd = {x:x*x for x in range(6) if x%2!=0}
# print(odd)

# print(1 in odd)
# print(3 not in odd)

#!dictunary

my_dict = {
    "name": "Ritom",
    "age": 21,
    "city": "Delhi",
    "course": "CSE",
    "language": "Python"
}

# print("name is:",my_dict.get("name"))

# print("keys are:",my_dict.keys())

# print("values:",my_dict.values())

# print("pop",my_dict.pop("age"))

# print("popitems:",my_dict.popitem())

# print("all dic:",my_dict.items())
# my_dict.update({"name":"priya","bbari": "bangladesh"})
# print("update:",my_dict)

# list = [1,3,4,6,7,8,9,34]
# # list.pop(1)
# list.remove(3)
# print(list)

tup =(1,4)


print(tup[1])

