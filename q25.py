class divisible(Exception):
    def __init__(self, massege):
        super().__init__(massege)

def divisiblen(n,d):
    if d == 0:
        raise divisible("error found")
    return n/d
try:
    print("q-1",divisiblen(12,9))
except divisible as e:
    print(e)
try:
    print("q-2",divisiblen(12,0))
except divisible as e:
    print(e)
try:
    print("q-3",divisiblen(12,9))
except divisible as e:
    print(e)




