# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # A bit messy solution but uses O(1) space

        #finding the len of head

        temp = head
        count = 0

        while temp != None:
            temp = temp.next
            count += 1
        
        # this is where the partition occurs. So now nums[:part] is left and nums[part:] is right side
        part = count // 2

        #now we need to reverse the linked list starting from part
        curr = head

        for i in range(part-1):
            print("moving to right side: ", curr.val)
            curr = curr.next

        temp = curr.next
        curr.next = None
        curr = temp
        
        #now temp starts from the partitioning. Lets reverse it
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #lets print both sides to be safe

        # #printing left
        # print("left Side")
        # temp = head
        # while temp != None:
        #     print("\t",temp.val)
        #     temp = temp.next
        
        # #printing right
        # print("right side")
        # temp = prev
        # while temp != None:
        #     print("\t", temp.val)
        #     temp = temp.next

    
        #okay now its pretty simple

        l, r = head, prev
        count = 0
        while (l != None) and (r != None):
            
            if count == 0:
                temp = l.next
                l.next = r
                l = temp
                count += 1
            else:
                temp = r.next
                r.next = l
                r = temp
                count -= 1 


