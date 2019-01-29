class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0/self.myPow(x, -n)
        else:
            tmp = self.myPow(x, int(n/2))
            if n % 2 == 1:
                return tmp * tmp * x
            else:
                return tmp * tmp