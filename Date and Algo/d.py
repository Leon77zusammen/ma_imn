class Solution:
    def replaceSpace(self,s):
        res = []
        for a in s:
            if a == ' ': res.append("%20")
            else: res.append(a)
        return "".join(res) 
