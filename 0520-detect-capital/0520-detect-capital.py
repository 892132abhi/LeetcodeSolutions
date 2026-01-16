class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        res = word[0].upper()+word[1:].lower()
        if word == word.upper() or word ==word.lower() or word ==res:
            return True
        else:
            return False