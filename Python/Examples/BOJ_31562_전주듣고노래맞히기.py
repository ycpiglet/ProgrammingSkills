import sys
input = sys.stdin.readline

N, M = map(int, input().split())
music_info = []
for _ in range(N):
    music_info.append(list(input().split()))

hints = []
for _ in range(M):
    hints.append(list(input().split()))

for i in range(M):
    possibility = 0
    for music in music_info:
        if hints[i] == music[2:5]:
            possibility += 1
            song = music[1]
    if possibility == 2:
        print("?")
    elif possibility == 1:
        print(song)
    elif possibility == 0:
        print("!")