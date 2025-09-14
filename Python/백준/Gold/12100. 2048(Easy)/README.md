## 문제 상황

2048 최대 타일 탐색 문제를 DFS(깊이 탐색)로 풀던 중,
gravity(arr) 함수가 원본 배열을 in-place 수정하면서
재귀 분기마다 서로 다른 보드 상태가 오염됨 → 오답 발생

## 원인 분석

파이썬에서 리스트는 참조 타입

gravity(arr)에서 arr를 직접 수정하면

이후 다른 분기(예: 오른쪽 이동, 위쪽 이동)에서도 바뀐 arr로 탐색

결과적으로 LEFT → RIGHT → ... 순으로만 탐색되는 꼴

## 해결 방법 – deepcopy 적용

import copy 후, 재귀 호출 전에 copy.deepcopy(arr)로 완전한 복사본 생성

각 분기에서 독립적인 보드 상태를 유지할 수 있음

## 정리
얕은 복사(shallow copy) 는 중첩 리스트에서 참조가 공유돼 버그 유발

깊은 복사(deepcopy) 는 중첩 객체까지 전부 새로운 메모리에 할당 → 안전

브루트포스/DFS/시뮬레이션 문제에서 상태 보존이 중요할 때 필수적으로 사용

## 회전 정리
```
left_90 = list(map(list, zip(*arr)))[::-1]
right_90 = list(map(list, zip(*arr[::-1])))
turn_180 = [list(row)[::-1] for row in arr[::-1]] 
```