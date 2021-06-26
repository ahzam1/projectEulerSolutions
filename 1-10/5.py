# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 20
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, 20]
def check(i):
    for x in nums:
        if(i%x==0):
            continue
        else:
            return False
    return True
while(True):
    
    if(check(i)):
        print(i)
        break
    else: 
        i+=20