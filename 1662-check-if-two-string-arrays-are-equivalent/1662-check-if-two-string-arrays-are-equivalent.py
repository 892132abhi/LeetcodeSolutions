class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        f = "".join(word1)
        s = "".join(word2)
        if f==s:
            return True
        else:
            return False