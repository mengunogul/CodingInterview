class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1/x
        
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return self.myPow(x, n-1) * x