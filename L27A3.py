#Program to find out the maximum value in an array using recursion
def maximum(a):
    #checking the length of the array
    length = len(a)
    # returning the element if the length is less than 1
    if length <= 1:
        return a[0]
    # returning the max value in the array and recalling the function until we get max value
    else:
        return max(a[0],maximum(a[1:]))
#List    
a = [1,2,3,4,87,35,997,8,54,23,765,987]
#Displaying the result
print("The max value in the array is",maximum(a))