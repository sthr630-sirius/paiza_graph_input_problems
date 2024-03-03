"""
degree euler graph, indirected graph
"""
n, m, v = map(int, input().split())
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    if v == a or v == b:
        ans += 1

print(ans)