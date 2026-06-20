#Program to sum the list
def atosum(a):
    # checking  the length of the array
    length = len(a)
    # if the length is less than or equal to 1 returning the element
    if length <= 1 :
        return a[0]
    return a[0]+atosum(a[1:])
a = [1,2,3,6]
print("the sum is",atosum(a))