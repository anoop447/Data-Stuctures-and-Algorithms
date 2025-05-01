from collections import deque

class TreeNode():

    def __init__(self,value):
        self.value = value
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)

root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode('C')
node_d = TreeNode('D')
node_e = TreeNode('E')

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)



def dfs(node):
    if node:
        print(node.value)
    for child in node.children:
        dfs(child)

dfs(root)

print(" ")

def bfs(node):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value)
        for child in current.children:
            queue.append(child)

bfs(root)

print(" ")

def count_nodes(node):
    if node is None:
        return 0
    count = 1
    for child in node.children:
        count += count_nodes(child)

    return count
print(count_nodes(root))
        
print(' ')

def tree_height(node):
    if not node.children:
        return 1
    height = [tree_height(child) for child in node.children]
    return 1 + max(height)
print(tree_height(root))

print(' ')

def leaf_count(node):
    if not node.children:
        return 1
    return sum([leaf_count(child) for child in node.children])
    
print(leaf_count(root))

print(' ')

