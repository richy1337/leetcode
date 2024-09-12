# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            main = list1
            toMerge = list2
        else:
            main = list2
            toMerge = list1

        current = main

        while toMerge is not None:
            if main.next is None or main.next.val >= toMerge.val:
                temp = main.next
                main.next = toMerge
                toMerge = toMerge.next
                main = main.next
                main.next = temp
            else:
                main = main.next

        return current



        