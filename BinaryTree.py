from collections import deque

class BinaryTree():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

def preOrder(node):
    if not node:
        return []
    return [node.value] + preOrder(node.left) + preOrder(node.right)

print(preOrder(root))
print(' ')

def inOrder(node):
    if not node:
        return []
    return  inOrder(node.left) + [node.value] + inOrder(node.right)

print(inOrder(root))
print(' ')

def postOrder(node):
    if not node:
        return []
    return postOrder(node.left) + postOrder(node.right) + [node.value]

print(postOrder(root))
print(' ')


def level_order_bfs(node):
    if not node:
        return 
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

level_order_bfs(root)
print(' ')

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

print(count_nodes(root))
print(' ')

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left),height(node.right))

print(height(root))
print(' ')
