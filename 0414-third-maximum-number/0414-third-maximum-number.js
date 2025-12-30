/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let num2 = nums.sort((a,b)=>b-a)
    let num3 = [...new Set(num2)]
    return num3.length>=3?num3[2]:num2[0]
};