"""
input adjacency matrix, number of edge
"""
n = int(input())
g = []
ans = 0
for _ in range(n):
    g.append(list(map(int, input().split())))
for i in range(n):
    ans += sum(g[i])
print(ans//2)