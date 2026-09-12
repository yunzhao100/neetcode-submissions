# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # seperate
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse the second half
        prev,curr=None,slow.next
        while curr:
            temp=curr.next
            curr.next=prev
            prev,curr=curr,temp
        # link
        curr_1,curr_2=head,prev
        while curr_2:
            temp1,temp2=curr_1.next,curr_2.next
            curr_1.next=curr_2
            curr_2.next=temp1
            curr_1,curr_2=temp1,temp2
        slow.next=None