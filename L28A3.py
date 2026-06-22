n = int(input("enter the number"))
def checkpowerof4(n):
    if n <= 0:
        return False
    if n == 1 :
        return True
    if n % 4 == 0:
        return checkpowerof4(n//4)
    return False

if (checkpowerof4(n)):
    print("power of 4")
else:
    print("not a power of 4")