# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # create empty node to build answer
        # should be 0 but leaving blank as a placeholder
        head = ListNode()
        # to keep track of our pointer initialize current to be the head
        # used to traverse new linked list we created to hold our answer
        current = head

        carry = 0

        # while l1 and l2 and carry aren't 0
        # if any of these are true we have more numbers to add
        while (l1 != None or l2 != None or carry != 0):
            # variable to store value of l1 node
            # if l1 isn't none then take the value, if it is none then just make it 0
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            # calculate total l1_value + l2_value + carry
            total = l1_value + l2_value + carry

            # create new ListNode to hold the answer, and the value will be the total
            # value = total % 10 bc dividing by 10 and taking the remainder
            # eliminates what's in the 10's place and keep the ones place.
            current.next = ListNode(total % 10)
            # carry = total floor divided by 10
            carry = total // 10
            # checks to make sure there is a next node if not then it's None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # advance current
            current = current.next

        return head.next
