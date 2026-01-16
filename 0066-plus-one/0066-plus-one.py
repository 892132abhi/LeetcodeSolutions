class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        val = [str(n) for n in digits]
        val2 = list(str(int("".join(val))+1))
        val3 = [int(n) for n in val2]
        return val3
        