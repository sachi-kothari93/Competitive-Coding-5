# 234. Palindrome Linked List

# TC : O(n) where n is the number of nodes in the linked list. We traverse the list three times: once to find the middle, once to reverse the second half, and once to compare.
# SC :  O(1) as we only use a constant amount of extra space regardless of input size.
# Did this code successfully run on Leetcode : Yes

# Approach :
# Find the middle point: Use the fast and slow pointer technique where the fast pointer moves twice as fast as the slow pointer. When the fast pointer reaches the end, the slow pointer will be at the middle of the list.
# Reverse the second half: Once we've found the middle, reverse the linked list from the middle to the end. This is done using the iterative linked list reversal algorithm with three pointers (previous, current, and next).
# Compare halves: After reversing the second half, we can compare the first half with the reversed second half by traversing both simultaneously. If all corresponding nodes have matching values, then the linked list is a palindrome.


from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: empty list or single node list is always a palindrome
        if not head or not head.next:
            return True
            
        # Step 1: Find the middle of the linked list using slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
            
        # Step 3: Compare the first half with the reversed second half
        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
            
        return True