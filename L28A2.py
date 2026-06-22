def reversedname(s):
    if len(s) == 1 :
        return s[0]
    else:
        return reversedname(s[1:])+s[0]   
name = input('Enter the name')
print("the flipped name is ",reversedname(name))