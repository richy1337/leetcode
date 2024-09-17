# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Function to reverse a linked list
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # Reverse both linked lists
        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        numOne, numTwo = "", ""

        # Extract the number from the reversed l1
        currOne = l1
        while currOne:
            numOne += str(currOne.val)
            currOne = currOne.next

        # Extract the number from the reversed l2
        currTwo = l2
        while currTwo:
            numTwo += str(currTwo.val)
            currTwo = currTwo.next

        # Add the two numbers
        addedNum = int(numOne) + int(numTwo)

        # Convert the result back to a string
        addedNum = str(addedNum)

        # Now, create a linked list from the sum (in reverse order)
        dummy_head = ListNode(0)
        current = dummy_head

        for c in addedNum:
            # Insert each digit as a new node at the front of the list
            new_node = ListNode(int(c))
            new_node.next = current.next
            current.next = new_node

        # The list is in the correct order because we inserted nodes at the front
        return dummy_head.next
