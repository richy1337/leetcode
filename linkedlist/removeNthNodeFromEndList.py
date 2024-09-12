# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        prev = None
        count = 0

        while (current != None):
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
            count += 1
        

        current = prev #head node
        head = current # store the head to come back to later
        prev = None
        for i in range(n-1): #loop to find the node to remove
            prev = current
            current = current.next
        
        
        #We are on the node that we want to remove now
        #Check for edge cases i.e. end or beginning
        if n == 1:
            temp = current
            current = current.next #so we don't lose the linked list
            head = current
            temp.next = None
        elif n == count:
            prev.next = None
        else:
            prev.next = current.next


        current = head
        prev = None
        while (current != None):
            temp = current
            current = current.next
            temp.next = prev
            prev = temp

        head = prev
        return head
        


        
