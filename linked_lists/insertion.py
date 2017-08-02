class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        the_head = self.head
        print(the_head.data)
        while the_head is not None:
            print(the_head.data)
            the_head = the_head.next

    def insert(self, data):
        new_node = Node(data=data, next_node=None)
        if self.head is None:
            self.head = new_node
            return self
        the_head = self.head
        while the_head.next is not None:
            the_head = the_head.next
        the_head.next = new_node
        return self


link = LinkedList()
first_node = Node(data=1)
second_node = Node(data=2)
link.insert(first_node)
link.insert(second_node)
print(link)
