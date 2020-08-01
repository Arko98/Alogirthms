global INF 
INF = 10000

def Bellman_Ford(Weight):
  dist = [0]+[INF for i in range(len(Weight)-1)]
  edge_list = []
  for i in range(len(Weight)):
    for j in range(len(Weight)):
      if (Weight[i][j]!=0 or Weight[i][j]!=INF):
        edge_list.append((i,j))
  for i in range(len(Weight)):
    update = False
    for e in edge_list:
      if (dist[e[1]] > dist[e[0]]+Weight[e[0]][e[1]]):
        dist[e[1]] = dist[e[0]]+Weight[e[0]][e[1]]
        update = True
    if (update == False):
      break
    return dist

# Input Graph Adjacency Matrix
W = [[0,-1,4,INF,INF],
     [INF,0,3,2,2],
     [INF,INF,0,INF,INF],
     [INF,1,5,0,INF],
     [INF,INF,INF,-3,0]]

dist_vals = Bellman_Ford(W)
print(dist_vals)
