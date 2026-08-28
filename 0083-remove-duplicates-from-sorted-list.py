from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # my approach:

        if not head or not head.next:
            return head

        temp2 = head.next
        temp1 = head
        while temp2 is not None:
            if temp1.val == temp2.val:
                temp2 = temp2.next
            else:
                temp1 = temp1.next
                temp1.val = temp2.val
                temp2 = temp2.next
        temp1.next = None
        return head

        # shorter code:

        # current = head
        # while current and current.next:
        #     if current.val == current.next.val:
        #         current.next = current.next.next
        #     else:
        #         current = current.next
        # return head

# helper: list to ListNode
def arr_to_ll(arr):
    head = ListNode(arr[0])
    current = head
    for i in arr[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

# helper: ListNode to list
def ll_to_arr(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a

c = Solution()
t = c.deleteDuplicates(arr_to_ll([1, 1, 2, 3, 3]))
print(ll_to_arr(t))

