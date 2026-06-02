#? multiple number for a table

# for i in range(1,11):
#     # print("the multiple table of 5 is :")
#     print( f"3 x {i} = ",3*i)


vow = ('a' , 'e' , 'i' , 'o' , 'u' )


name = input("enter the name:")
count = 0
for ch in name:
    if ch in vow:
      count+=1

print("your vowel number in your word :",count)