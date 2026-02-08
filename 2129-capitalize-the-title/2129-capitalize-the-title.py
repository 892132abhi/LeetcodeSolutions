class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        res=[]
        t1 = title.lower().split(" ")
        for i in t1:
            if len(i)>2:
                res.append(i.title())
            else:
                res.append(i)
        return " ".join(res)