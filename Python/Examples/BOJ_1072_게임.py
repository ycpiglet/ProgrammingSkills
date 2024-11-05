""" 게임
문제
김형택은 지금 몰래 Spider Solitaire(스파이더 카드놀이)를 하고 있다. 형택이는 이 게임을 이길 때도 있었지만, 질 때도 있었다. 누군가의 시선이 느껴진 형택이는 게임을 중단하고 코딩을 하기 시작했다. 의심을 피했다고 생각한 형택이는 다시 게임을 켰다. 그 때 형택이는 잠시 코딩을 하는 사이에 자신의 게임 실력이 눈에 띄게 향상된 것을 알았다.

이제 형택이는 앞으로의 모든 게임에서 지지 않는다. 하지만, 형택이는 게임 기록을 삭제 할 수 없기 때문에, 자신의 못하던 예전 기록이 현재 자신의 엄청난 실력을 증명하지 못한다고 생각했다.

게임 기록은 다음과 같이 생겼다.

게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

입력
각 줄에 정수 X와 Y가 주어진다.

출력
첫째 줄에 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.

제한
1 ≤ X ≤ 1,000,000,000
0 ≤ Y ≤ X """


# 1. Brute-Force
# def calculate(x, y):
#     return (y * 100) // x

# x, y = map(int, input("Enter two integers separated by a space: ").split())
# z = calculate(x, y)
# count = 0
# if x == y:
#     print(-1)
# else:
#     while calculate(x, y) == z:
#         x += 1
#         y += 1
#         count += 1
#     print(count)


# 2. Binary Search
# 플레이 수와 승리 수를 입력받는다
# x, y = map(int, input().split())

# # 현재 승률 계산
# current_win_rate = (100 * y) // x  # 정수형으로 승률을 계산

# # 이진 탐색을 위한 변수 초기화
# left, right = 0, x  # left는 0부터, right는 현재 플레이 수 x까지
# result = x          # 기본적으로 결과는 최대 플레이 수로 설정

# # 99% 이상의 승률일 경우 -1을 반환
# if current_win_rate >= 99:
#     print(-1)
# else:
#     # 이진 탐색 수행
#     while left <= right:
#         mid = (left + right) // 2
#         # 새로운 승률 계산
#         new_win_rate = (100 * (y + mid)) // (x + mid)

#         # 새로운 승률이 기존 승률보다 높으면
#         if new_win_rate > current_win_rate:
#             result = mid        # 결과 업데이트
#             right = mid - 1     # 더 작은 mid 값을 찾기 위해 오른쪽 범위를 줄임
#         else:
#             left = mid + 1      # 조건을 만족하지 않으므로 왼쪽 범위를 증가시킴

#     print(result)

# 3. Mathematics
x, y = map(int,input().split())
k = y * 100 // x # 정수 k로 치환
if x == y or (99 - k) == 0:
    print(-1)
else:
    if ((k + 1) * x - 100 * y) % (99 - k) == 0: # 나머지가 없으면 그대로, 나머지가 있으면 +1
        print(((k + 1) * x - 100 * y) // (99 - k)) 
    else:
        print(((k + 1) * x - 100 * y) // (99 - k) + 1)