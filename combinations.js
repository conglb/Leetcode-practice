/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    var mark = Array(n+1).fill(false);
    var res = [];
    var c = [];
    const update = function(){
        "use strict";
        let cc = c.slice(0);
        res.push(cc);
    };
    const attempt = function(i) {
        "use strict";
        for (let j=1; j<=n; j++) {
            if (mark[j] == false && (c.length == 0 || j > c[c.length-1])) {
                mark[j] = true;
                c.push(j);
                if (i == k) {
                    update();
                } else attempt(i+1);
                mark[j] = false;
                c.pop();
            }
        }
    };
    attempt(1);

    return res;
};

console.log(combine(4,2));