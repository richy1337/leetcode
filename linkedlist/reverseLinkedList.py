# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while (current != None):
            temp = current
            current = current.next

            temp.next = prev
            prev = temp
        
        head = prev
        return head
            
            
        