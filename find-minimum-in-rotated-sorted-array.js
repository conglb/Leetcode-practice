/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let ascending = true;
    for (let i=1; i<nums.length; i++) 
        if (nums[i] < nums[i-1]){
            ascending = false;
        }
    if (ascending == true) {
        return nums[0];
    }
    l = 0;
    r = nums.length-1;
    while (l < r-1) {
        m = Math.floor((l + r) / 2);
        console.log(m)
        if (nums[m] >= nums[l]) {
            l = m;
        } else {
            r = m;
        }
    }
    return nums[l] < nums[r]? nums[l]: nums[r];
};

