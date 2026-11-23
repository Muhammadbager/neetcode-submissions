class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head


    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return - 1


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        # Move curr to the node before index
        for _ in range(index):
            if curr is None:
                return
            curr = curr.next

        # If index is greater than the list length
        if curr is None:
            return

        new_node = ListNode(val, curr.next)
        curr.next = new_node

        # If inserted at the end, update tail
        if new_node.next is None:
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for _ in range(index):
            if curr is None:
                break
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)