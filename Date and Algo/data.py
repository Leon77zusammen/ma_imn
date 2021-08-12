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
         return "".join(res) # no " ", right ""

#right answer
class Solution:
    def replaceSpace(self,s):
        res = []
        for c in s:
             if c == " ": res.append("%20")
             else : res.append(c)
        return "".join(res)

# 02.08 offer06 print linked list from end to start
class Solution: 
    def reversePrint(self, head): #digui Recursion
        return self.reversePrint(head.next) + [head.val] if head else []

class Solution:
    def reversePrint(self, head): #stack
        stack = []
        while head:
             stack.append(head.val)
             head = head.next
        return stack[::-1] #inverted list

# 02.08 offer09 2 stacks --> queue
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()    