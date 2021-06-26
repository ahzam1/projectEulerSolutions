# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

s = 600851475143
d=2
ret = []

#attempting trial division, not optimal

while(s!=1):
    if(s%d == 0):
        ret.append(d)
        s=s/d
    else:
        d+=1
print(ret)