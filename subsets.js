/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    var n = nums.length;
    var mark = Array(n).fill(0);
    var res = []
    var update = function() {
        let s = [];
        for (let i=0; i<n; i++) 
        if (mark[i] === 0){
            s.push(nums[i]);
        }
        res.push(s);
    }
    var attempt = function(i) {
        for (let j=1; j>=0; j--) {
            mark[i] = j;
            if ( i === n-1 ) {
                update();
            }else attempt(i+1);
        }
    }

    attempt(0);
    
    return res
};