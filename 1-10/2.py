# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

nums = [1,2]
r =0
while(nums[-1] < 4000000):
    n = nums[-1] + nums[-2]
    nums.append(n)
    if(n%2==0):
        r+= n
# +2 is to make up for the initial 2 in the list.
print(r+2)