/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let res = nums.sort((a,b)=>a-b)
    return res[0]
};