class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in accounts:
            a = 0
            for j in i:
                a+=j
            if a>res:
                res = a
        return res