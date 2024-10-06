#include <stdio.h>  // Standard Input Output: printf(), scanf(), ...
#include <stdlib.h> // Standard Library: malloc(), calloc(), realloc(), free(), atoi(), qsort(), ...
#include <string.h> // String: strcpy(), strcmp(), strlen(), strcat(), strchr(), strstr(), ...
#include <math.h>   // Mathematics: sqrt(), pow(), abs(), exp(), log(), ceil(), floor(), round(), sin(), cos(), tan(), atan(), ...
#include <limits.h> // INT_MAX, INT_MIN, LONG_MAX, ...
#include <ctype.h>  // isdigit(), isalpha(), isalnum(), isspace(),islower(), isupper(), isprint(), tolower(), toupper(), ...

// 상수(Constant) 정의
#define MAX 100

// 사용자 정의 함수 sum() 선언 및 정의
int sum(int a, int b) {
    int result = a + b;
    return result;
}

// 사용자 정의 함수 선언, 정의 분리
// 사용자 정의 함수 diff() 선언: 함수 원형(Function Prototype)
int diff(int a, int b);

struct Student {
    char name[50];
    int age;
    float gpa;
};

// main() 함수 시작
int main(void) { // main() 함수에 인자(Argument) 넘기지 않음
    int array[] = {1, 2, 3, 4, 5};
    int octet = 0101;
    int num = 5;
    int arr[MAX] = {0};
    int num_size = sizeof(num);

    struct Student student1 = {"Alice", 21, 3.9};

    char sptr[] = "Hello World";
    printf("%s \n", sptr);

    // 반복문 1: for(초기값; 조건식; 증감식);
    for (int i=0; i < (int)strlen(sptr); i++) {
        if (isupper(sptr[i])) {
            sptr[i] = tolower(sptr[i]);
        }
        else {
            sptr[i] = toupper(sptr[i]);
        }
    }
    printf("%s \n", sptr);

    char* s1 = student1.name;
    char s2[10];
    strcpy(s2, s1);
    printf("%s %s %s\n", s1, s2, student1.name);
    s1[0] = 'a';
    printf("%s %s %s\n", s1, s2, student1.name);

    printf("%d, %o\n", octet, octet);
    printf("%d\n", array[0]);

    // 반복문2: while(조건식);
    float k = 0;
    while(k < 5.1) {
        printf("%2.1f ", k);
        k++;
    }

    int x, y;
    printf("Enter two numbers: ");
    scanf("%d, %d", &x, &y);

    if (sum(x, y) > 7) {
        printf("%d\n", diff(x, y));
    }
    else {
        printf("%d\n", diff(x, y));
    }

    // main() 함수 정상 종료
    return 0;
}

// 사용자 정의 함수 diff() 정의: 함수 헤더(Function Header)와 함수 본체(Function Body)
int diff(int a, int b) {
    return abs(a-b);
}