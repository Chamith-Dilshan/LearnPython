from typing import Optional

class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next: Optional['LinkedList.Node'] = None

    def __init__(self):
        self.length: int = 0
        self.head: Optional[LinkedList.Node] = None

    def is_empty(self) -> bool:
        return self.length == 0

    def add(self, element) -> None:
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node is not None and current_node.element != element:
                current_node = current_node.next
            if current_node is not None:
                current_node.next = node
        self.length += 1

    def remove(self, element) -> None:
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1


def main():
    my_list = LinkedList()
    print(my_list.is_empty())

    my_list.add(1)
    my_list.add(2)
    print(my_list.is_empty())
    print(my_list.length)

    my_list.remove(1)
    print(my_list.length)


if __name__ == "__main__":
    main()