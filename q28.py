class ValueTooLarge(Exception):
    pass
class ValueTooSmall(Exception):
    pass

number = 50

while True:
    try:

        num = int(input("enter your number:"))
 
        if(num>number):
           raise ValueTooLarge("value too large")
        elif(num<number):
           raise ValueTooSmall("value too small")
    
        else:
          print("correct number!Game over")

    except ValueTooLarge as e:
     print(e)

    except ValueTooSmall as e:
        print(e)