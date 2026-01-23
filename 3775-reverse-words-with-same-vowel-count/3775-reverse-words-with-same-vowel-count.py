class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        b = s.split(" ")
        a = "aeiou"
        count=0
        res = []
        res.append(b[0])
        for i in b[0]:
            if i in a:
                count+=1
        d = b[1:]
        for i in d:
            c = 0
            for j in i:
                if j in a:
                    c+=1 
            if c==count:
                res.append(i[::-1])
            else:
                res.append(i)
        ans = " ".join(res)
        return ans