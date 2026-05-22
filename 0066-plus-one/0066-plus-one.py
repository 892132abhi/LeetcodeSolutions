class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        res=[]
        for i in digits:
            s+=str(i)
        s1 = str(int(s)+1)
        for i in s1:
            res.append(int(i))
        return res
        