# [Unrated] [모의 SW 역량테스트] 탈주범 검거 - 1953

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq) 

### 성능 요약

메모리: 61,440 KB, 시간: 118 ms, 코드길이: 1,136 Bytes

### 제출 일자

2025-09-09 09:40

> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do

## 배운 점

- **BFS 탐색 활용**
  - 시작점에서부터 탐색을 진행하며 **레벨(시간)**을 관리하기 위해 `while q and time < L:` 구조 사용
  - 매 시간(`time`)마다 `for _ in range(len(q)):`로 큐의 현재 레벨에 있는 원소만 처리 → **레벨 단위 BFS**
- **방향 관리**
  - `direction = [[-1,0],[1,0],[0,-1],[0,1]]` : 상하좌우를 인덱스로 관리
  - `opp = {0:1, 1:0, 2:3, 3:2}` : 반대 방향을 매핑해 **연결 여부 검사**에 활용
- **파이프(터널) 모양 연결 규칙**
  - `pipe_dict`에 각 터널 번호별로 가능한 방향을 저장
  - 다음 위치로 이동할 때 `opp[d] in pipe_dict[next]` 조건으로 **양방향 연결 여부** 체크
- 시간복잡도
  - BFS는 O(V+E)
  - V(정점의 개수) = N x M(2차원 배열) = 50 x 50 = 2500
  - E(간선의 개수) = 상하좌우 x 각 정점 = 4 x 2500 = 10000개
- **결과**
  - `cnt` 변수를 사용해 방문 가능한 지점 개수를 세고, 최종적으로 반환

## 핵심

- BFS에서 **시간(레벨) 제어**를 위해 `for _ in range(len(q))` 패턴을 활용한다.
- 단순히 이동할 수 있는지만 확인하는 것이 아니라, **양쪽 터널이 서로 연결되는지**까지 확인해야 한다.
- 현재 방향과 다음 위치의 반대 방향을 체크해준다.