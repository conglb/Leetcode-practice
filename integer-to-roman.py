class Solution:
    def make(self,i,v,x):
        global num
        global value
        digit = int(num / value[i])
        res = ''
        if digit == 9:
            res = i + x
            num -= value[x] - value[i]
        elif digit >= 5:
            res = v
            num -= value[v]
            digit -= 5
            while digit > 0:
                res += i
                num -= value[i]
                digit -= 1
        elif digit == 4:
            res = i + v
            num -= - value[i] + value[v]
        else:
            while digit > 0:
                res += i
                num -= value[i]
                digit -= 1
        print(num)
        return res
    def intToRoman(self, n):
        """
        :type num: int
        :rtype: str
        """
        global num
        num = n
        global value
        value = {}
        value['I'] = 1
        value['V'] = 5
        value['X'] = 10
        value['L'] = 50
        value['C'] = 100
        value['D'] = 500
        value['M'] = 1000
        value['O'] = 5000
        s = ''
        if n > 1000:
            s += self.make('M','O','O')
        if n > 100:
            s += self.make('C','D','M')
        if n > 10:
            s += self.make('X','L','C')
        if n > 0:
            s += self.make('I','V','X')
        return s

if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1994))

