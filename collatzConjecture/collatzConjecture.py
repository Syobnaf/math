import sys
import math

if __name__ == '__main__':

    def testIfPowerOfTwo(n):
        power = 1
        while True:
            if n == power:
                return True
            elif n < power:
                return False
            power = power * 2

    def printCollatzStats(n):
        originalN = n
        seriesStr = "\n"
        stepCount = 0
        stepsTillPowerOfTwo = 0
        while n != 1:
            if not stepsTillPowerOfTwo and testIfPowerOfTwo(n):
                stepsTillPowerOfTwo = stepCount
            seriesStr += str(n) + ","
            if n % 2 == 0:
                # Even => divide by 2
                n = n // 2
            else:
                # Odd => multiple by 3 then add 1
                n = (3 * n) + 1
            stepCount += 1
        print(seriesStr + str(n))
        print(str(originalN) + " took " + str(stepCount) + " steps")
        print(str(stepsTillPowerOfTwo) + " steps until it was a power of 2")

    n = int(input("How many collatz series would you like to be computed: "))
    for i in range(1, n + 1):
        printCollatzStats(i)
