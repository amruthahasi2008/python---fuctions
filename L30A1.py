#Keyboard map

keypad = {
    "2":['a','b','c'],
    "3":['d','e','f'],
    "4":['g','h','i'],
    "5":['j','k','l'],
    "6":['m','n','o'],
    "7":['p','q','r','s'],
    "8":['t','u','v'],
    "9":['w','x','y','z']
}
# Part 2
def combination(digits,current):
    if len(digits) == 0:
        print(current)
        return
    # Part 3
    first_digit = digits[0]
    remaining = digits[1:]

    for l in keypad[first_digit]:
        combination(remaining,current+l)

# Part 4
num = input ("enter the number")
print("All combinations:")
combination(num,"")

# Part 5
count = 1
for d in num:
    count = count * len[keypad[d]]
print("Total combinations : ",count)