# WHAT YOU ARE BUILDING:
# A recursive function that generates every valid combination of n
# pairs of curly braces {}. Rule 1: if l > r → place }
# Rule 2: if l < n → place { n=2 gives 2, n=3 gives 5 results
# Task 1 - Define paren(s, l, r, p, n): if p == 2*n: print s and return
# Task 2 - Add the close-brace branch: if l > r: s[p] = "}" then recurse
# Task 3 - Add the open-brace branch: if l < n: s[p] = "{" then recurse
# Task 4 - Set up: s = [""] * 2 * n and call paren(s, 0, 0, 0, n)
# Task 5 - Test n=2 (expect {}{} and {{}}) then n=3 (expect 5 results)

def paren(s,l,r,p,n):
    #Base case 1
    if (p == 2*n):
        for ss in s :
            print(ss,end = " ")
        print("\n")
        return
    #Close - base brach
    if (l>r):
        s[p] = "}"
        paren(s,l,r+1,p+1,n)
    # Open - base branch
    if (l<n):
        s[p] = "{"
        paren(s,l+1,r,p+1,n)

n = int(input("enter the number of parentheses: "))
s = [""]* 2 * n
print("\n")
paren(s,0,0,0,n)
