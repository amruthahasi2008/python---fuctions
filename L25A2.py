def fact(n):
    # when n is 1
    if n == 1 :
        return 1
    else:
        # factorial of n = n * n-1 * n-2 * ... * 1
        return n * fact(n-1)
    
n = int(input("enter the number"))
if n < 0 :
    print("There is no factorial for negative numbers.")
elif n == 0 :
    print("The factorial for 0 is 1")
else:
    print("The factorial for",n,"is",fact(n))