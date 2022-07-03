# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode_Naive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(n), space: O(n)
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)

        return arr[len(arr)//2]
    
    def moiddleNode_fastslow(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(n), space:O(1)

        # return none if head == None
        if head == None:
            return head
        slow = fast = head
        # fast goes twice faster than slow
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow