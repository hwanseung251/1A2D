import sys
sys.stdin = open("input.txt")

import copy
def recur(depth, arr):
    global max_value
    if depth == 5:
        current_max = max(max(i) for i in arr)
        max_value = max(current_max, max_value)
        return
    # 오른쪽에서 왼쪽으로 붙이기(default)
    recur(depth+1, gravity(arr))
    # 왼쪽에서 오른쪽으로 붙이기 - 180회전 함수 180회전
    r1 = gravity([list(row)[::-1] for row in arr[::-1]])
    recur(depth+1, [list(row)[::-1] for row in r1[::-1]])
    # 아래에서 위로 붙이기 - 왼쪽회전 함수 오른쪽회전
    r2 = gravity(list(map(list, zip(*arr)))[::-1])
    recur(depth+1, list(map(list, zip(*r2[::-1]))))
    # 위에서 아래로 붙이기 - 오른쪽회전1 함수 왼쪽회전
    r3 = gravity(list(map(list, zip(*arr[::-1]))))
    recur(depth+1, list(map(list, zip(*r3)))[::-1])


def gravity(input_arr):
    # 오른쪽에서 왼쪽으로 붙이기
    copy_arr = copy.deepcopy(input_arr)
    for i in range(N):
        result = []
        stack = []
        for j in range(N):
            # 0이면 pass
            if copy_arr[i][j] == 0:
                continue
            if not stack:
                stack.append(copy_arr[i][j])
                continue

            a = stack.pop()
            if a == copy_arr[i][j]:
                result.append(2*a)
            else:
                result.append(a)
                stack.append(copy_arr[i][j])
        if stack:
            result.append(stack.pop())
        r_len = len(result)
        copy_arr[i] = result + [0]*(N - r_len)

    return copy_arr


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_value = 0
recur(0, board)
print(max_value)