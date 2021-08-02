# class TreeNode:
#     def __init__(self,x):
#         self.val = x
#         self.left = None
#         self.right = None

# n1 = TreeNode(3)
# n2 = TreeNode(4)
# n3 = TreeNode(5)
# n4 = TreeNode(1)
# n5 = TreeNode(2)

# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5


# 27.07 review offer05 replace space
class Solution:
     def replaceSpace(self, s):
         res = []
         for c in s:
             if c == " ": res.append["%20"] #pay attention to [] and ()
             else : res.append[c]
         return "".join(res)

#right answer
class Solution:
    def replaceSpace(self,s):
         res = []
         for c in s:
             if c == " ": res.append("%20")
             else : res.append(c)
         return "".join(res)

