from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 0123

pipe_dict = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}
opp = {0: 1, 1: 0, 2: 3, 3: 2}


def bfs(i,j,L):
    q = deque()
    visited = [[False]*M for _ in range(N)]
    q.append((i, j))
    visited[i][j] = True

    cnt = 1
    time = 1

    while q and time < L:
        for _ in range(len(q)):
            ci, cj = q.popleft()

            for d in pipe_dict.get(tunnel[ci][cj], []):
                ni = ci + direction[d][0]
                nj = cj + direction[d][1]
                if 0<=ni<N and 0<=nj<M:
                    if tunnel[ni][nj] != 0 and not visited[ni][nj] and opp[d] in pipe_dict.get(tunnel[ni][nj], []):
                        visited[ni][nj] = True
                        q.append((ni, nj))
                        cnt += 1
        time += 1

    return cnt

T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{t} {bfs(R, C, L)}")