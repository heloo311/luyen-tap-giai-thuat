# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxPathSum(self, root):
    res = float('-inf')
    stack = [(root, False)]

    while stack:
      node, visited = stack.pop()

      if node:
        if visited:
          left = right = 0
          if node.left:
            left = node.left.val
          if node.right:
            right = node.right.val
          res = max(res, node.val + left + right)
        else:
          stack.append((node.right, False))
          stack.append((node.left, False))
          stack.append((node, True))

    return res
a=TreeNode(2,None,None)
b=TreeNode(3,None,None)
root = TreeNode(1,a,b)



a=Solution()
print(a.maxPathSum(root))