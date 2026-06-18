def onetoten(n):
    # base case to stop the function 
    if n > 10 :
        return
    print(n)
    onetoten(n+1) # recursion calling the function to print 1 to 10

onetoten(1)