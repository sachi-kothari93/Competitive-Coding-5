# 110. Balanced Binary Tree

# TC : O(n) where n is the number of nodes in the tree. We visit each node exactly once.
# SC : O(h) where h is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), it could be O(n), but for a balanced tree it would be O(log n).
# Did this code successfully run on Leetcode : Yes

# Approach :
# The approach for solving this height-balanced binary tree problem uses a bottom-up recursive strategy.:
# Bottom-up recursive traversal: Rather than checking balance separately after calculating heights (which would be inefficient), we compute heights and check balance in a single traversal.
# Special return value: We use -2 as a special flag to indicate an unbalanced subtree has been found. This allows us to immediately stop further unnecessary checks once we detect imbalance.
# Height calculation with balance checking: For each node, we:
    # Calculate the height of left and right subtrees
    # Check if either subtree is unbalanced (returned -2)
    # Check if the current node is balanced (height difference ≤ 1)
    # Return either the node's height (if balanced) or -2 (if unbalanced)
# This approach is efficient because:
    # Visit each node exactly once (O(n) time complexity)
    # Don't recalculate heights multiple times
    # Terminate early once we detect an unbalanced subtree
# The efficiency comes from combining the height calculation and balance checking into a single recursive function, eliminating the need for separate traversals that would increase time complexity.


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate height and check balance
        def check_height(node):
            # Base case: empty node has height -1
            if not node:
                return -1
            
            # Get heights of left and right subtrees
            left_height = check_height(node.left)
            # If left subtree is unbalanced, propagate the failure
            if left_height == -2:
                return -2
                
            right_height = check_height(node.right)
            # If right subtree is unbalanced, propagate the failure
            if right_height == -2:
                return -2
                
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                # Return -2 as a flag for unbalanced
                return -2
                
            # Return height of current node
            return max(left_height, right_height) + 1
        
        # Tree is balanced if check_height doesn't return -2
        return check_height(root) != -2