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
        # link
        curr_1=head
        curr_2=prev
        while curr_2:
            tmp1,tmp2=curr_1.next,curr_2.next
            curr_1.next=curr_2
            curr_2.next=tmp1
            curr_1,curr_2=tmp1,tmp2
        slow.next=None