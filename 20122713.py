def DFS(graph,start):
   visited=set()
   stack=[start]
   while stack:
      u=stack.pop()
      if u in visited:continue
      yield u
      visited.add(u)
      for v in reversed(graph[u]):
         if v in visited:continue
         stack.append(v)
def BFS(graph,start):
   visited=set()
   queue=[start]
   while queue:
      u=queue.pop()
      if u in visited:continue
      yield u
      visited.add(u)
      for v in graph[u]:
         if v in visited:continue
         queue.insert(0,v)
_,edges,start=map(int,raw_input().split())
graph=dict()
for _ in range(edges):
   u,v=map(int,raw_input().split())
   graph.setdefault(u,[]).append(v)
   graph.setdefault(v,[]).append(u)
for u in graph:graph[u].sort()
for u in DFS(graph,start):
   print u,
print
for u in BFS(graph,start):
   print u,
