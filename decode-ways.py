class Solution:
    def numDecodings(self, s: str) -> int:
        f = []
        
        if len(s) == 0:
            return 0
        
        def check(s, i):
        	if i == 0:
        		return False
        	if s[i-1] == '0':
        		return False
        	if s[i-1] == '1':
        		return True
        	if s[i-1] != '2':
        		return False
        	if int(s[i]) > 6:
        		return False
        	return True
        
        if s[0] == '0':
        	return 0
        def get(i):
        	if i < 0:
        		return 1
        	else:
        		return f[i]
        for i in range(len(s)):
        	if i == 0:
        		if s[i] != '0':
        			tmp = 1
        		else:
        			tmp = 0 
        	else:
        	    # unfixable case
        	    #if s[i] == 0 and (s[i-1] != '1' or s[i-1] != '2') == '0':
        	    #	return 0 
        	    if s[i] == '0':
        	    	if s[i-1] != '1' and s[i-1] != '2':
        	    		return 0
        	    	else:
        	    		tmp = get(i-2)
        	    else:
        	    	tmp = f[i-1] 
        	    	if check(s,i):
        	    		tmp += f[i-2]
        	f.append(tmp)
        	print(tmp)
        return f[len(s)-1]