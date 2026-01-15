class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = s[0:k:1]
        ans = res[::-1]
        result = ans + s[k:]
        return result
