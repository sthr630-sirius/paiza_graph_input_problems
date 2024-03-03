"""
degree euler graph, indirected graph
"""
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    print(len(g[i]), end ="")
    if i < n-1:
        print(" ", end = "")
