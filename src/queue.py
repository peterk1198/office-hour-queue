# This is the basic queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ClassQueue:
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.head = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def peek(self):
        return self.head


