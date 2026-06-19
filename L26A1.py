def linear(n):
    if n == 0 :
        return
    print(n,end = " ")
    linear(n-1)
print("Linear recursion")
linear(5)
print()

def tail(n):
    if n == 0:
        return
    print(n,end = " ")
    tail(n-1)
print("Tail recursion")
tail(5)
print()

def head(n):
    if n == 0:
        return
    head(n-1)
    print(n,end = " ")
print("Head recursion")
head(5)
print()

def ind(n):
    if n == 0 :
        return
    print(n,end = " ")
    ind(n-1)
    print(n,end = " ")
print("increasing decreasing")
ind(4)
print()

def tree(n):
    if n == 0:
        return
    print(n , end = " ")
    tree(n-1)
    tree(n-1)
print("Tree Recursion")
tree(3)
print()
print("Level calls: doubles everytime")
