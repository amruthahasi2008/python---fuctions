def ind(n,num):
    # Base Case
    if (n < 1 or n > num):
        return
    # print in decreasing order
    print(n)
    ind(n-1,num)
    # print in increasing order
    print(n)
n = int(input("Enter any number n :"))
ind(n,n)