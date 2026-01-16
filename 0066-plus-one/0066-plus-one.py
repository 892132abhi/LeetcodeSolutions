class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=""
        for i in digits:
            res+=str(i)
        res2 = list(str(int(res)+1))
        fin = [int(i) for i in res2]
        return fin