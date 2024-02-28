"""
output adjacency list, directed graph
"""
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b)

for gi in g:
    if gi:
        print(*sorted(gi))
    else:
        print(-1)
