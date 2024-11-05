import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
index = 1
word_list = []

for _ in range(N):
    word = data[index]
    index += 1
    
    if word[::-1] in word_list:
        print(len(word), word[len(word) // 2])
    else:
        word_list.append(word)