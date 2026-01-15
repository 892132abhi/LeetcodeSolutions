class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        res = word[0:index+1:1]
        ans = res[::-1]
        result = ans+word[index+1:]
        return result