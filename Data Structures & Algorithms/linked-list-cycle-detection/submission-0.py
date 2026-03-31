# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        stack = []

        temp = head

        while (temp):
            if temp.val not in stack:
                stack.append(temp.val)
            else:
                return True
            temp = temp.next
        
        return False