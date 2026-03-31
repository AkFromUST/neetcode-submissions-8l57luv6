# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # simple idea. Get the total len -> O(n)
        # calculate which node to remove from the start -> O(1)
        # remove that node -> O(n)

        curr = head;
        total = 0

        while (curr != None):
            total += 1
            curr = curr.next

        i = total - n

        if i == 0:
            head = head.next
            return head

        prev = None
        curr = head

        for j in range(i):
            prev = curr
            curr = curr.next

        #remove the curr
        prev.next = curr.next

        return head  