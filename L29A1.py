#climbing stairs
# A recursive function that counts every distict path uo a stair
# when you can take 1 or two steps at a time 
# Task 1:Define ways(stairs):base case 1 if stairs< 0 return 0
# Task 2:Add base case 2 if stairs == 0 return 1
# Task 3: add two steps = 0 if stairs >= 2 two = ways(stairs-2)
# Task 4:add one step  = ways(stairs -1) and return two + one
# Task 5: add input to enter number of stairs and test with n = 4

def ways(stairs):
    #base case 1
    if stairs < 0 :
        return 0
    # base case 2
    if stairs == 0:
        return 1
    # if stairs are more then 2 to take 2 stairs at a time 
    two = 0
    if stairs >= 2:
        two = ways(stairs-2)
    # one stair
    one = ways(stairs-1)
    # total distict path 
    return two+one
stairs = int(input("enter the number of stairs?"))
print("the number of distinct ways for ", stairs,"is :",ways(stairs))