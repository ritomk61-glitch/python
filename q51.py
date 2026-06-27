name = input("enter your name here:")
vow = ['a','e','i','o','u']
count=0
for che in name:
    for ch in vow:
        if che == ch:
            count+=1
        
print(count)
