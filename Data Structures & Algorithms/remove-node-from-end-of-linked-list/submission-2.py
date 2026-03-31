# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #finding the length of the list
        temp = head
        length = 0
        while (temp):
            temp = temp.next
            length += 1

        print(length)

        curr = head
        prev = None

        for i in range(length - n):
            if (curr.next):
                prev = curr 
                curr = curr.next
        
        #two cases, can be the end of the list or can be the middle
        if (curr.next):
            if (prev):
                prev.next = curr.next
                curr = None
            else:
                head = curr.next
        else:
            if (prev):
                prev.next = None
                curr = None
            else:
                return None
        
        return head
        