class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = s.split(" ")
        ans = res[:k]
        res2 = " ".join(ans)
        return res2