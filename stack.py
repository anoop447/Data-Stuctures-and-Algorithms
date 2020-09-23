
class Stack():

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def remove(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def getStack(self):
        return self.items

'''
s = Stack()
s.push(1)
s.push(2)
print(s.getStack())
s.remove()
print(s.getStack())
print(s.isEmpty())
'''
