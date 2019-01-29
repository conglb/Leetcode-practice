/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var ans = -2147483699;
    var a = [];
    let s = 0;
    a.push(0);
    for (let i=0; i<nums.length; i++) {
        s += nums[i];
        a.push(s);
    }
    var divide = function(l, r) {
        if (l === r) {
            return {'min': a[l], 'max': a[l]};
        }
        let m = Math.floor((l + r) / 2);
        let left = divide(l, m);
        let right = divide(m+1, r);
        ans = Math.max(ans, right['max'] - left['min']);
        //console.log(l.toString() + ' ' + r.toString())
        //console.log(right['max'] - left['min']);
        return {'min': Math.min(left['min'], right['min']), 'max': Math.max(left['max'], right['max'])};
    };
    divide(0,a.length-1);
    return ans;
};