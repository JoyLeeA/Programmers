#배달 python
#N = 5
N = 6
#road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
#K = 3
K = 4

from collections import deque
def bfs(start, maps, distance, K):
    Q = deque()
    Q.append(start)
    distance[start] = 0
    while Q:
        y = Q.popleft()
        for x in range(1, len(maps)):
            if maps[y][x]:
                if distance[x] > distance[y] + maps[y][x] and distance[y] + maps[y][x] <= K:
                    distance[x] = distance[y] + maps[y][x]
                    Q.append(x)
    cnt = 0 
    for d in distance:
        if d <= K:
            cnt +=1
    return cnt

def solution(N, road, K):
    distance = [float('inf') for _ in range(N+1)]
    
    maps = [[0]*(N+1) for _ in range(N+1)]
    for fRom, to, w in road:
        if not (maps[fRom][to] or  maps[to][fRom]):
            maps[fRom][to], maps[to][fRom] = w,w
        else:
            if w < maps[fRom][to]:
                maps[fRom][to], maps[to][fRom] = w, w
    
    return bfs(1, maps, distance, K)

print(solution(N, road,K))