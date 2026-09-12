# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # separate
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse the second half, starting from slow.next
        curr=slow.next
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev,curr=curr,temp
        # link the first and reversed second half, starting from prev
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next,second.next=second,tmp1
            first,second=tmp1,tmp2
        slow.next=None