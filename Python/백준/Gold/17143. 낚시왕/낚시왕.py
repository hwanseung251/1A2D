import sys
sys.stdin = open("input.txt")


def move_1d(pos1, speed, dir_code, L, neg_code, pos_code):
    """
    pos1: 세로방향일 땐 i, 가로방향일 땐 j
    speed: 이동 칸수 s
    dir_code: direction
    L: 축 길이 (R 또는 C)
    반환: next_i or j, next_direction
    """
    if L == 1 or speed == 0:
        return pos1, dir_code

    period = 2 * (L - 1)
    k = speed % period
    if k == 0:
        # 제자리면 방향도 유지
        return pos1, dir_code

    sgn = +1 if dir_code == pos_code else -1  # ↓/→ = +1, ↑/← = -1
    x0 = pos1 - 1             # 0-based
    span = L - 1              # 왕복 반사 기준 길이

    # x0 + sgn*k 를 span으로 나눈 몫(q)과 나머지(r)를 이용
    q, r = divmod(x0 + sgn * k, span)

    if q % 2 == 0:
        pos0 = r
        sgn2 = sgn            # 반사 횟수 짝수 → 진행부호 유지
    else:
        pos0 = span - r
        sgn2 = -sgn           # 반사 횟수 홀수 → 진행부호 반전

    new_pos1 = pos0 + 1
    new_dir = pos_code if sgn2 == +1 else neg_code
    return new_pos1, new_dir


R, C, M = map(int, input().split())
beach = [[False] * (C+1) for _ in range(R+1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    beach[r][c] = (s, d, z)


di = [0, -1, 1, 0, 0] # 1상 2하 3우 4좌
dj = [0, 0, 0, 1, -1]

cnt = 0
for peaple in range(1, C+1):
    # 낚시
    for r in range(1, R+1):
        # 땅에서 가까운 상어를 만나면 상어의 크기만큼 카운팅
        if beach[r][peaple] != False:
            cnt += beach[r][peaple][2]
            # 상어잡았으니 False처리
            beach[r][peaple] = False
            break

    # 상어 이동 반영할 바다
    next_beach = [[False] * (C+1) for _ in range(R+1)]
    # 상어 이동
    for i in range(1, R+1):
        for j in range(1, C+1):
            if beach[i][j] == False:
                continue

            speed, direction, size = beach[i][j]

            if direction in (1, 2):  # 세로
                next_i, direction = move_1d(i, speed, direction, R, neg_code=1, pos_code=2)
                next_j = j
            else:  # 가로 (3,4)
                next_j, direction = move_1d(j, speed, direction, C, neg_code=4, pos_code=3)
                next_i = i

            beach[i][j] = False
            if not next_beach[next_i][next_j]:
                next_beach[next_i][next_j] = (speed, direction, size)
            else:
                if next_beach[next_i][next_j][2] < size:
                    next_beach[next_i][next_j] = (speed, direction, size)

    beach = next_beach

print(cnt)