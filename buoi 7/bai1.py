class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        value = self.list.reverse()
        value = [str(x) for x in self.list]
        return '\n'.join(value)
    def isEmty(self):
        if self.list == []:
            return True
        else:
            return False
customStack = Stack()
print(customStack.isEmty())
        