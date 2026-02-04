# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        carry = 0 
        result = ListNode(0) # type: ignore #creates linked list with node of 0 to represent final result
        #print(result)
        pointer = result #used to move to the next node

        #while l1, l2, or carry hold units
        while l1 or l2 or carry:
            #if value is None, value is 0
            firstNum = l1.val if l1 else 0
            secondNum = l2.val if l2 else 0

            sum = firstNum + secondNum + carry
            num = sum%10 #last digit
            carry = sum//10 #carries if sum >=10

            #save result to pointer.next
            pointer.next = ListNode(num) # type: ignore
            #set pointer to the next node
            pointer = pointer.next

            #update each linked list to start at the next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next #this is dummy node = to 0