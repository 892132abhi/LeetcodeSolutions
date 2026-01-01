/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let res = dividend/divisor
    let a  = 2 ** 31-1
    let b = -(2 ** 31)
    let ans = Math.trunc(res)
    if(ans>a)return a
    if(ans< b)return b
    return ans
    };