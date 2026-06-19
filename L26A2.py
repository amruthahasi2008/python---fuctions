def tailrec(n,num):
    #Base case
    if n > num:
        return
    #Print the current value of n
    print(n)
    # Recursive call
    tailrec(n+1,num)
n = int(input("Enter the n to print 1 to n"))
num = int(input("enter the input to print until n to num"))

tailrec(n,num)


