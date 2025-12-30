/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    let n = nums.length
    nums=nums.sort((a,b)=>a-b)
    let res = nums[0]*nums[1]*nums[n-1]
    let ans = nums[n-1]*nums[n-2]*nums[n-3]
    return res>ans?res:ans
};