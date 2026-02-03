class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res=[]
        ans = []
        arr1.sort()
        for i in arr1:
            if i not in arr2:
                res.append(i)
        for a in arr2:
            for b in arr1:
                if a==b:
                    ans.append(b)
        ans.extend(res)
        return ans