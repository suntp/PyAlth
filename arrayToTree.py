# -*- coding: utf-8 -*-

#Definition of TreeNode: 
class TreeNode: 
    def __init__(self, val): 
        self.val = val 
        self.left, self.right = None, None 

class Solution:  
    def sortedArrayToBST(self, A):  
        if len(A) == 0:  
            return None  
        left, right = 0, len(A) - 1  
        return self.helper(A, left, right)  
          
          
    def helper(self, A, left, right):  
        if left <= right:  
            mid = (left + right) // 2  
            root = TreeNode(A[mid])  
            root.left = self.helper(A, left, mid - 1)  
            root.right = self.helper(A, mid + 1, right)  
        else:  
            return None  
        return root  

    # print tree
    def PrintTree(self, tn):
        print tn.val
        if(tn.left):
            self.PrintTree(tn.left)
        if(tn.right):
            self.PrintTree(tn.right)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = Solution()
tn = s.sortedArrayToBST(a)
s.PrintTree(tn)