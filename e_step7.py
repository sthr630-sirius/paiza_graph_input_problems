"""
euler graph, directed graph
weakly connected
有向グラフを無向グラフとみなした時に、どの２つの頂点間も辺をたどって行き来ができる：弱連結なグラフ
弱連結な有向グラフにおいて、全ての辺を一筆書きして最初の頂点に戻ってくることができる必要十分条件
(euler graphであることの必要十分条件)
「全ての頂点において、入次数と出次数が一致する」
"""
n, m = map(int, input().split())
outdegree = [0]*n
indegree = [0]*n
isWeaklyConnected = True

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    outdegree[a] += 1
    indegree[b] += 1

for ideg, odeg in zip(indegree, outdegree):
    if ideg != odeg:
        isWeaklyConnected = False

if isWeaklyConnected:
    print(1)
else:
    print(0)
