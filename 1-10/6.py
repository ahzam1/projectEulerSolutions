# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumofsquares =0 
squareofsum = 0
for i in range(101):
    sumofsquares+= i**2
    squareofsum+= i

squareofsum = squareofsum**2

print(squareofsum - sumofsquares)