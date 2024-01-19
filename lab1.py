class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackArray:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueArray:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def size(self):
        return len(self.queue)

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            popped_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return popped_item
        else:
            return None

    def front(self):
        if not self.is_empty():
            return self.front.data
        else:
            return None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
