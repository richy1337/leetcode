# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
            
        current = head
        duplicate = current.val

        while current and current.next:
            if current.next.val == duplicate:
                current.next = current.next.next
            else:
                current = current.next
                duplicate = current.val

        return head

        