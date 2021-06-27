# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                   a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def checkPyTrip(a,b,c):
    return (a**2 + b**2) == c**2

# #ranges appear weird, but are adjusted for minimizing iterations. considering above constraints
# for a in range(1,332):
#     for b in range(2,(1000-a)//2):
#         for c in range(3,1000-b-a):
#             if (checkPyTrip(a,b,c) and a+b+c==1000):
#                 print(a,b,c)
#                 exit()

#attempt at using euclid's formula for generating pythagorean triplets
pairs = []
for m in range(1,500):
    for n in range(1,500):
        if (((2*m)*(m+n)) == 1000 and m > n):
            pairs.append((m,n))

(finalM , finalN) = pairs[0]

a = finalM**2 - finalN**2
b = 2*finalM*finalN
c= finalM**2 + finalN**2
print(a*b*c)
