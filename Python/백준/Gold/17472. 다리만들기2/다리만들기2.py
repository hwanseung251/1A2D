N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]

# 섬의 개수를 셈
def count_island(i,j):
    visited[i][j] = True
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<M:
            if not visited[ni][nj] and Map[ni][nj] == 1:
                visited[ni][nj] = True
                Map[ni][nj] = num
                count_island(ni, nj)

# 섬에 넘버링
visited = [[False]*M for _ in range(N)]
num = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1 and not visited[i][j]:
            num += 1
            Map[i][j] = num
            visited[i][j] = True
            count_island(i,j)


if num <= 1:
    print(0)

INF = float("inf")
# 각 섬과 섬의 거리 최솟갑 기록할 자료구조
min_edge = [[INF] * (num+1) for _ in range(num+1)]

for i in range(N):
    # 직전에 본 섬 (0은 바다)
    prev = 0
    # 연속 바다 길이
    dist = 0
    for j in range(M):
        cur = Map[i][j]
        # 현재 바다인데 전에 섬이었다면
        # 바다 길이 센다
        if cur == 0:
            if prev != 0:
                dist += 1
        else:
            if prev != 0:
                if cur != prev and dist >= 2:
                    u, v = prev, cur
                    # 입력되어있는 길이보다 적으면 갱신
                    # 양방향 갱신
                    if min_edge[u][v] > dist:
                        min_edge[u][v] = min_edge[v][u] = dist
            # 새로운 섬을 만났으니 초기화
            prev = cur
            dist = 0

for j in range(M):
    prev = 0
    dist = 0
    for i in range(N):
        cur = Map[i][j]
        if cur == 0:
            if prev != 0:
                dist += 1
        else:
            if prev != 0:
                if cur != prev and dist >= 2:
                    u, v = prev, cur
                    if min_edge[u][v] > dist:
                        min_edge[u][v] = min_edge[v][u] = dist
            prev = cur
            dist = 0

# min_edge를 활용해서 간선 리스트 생성
edges = []
for u in range(1, num+1):
    for v in range(1, num+1):
        if min_edge[u][v] != INF:
            edges.append((min_edge[u][v], u, v))

parent = list(range(num+1))
rank = [0]*(num+1)


# 유니온 파인드 활용
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True


edges.sort()  # 길이 오름차순
ans = 0
used = 0
for w,u,v in edges:
    if union(u,v):
        ans += w
        used += 1
        if used == num-1:
            break

print(ans if used == num-1 else -1)