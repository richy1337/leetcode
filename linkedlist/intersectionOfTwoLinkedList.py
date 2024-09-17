# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            nodes = set()

            currOne, currTwo = headA, headB

            while currOne:
                nodes.add(currOne)
                currOne = currOne.next
            
            while currTwo:
                if currTwo in nodes:
                    return currTwo
                currTwo = currTwo.next
            

            return None