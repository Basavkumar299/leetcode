# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()

    def size(self):
        return len(self.stack1)


class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []
        
        ans = []
        queue = Queue()
        queue.push(root)
        
        while queue.size() > 0:
            l = queue.size()
            level_sum = 0
            
            for _ in range(l):
                front = queue.pop()
                level_sum += front.val
                
                if front.left is not None:
                    queue.push(front.left)
                if front.right is not None:
                    queue.push(front.right)
                    
            ans.append(level_sum / l)
            
        return ans
