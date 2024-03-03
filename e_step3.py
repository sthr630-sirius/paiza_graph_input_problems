"""
degree euler graph, indirected graph
連結無向グラフにおいて、全ての辺を一筆書きして最初の頂点に戻ってくることことができることの必要十分条件
（euler graphであることの必要十分条件）
「全ての頂点の次数が偶数」
"""
n, m = map(int, input().split())
degree = [0]*n
isEuler = True

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    degree[a] += 1
    degree[b] += 1

for d in degree:
    if d%2 == 1:
        isEuler = False

if isEuler:
    print(1)
else:
    print(0)