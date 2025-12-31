/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let res = [...new Set(nums)]
    return res.length!==nums.length?true:false
};