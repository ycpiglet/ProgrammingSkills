from itertools import product

def generate_unlucky_sequence(N):
    # 숫자를 저장할 리스트
    unlucky_numbers = []
    num = 1 # 조합하는 경우의 수
    
    while len(unlucky_numbers) < N: # 입력받은 수보다 긴 수열을 만들어야 함
        # 4와 13의 조합을 이용해 모든 가능한 수 생성
        for combination in product([4, 13], repeat=num):
            number = ''.join(map(str, combination))
            unlucky_numbers.append(int(number))
        # 조합하는 경우의 수 늘림
        num += 1
    
    # 오름차순 정렬
    unlucky_numbers.sort()
    
    
    return unlucky_numbers

if __name__ == '__main__':
    # n번째 수 입력 받기
    n = int(input("임의의 수를 입력하세요: "))

    # 불길한 수열 생성
    unlucky_sequence = generate_unlucky_sequence(n)
    print(unlucky_sequence)
    
    # n번째 숫자 반환 (n은 1부터 시작하므로 0-based index 처리)
    answer = unlucky_sequence[n-1]
    print(answer)