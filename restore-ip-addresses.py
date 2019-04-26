class Solution:
    def restoreIpAddresses(self, s: str, g = 4) -> List[str]:
        "return way to divide s into g groups"        
        if g == 1:
            if len(s) > 1 and s[0] == '0':
                return []
            if int(s) <= 255:
                return [s]
            else:
                return []      
        res = []
        for i in range(len(s)-1):
            st = s[0:i+1]     
            if len(st) > 1 and st[0] == '0':
                continue
            if int(st) > 255:
                break
            else:
                next = self.restoreIpAddresses(s[i+1:len(s)], g-1)
                for instance in next:
                    res.append(st + '.' + instance)
        return res