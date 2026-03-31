# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        # brute force is -> Store all the val in a set and if a repeated val, return True

        temp = head
        val = set()

        while (temp != None):
            if id(temp) not in val:
                val.add(id(temp))
            else:
                return True
            temp = temp.next

        return False