/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let result = nums.findIndex(num=>num>=target)
    return result!==-1?result:nums.length
};