class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        n1 = sorted(target)
        n2 = sorted(arr)
        if n1==n2:
            return True
        else:
            return False