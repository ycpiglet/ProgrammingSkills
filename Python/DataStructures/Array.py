import random
import copy

# Array(정적 배열)는 List(동적 배열)로 대체 가능
# 배열은 인덱스(Index)로 임의 접근(Random Access)이 가능
my_list = [1, 2, 3] # 또는 list(range(1, 4))
print(my_list)

# 리스트 인덱싱(Indexing)
my_list[2]

# 리스트 슬라이싱(Slicing)
my_list[0:1]

# 리스트 내부에 값이 존재하는지 확인
4 in my_list
print(my_list)

# Python의 변수는 값을 저장하는 것이 아니라, 객체의 주소를 참조하는 것임
# copied = my_list 이것은 복사가 아닌 할당(Assignment)
# 얕은 복사(Shallow Copy): 서로 다른 객체이지만 참조값(메모리 주소값)은 동일, 하나를 수정하면 나머지도 영향을 받음
copied = copy.copy(my_list) # 또는 my_list[:]
print(f'Copy: {id(copied)}, Original: {id(my_list)}')
copied.append(10)
my_list.append(20)
print(f'Copy: {copied}, Original: {my_list}')

# 깊은 복사(Deep Copy): 내부 객체들까지 모두 새롭게 복사, 즉 독립된 객체, copy 모듈 활용
copied = copy.deepcopy(my_list)
print(f'Copy: {id(copied)}, Original: {id(my_list)}')
copied.append(10)
my_list.append(30)
print(f'Copy: {copied}, Original: {my_list}')

# 리스트 맨 끝에 추가
my_list.append(4)
print(my_list)

# 리스트 연결하기
my_list = my_list + [5, 6]
print(my_list)

# 리스트 일치하는 값의 갯수
my_list.count(4)
print(my_list)

# 리스트 값의 인덱스 찾기
my_list.index(5)
print(my_list)

# 리스트 인덱스 위치에 추가
my_list.insert(4, 7)
print(my_list)

# 리스트 맨 끝 삭제
my_list.pop()
print(my_list)

# 리스트 일치하는 값 삭제
my_list.remove(5)
print(my_list)

# 리스트 인덱스 위치의 값 삭제
del my_list[1]
print(my_list)

# 리스트 오름차순 정렬
my_list.sort()
print(my_list)

# 리스트 내림차순 정렬
my_list.sort(reverse=True)
print(my_list)

# 리스트 순서 뒤집기
my_list.reverse()
print(my_list)

# 리스트 정렬된 결과만 반환하기
sorted(my_list)
print(my_list)