class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res=[]
        for i in arr:
            if arr.count(i)==i and i not in res:
                res.append(i)

        if len(res)>0:
            return max(res)
        return -1