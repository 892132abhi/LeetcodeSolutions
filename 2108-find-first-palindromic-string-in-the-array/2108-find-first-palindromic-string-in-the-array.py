class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            res = i[::-1]
            if res==i:
                return i
            
        return ""
             