# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        midnode = self.findMiddle(head)
        nexthead = midnode.next
        midnode.next = None
        lefthead = self.sortList(head)
        righthead = self.sortList(nexthead)
        sortedlist = self.merge(lefthead, righthead)

        return sortedlist
    
    def findMiddle(self, head):
        slow = fast = head
        # while fast != None and fast.next != None:
        # this is to get the node next to the first middle node when the length is even
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        # initialize the result node
        result = None
        # if one node is None, return the other node
        if left == None:
            return right
        if right == None:
            return left
        # choose the smaller one (ascending order) and recursion
        if left.val <= right.val:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result




