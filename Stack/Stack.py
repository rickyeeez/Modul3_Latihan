class Stack:
    def __init__(self, size):
        self.maxSize = size
        self.stackArray = [None] * self.maxSize
        self.top = -1

    def push(self, value):
        self.top += 1
        self.stackArray[self.top] = value

    def pop(self):
        value = self.stackArray[self.top]
        self.top -= 1
        return value

    def peek(self):
        return self.stackArray[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.maxSize - 1

    def search(self, value):
        index = self.top
        while index >= 0:
            if self.stackArray[index] == value:
                return self.top - index + 1
            index -= 1
        return -1
