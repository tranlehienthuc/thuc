class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]

    def push(self, item):
        if len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        if not self.stacks:
            return None
        item = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return item

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        item = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return item


set_of_stacks = SetOfStacks(3)  

for i in range(10):
    set_of_stacks.push(i)

print(set_of_stacks.stacks)  

print(set_of_stacks.pop())  
print(set_of_stacks.popAt(1))  

print(set_of_stacks.stacks)  
