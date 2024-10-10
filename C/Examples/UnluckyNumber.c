#include <stdio.h>
#include <string.h>

// 불길한 수를 문자열로 표현
const char *unluckyNumbers[] = {"4", "13"};

// 결과를 저장할 문자열
char result[100];

// 재귀적으로 불길한 수열을 생성하는 함수
void generateUnluckyNumbers(int n, int maxDigits, int currentLength) {
    if (currentLength == maxDigits) {
        // 자릿수를 다 채운 경우 출력
        printf("%s\n", result);
        return;
    }

    for (int i = 0; i < 2; i++) {
        // 각 자리에 4 또는 13을 배치
        strcat(result, unluckyNumbers[i]);
        generateUnluckyNumbers(n, maxDigits, currentLength + 1);
        // 백트래킹: 마지막 자리수 삭제
        result[strlen(result) - strlen(unluckyNumbers[i])] = '\0';
    }
}

int main() {
    int n;
    printf("n번째 불길한 수를 입력하세요: ");
    scanf("%d", &n);

    int maxDigits = 1;  // 자릿수를 늘려가며 수를 생성
    int count = 0;      // 수열에서 몇 번째인지 카운트

    // n번째 수를 찾을 때까지 자릿수를 늘려가며 생성
    while (1) {
        result[0] = '\0'; // 결과 문자열 초기화
        printf("자릿수 %d의 불길한 수열 생성 중...\n", maxDigits);
        generateUnluckyNumbers(n, maxDigits, 0);
        maxDigits++; // 자릿수를 증가시켜 탐색을 넓혀감
        if (count >= n) {
            break;
        }
    }

    return 0;
}
