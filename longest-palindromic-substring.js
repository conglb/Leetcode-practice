/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
      n = s.length;
      var f = []
      for (let i = 0; i < n; i++) {
            f[i] = []
            for (let j = 0; j < n; j++) {
                  if (i >= j) {
                        f[i].push(true);
                  } else {
                        f[i].push(false);
                  }
            }
      }
      l = 0;
      r = 0;
      for (let i = n-1; i >= 0; i--) {
            for (let j = i+1; j< n; j++) {
                  if (s[i] == s[j]) {
                        f[i][j] = f[i+1][j-1];
                  } else {
                        f[i][j] = false;
                  }
                  if (f[i][j] == true && j-i > r-l){
                        l = i;
                        r = j;
                  }
            }
      }
      res = '';
      for (let i = l; i <= r; i++) res += s[i];
      return res;
};

