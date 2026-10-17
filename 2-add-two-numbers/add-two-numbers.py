class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2:
            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            total = a + b + carry
            if total >= 10:
                carry = 1
                total = total - 10
            else:
                carry = 0
            temp.next = ListNode(total)
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return dummy.next