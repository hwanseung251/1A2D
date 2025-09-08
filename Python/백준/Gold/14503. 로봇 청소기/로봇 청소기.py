N,M = map(int, input().split())
r,c,d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]


while True:
    # 현재 칸이 아직 청소안됬으면 청소함
    if Map[r][c] == 0:
        # 청소는 2로 넣어놈
        Map[r][c] = 2
        # 칸 수 카운팅
        cnt += 1
    key = False
    # 방향 탐색
    for k in range(1,5):
        # 현재 바라보는 방향을 고려한 탐색 순서
        ny = r + dy[d-k]
        nx = c + dx[d-k]
        if 0<=ny<N and 0<=nx<M:
            if Map[ny][nx] == 0:
                r = ny
                c = nx
                d = (d-k)%4
                key = True
                break
    # 4방향 중 청소되지 않은 빈칸이 없으면
    if key == False:
        # 한칸 후진
        ny = r - dy[d] 
        nx = c - dx[d]
        if 0<=ny<N and 0<=nx<M:
            # 벽이면 종료
            if Map[ny][nx] == 1:
                break
            else:
                r = ny
                c = nx
        else:
            break

print(cnt)