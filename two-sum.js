/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    ans = []
    for (let i = 0; i < nums.length; i++) {
        for (let j =0; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                ans.push(i)
                ans.push(j)
                return ans
            }
        }
    }
};
console.log(twoSum([1,2,3,4], 7));