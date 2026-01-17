class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        val = [str(n) for n in num]
        val2 = list(str(int("".join(val))+k))
        val3 = [int(n) for n in val2]
        return val3
        