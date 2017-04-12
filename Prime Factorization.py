#Author : Mohammed Nafiuzzaman
"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumSquare(numberstart, numbers):
    mylist = list(range(numberstart,numbers+1))
    final = 0
    for i in mylist:
        final += i ** 2
    return final
def squareSum(numberstart, numbers):
    mylist = list(range(numberstart,numbers+1))
    final = 0
    for i in mylist:
        final += i;
    final2 = final **2
    return final2


def main():
    i = int(input("First natural number?"))
    j = int(input("second natural number? "))
    final = squareSum(i,j)-sumSquare(i,j)
    print(final)

main()