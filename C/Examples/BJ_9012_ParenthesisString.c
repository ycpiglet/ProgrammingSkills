// 문제(Problem)
/* 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.  */


// 입력(Input)
/* 입력 데이터는 표준 입력을 사용한다.
입력은 T개의 테스트 데이터로 주어진다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
하나의 괄호 문자열의 길이는 2 이상 50 이하이다.  */

// 출력(Output)
/* 출력은 표준 출력을 사용한다.
만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.  */


#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    char data;
    struct Stack* link;
} Stack;

void push(Stack** root, char chr) {
    Stack* newChar = (Stack*)malloc(sizeof(Stack));
    newChar->data = chr;
    newChar->link = *root;
    *root = newChar;
}

char pop(Stack** root) {
    if (*root == NULL) {
        return '\0'; // 스택이 비었을 경우
    }
    Stack* temp = *root;
    char popped_data = temp->data;
    *root = temp->link;
    free(temp);
    return popped_data;
}

void print_stack(Stack* root) {
    while (root->link != NULL) {
        printf("%c ", root->data);
        root = root->link;
    }
    printf("\n");
}

void check(const char* str) {
    Stack* root = NULL;
    
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '(') {
            push(&root, '(');  // 여는 괄호를 스택에 추가
        } else if (str[i] == ')') {
            if (pop(&root) != '(') {
                printf("NO\n");
                return;  // 올바른 쌍이 아닌 경우
            }
        }
    }

    if (root == NULL) {
        printf("YES\n");  // 모든 괄호 쌍이 올바른 경우
    } else {
        printf("NO\n");   // 스택에 여는 괄호가 남아 있는 경우
    }
}

int main() {
    int T;
    scanf("%d\n", &T);

    for (int i=0; i < T; i++) {
        char arr[50];
        scanf("%s", arr);

        check(arr);
    }

    return 0;
}