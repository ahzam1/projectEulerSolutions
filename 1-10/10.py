# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#instantly can see that this problem is similar to problem #7

sum=2
i =3

def checkDiv(num):
    r = num
    for i in range(2, r):
        if(num%i ==0):
            return False
        r = num/i
    return True


while (i<2000000):
    if(checkDiv(i)):
        
        sum+=i
    i+=2
print(sum)