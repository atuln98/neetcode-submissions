# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        fast=head
        while fast and fast.next:
            curr=curr.next
            fast=fast.next.next
        second = curr.next
        curr.next = None
        # reverse second half
        prev = None
        curr = second

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        curr=prev
        while head and curr:
            ahead=head.next
            next_curr=curr.next
            head.next=curr
            curr.next=ahead
            curr=next_curr
            head=ahead