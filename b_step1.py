"""
output adjacency list, indirected graph
"""
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

g.pop(0)

for gi in g:
    print(*sorted(gi))
