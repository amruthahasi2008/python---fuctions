#Program to check if an array is sorted or not 
def checksorted(a):
    #calculating the length of the array
    length = len(a)
    #if array length is 0 or 1 we donot need to check again
    if length == 0 or length == 1:
        return True
    #returns true if both conditions are true
    return a[0] <= a[1] and checksorted(a[1:])
a =[1,2,4,5,6,4,5]
#Displaying the result
if checksorted(a):
    print(" the array is sorted")
else :
    print("the array is not sorted")
