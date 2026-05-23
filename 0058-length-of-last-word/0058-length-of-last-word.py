class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s.split()
        l = len(s1[len(s1)-1])
        return l