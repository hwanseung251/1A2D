# 배운점
유니온 파인드 (Union-Find, Disjoint Set Union)

유니온 파인드(Union-Find)는 서로소 집합(Disjoint Set)을 관리하기 위한 자료구조입니다.
여러 원소들이 속한 집합을 빠르게 확인하고, 두 집합을 효율적으로 합치는 데 특화되어 있습니다.

## 핵심 개념
개념	설명
집합(Set)	공통된 속성을 가진 원소들의 모음
서로소 집합(Disjoint Set)	서로 겹치지 않는 집합들의 모음 (즉, 교집합이 없음)
Find	특정 원소가 어떤 집합에 속하는지(대표자/루트 노드) 찾는 연산
Union	두 집합을 하나의 집합으로 합치는 연산
## 자료구조 구현 방식

유니온 파인드는 보통 트리 기반으로 구현됩니다.

배열 parent[]

parent[x]는 x의 부모 노드 인덱스를 저장

루트 노드라면 자기 자신을 가리킴 (parent[x] == x)

기본 연산

# Find 연산
```
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]
```

# Union 연산
```
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a  # 한 쪽을 다른 쪽 루트로 연결
```