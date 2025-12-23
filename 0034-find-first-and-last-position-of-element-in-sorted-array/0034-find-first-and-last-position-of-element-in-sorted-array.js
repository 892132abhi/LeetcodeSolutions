/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let f = nums.indexOf(target)
    let l =nums.lastIndexOf(target)
   return [f,l]
};