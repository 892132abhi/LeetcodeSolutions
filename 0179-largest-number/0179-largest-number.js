/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    let res = nums
    res = res.map(String).sort((a,b)=>(b+a)-(a+b)).join("")
    return res[0]==="0"?"0":res
};