graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}


visited = []
queue = []

def bfs(visited,ad_max,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s,end=' ')
        
        for neigbour in graph[s]:
            if neigbour not in visited:
                visited.append(neigbour)
                queue.append(neigbour)
            


bfs(visited,graph,'A')

