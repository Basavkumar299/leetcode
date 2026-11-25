# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None :
            return head
        curr=head
        prev=None
        nxt=None
        while curr != None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
        