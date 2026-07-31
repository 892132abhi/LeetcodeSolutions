class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        w = list(s)
        right = len(s)-1
        v = "aeiouAEIOU"
        while left  < right:
            while left<right and v.find(w[left])==-1:
                left+=1
            while left<right and v.find(w[right])==-1:
                right-=1
            w[left],w[right] = w[right],w[left]
            left+=1
            right-=1
        return "".join(w)