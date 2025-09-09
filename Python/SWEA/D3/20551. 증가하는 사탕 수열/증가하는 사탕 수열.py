T = int(input())

for t in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0
    cant = False

    if C <= B:
        if C - 1 >= 2:
            cnt += B-C+1
            B = C - 1
        else:
            cant = True

    if not cant and B <= A:
        if B - 1 >= 1:
            cnt += A-B+1
        else:
            cant = True


    print(f"#{t} {-1 if cant else cnt}")
