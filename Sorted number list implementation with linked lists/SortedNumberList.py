from Node import Node

class SortedNumberList:
    def __init__(self,):
        self.head = None
        self.tail = None

    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        new_node = Node(number)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        # set new node before the list head
        if self.head is not None and self.head.get_data() > new_node.get_data():
            new_node.set_next(self.head)
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None and current_node.next.get_data() < number:
            current_node = current_node.next

        new_node.set_next(current_node.next)
        new_node.set_previous(current_node)
        current_node.set_next(new_node)

        if new_node.next is not None:
            new_node.next.set_previous(new_node)

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):

        if self.head is None:
            return False

        curNode = self.head

        if curNode.get_data() == number:
            if curNode.next is not None:
                self.head = curNode.next
                self.head.previous = None
            else:
                self.head = None
            return True
        while curNode is not None and curNode.get_data() != number:
            curNode = curNode.next

        if curNode is None:
            return False

        if curNode.next:
            curNode.next.previous = curNode.previous
        if curNode.previous:
            curNode.previous.next = curNode.next

        return True

    def search(self, key):
        curNode = self.head
        index = 0
        while curNode.get_data != key and curNode is not None:
            curNode = curNode.next
            index += 1

        if curNode is not None:
            return index
        else:
            return -1


