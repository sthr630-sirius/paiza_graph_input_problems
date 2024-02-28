"""
output adjacency list, directed graph
"""
n, m = map(int, input().split())
g = [[] for _ in range(n)]
w = [[] for _ in range(n)]
for _ in range(m):
    a, b, weight = map(int, input().split())
    g[a-1].append(b)
    w[a-1].append(weight)

for wi in w:
    if wi:
        print(*wi)
    else:
        print(-1)
