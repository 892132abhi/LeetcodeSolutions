class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=strs[0]
        for i in strs[1:]:
            while not i.startswith(res):
                res = res[:-1]
                if res=="":
                    return ""
        return res