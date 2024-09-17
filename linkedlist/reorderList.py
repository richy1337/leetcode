# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head.next or not head.next.next: #Base Case for single-attribute and two-attribute linked lists (they do not need to be reordered)
            return 

        slow, fast = head, head.next #Slow and Fast pointers to find the half way point of the linked list

        while fast and fast.next: #Loop to find the half way point
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #Head of the second half of the linked list
        slow.next = None #Cutting off the linked list into two halves
        prev = None #Prev node for reversing the linked list

        while second: #Reversing the linked list
            temp = second
            second = second.next
            temp.next = prev
            prev = temp
        
        second = prev #Setting it back to the head of the second half of the linked list (bc loop cuts off when second is None)


        current = head #Head of the first half of the linked list
        while second: #Loop to reorder lists
            tempCurr = current.next
            current.next = second
            tempSec = second.next
            second.next = tempCurr
            second = tempSec
            current = current.next.next
        
        return #Return


''' Useful tools for solving linkedlist problems efficiently:
1. Reversing a linked list -> when you need to traverse a linked list backwards it's often beneficial to reverse the portion that you need to traverse backwards
2. Finding the mid-way point of a linked list using a slow and a fast pointer -> slow, fast = current, current.next when fast pointer reaches end, fast.next = None that means list is even, fast = None that means list is Odd
'''


        