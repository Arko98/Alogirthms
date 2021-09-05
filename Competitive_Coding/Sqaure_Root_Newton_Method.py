# Fast Sqaure Root by Newton Method

'''
Newton's Method for Fast Square Root
n  = iterations
y = 1/2*x
for iterations:
    y = 1/2*(y + x/y)
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        iterations = 25
        y = 0.5 * x
        for i in range(iterations):
            y = 0.5 * (y + x/y)
        return int(y)