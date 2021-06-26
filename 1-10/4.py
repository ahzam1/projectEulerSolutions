# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPal(n):
    #helper function to check for palindromic number
    s= str(n)
    for i in range(len(s)//2):
        if(s[i] == s[-1-i]):
            continue
        else:
            return False
    return True

largest =0
first = False
for x in range(999,101,-1):
    for y in range(999,101,-1):
        if(isPal(x*y) and largest < x*y):
            largest = x*y
            
            first= True

print(largest)