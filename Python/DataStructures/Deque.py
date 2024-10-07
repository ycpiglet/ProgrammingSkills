from collections import deque

# Double Ended Queue(Deque)
# 데크 객체 생성
dq = deque(range(3))
print(dq)

# 오른쪽에 삽입
dq.append(1)
print(dq)

# 왼쪽에 삽입
dq.appendleft(2)
print(dq)

# 오른쪽에서 요소 제거 및 반환
dq.pop()
print(dq)

# 왼쪽에서 요소 제거 및 반환
dq.popleft()
print(dq)

# 인덱스 위치에 데이터 삽입
dq.insert(1, 3)
print(dq)

# 일치하는 첫 번째 값 제거
dq.remove(1)
print(dq)

# 순서 뒤집기
dq.reverse()
print(dq)

# 일치하는 값의 갯수
print(dq.count(2))

# +오른쪽으로 회전, -왼쪽으로 회전
dq.rotate(1)
print(dq)

# 모든 요소 제거(길이 0)
dq.clear()
print(dq)