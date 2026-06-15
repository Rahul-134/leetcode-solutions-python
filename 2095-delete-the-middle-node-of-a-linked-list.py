from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        if length == 1:
            return None
        i = length // 2
        d = head
        while i > 1:
            d = d.next
            i -= 1
        d.next = d.next.next

        return head


# Helper function to convert python list to linked list
def convert_to_linked_list(arr):
    if not arr:
        return None

    dummy = ListNode(0)
    current = dummy

    for item in arr:
        current.next = ListNode(item)
        current = current.next

    return dummy.next

# Code to print linked list

# current_node = convert_to_linked_list([1, 2, 3, 4, 5])
# output = []
# while current_node:
#     output.append(str(current_node.val))
#     current_node = current_node.next
# print(" -> ".join(output) + " -> None")

c = Solution()
print(c.deleteMiddle(convert_to_linked_list([1,3,4,7,1,2,6])))