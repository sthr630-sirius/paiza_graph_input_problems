"""
degree euler graph, directed graph
"""
n, m = map(int, input().split())
outdegree = [0]*n
indegree = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    outdegree[a] += 1
    indegree[b] += 1

print(*indegree)
print(*outdegree)