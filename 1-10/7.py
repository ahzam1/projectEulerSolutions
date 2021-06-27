# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
primes = [2]
i =3

def checkDiv(num):
    for n in primes:
      if(num%n ==0):
        return False
    return True
while (len(primes)!=10001):
    if(checkDiv(i)):
        primes.append(i)
    i+=2
print(primes[10000])