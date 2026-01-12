/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s =s.toLowerCase()
    let res = s.replaceAll(/[^a-zA-Z0-9]/g,"")
    let ans = res.split("").reverse().join("")
    return res===ans?true:false
};