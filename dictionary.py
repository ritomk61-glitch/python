 
# *dictionary are unordered items.items contains key and value pair..dictionaries are mutable.



dic = {
    "name":"ritom kumar",
    "age":44,
    "school":"shrda university"
}

# print(dic.get("name"))
# print(dic.get("age"))
# print(dic.get("school"))

# print(dic.items())
# print(dic.keys())
# print(dic.values())

# print(dic["name"])


#! updation

# dic["age"]=88
# print(dic["age"])


# !add item

# dic["address"] = "bangladesh"
# print(dic.items())

# !remove a particular item(key,values), returns , its valur

# print(dic.pop("age"))
# print(dic)

# !remove an arbitary item returs (key , values)..its remove the las items of a dictionary

# print(dic.popitem())
# print(dic)

# !python dictionary comprehension 

# sum = {a:a+a for a in range(10)}
# print(sum)

# !dictionary membership

# print( "age" in dic) #true

# print("priya " not in dic) #true

# print("motki" in dic) #false

# !iteratin through a dictionary

# num = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

# num = { 1 ,2 ,3 , 4 , 5}

# for i in num:
#     print(num[i])

# &question

# n=21
# number = {}

# for i in range(1 , n):
#     number[i] = i*i
# print(number)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True


prime_dict = {n: "Prime" for n in range(1, 10)}



print(prime_dict)



