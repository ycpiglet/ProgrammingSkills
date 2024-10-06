#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct WordChain{
    char* data;       // 문자열을 가리키는 포인터
    struct WordChain* next; // 다음 노드를 가리키는 포인터
} WordChain;

void add_word(WordChain** dest, const char* word) {
    // 첫 단어인 경우
    if (*dest == NULL) {
        *dest = (WordChain*)malloc(sizeof(WordChain));
        (*dest)->data = strdup(word);
        (*dest)->next = NULL;
        return;
    }

    // 끝말잇기용 노드 생성
    WordChain* last = *dest;
    while (last->next != NULL) {
        last = last->next;
    }

    // 마지막 글자
    char last_char = last->data[strlen(last->data) - 1];
    // 끝말잇기 규칙 확인(이전 단어의 마지막 글자와 새 단어의 첫 글자 비교)
    if (last_char == word[0]) {
        WordChain* new_word = (WordChain*)malloc(sizeof(WordChain));
        new_word->data = strdup(word);
        new_word->next = NULL;
        last->next = new_word;
    }
    else printf("'%s'는 끝말잇기 규칙에 맞지 않습니다!\n", word);
}

void free_words(WordChain* src) {
    WordChain* temp;
    while(src != NULL) {
        temp = src;
        src = src->next;
        free(temp->data);
        free(temp);
    }
}

void print_words(WordChain* src) {
    while (src != NULL) {
        printf("%s", src->data);
        src = src->next;
        if (src != NULL) printf(" -> ");
    }
    printf("\n");
}

int main() {
    // WordChain* root = NULL;
    // WordChain word[4];

    // root = &word[0];

    // word[0].data = "CREAM";
    // word[0].next = &word[1];

    // word[1].data = "MILK";
    // word[1].next = &word[2];
    
    // word[2].data = "KAKAO";
    // word[2].next = &word[3];
    
    // word[3].data = "ORANGE";
    // word[3].next = NULL;

    // printf("%s -> %s -> %s -> %s\n", root->data, root->next->data, root->next->next->data, root->next->next->next->data);

    WordChain* root = NULL;
    char word[100];
    int num_words;

    printf("끝말잇기를 위해 단어의 개수를 입력하세요: ");
    scanf("%d", &num_words);

    for (int i = 0; i < num_words; i++) {
        printf("%d번째 단어를 입력하세요: ", i + 1);
        scanf("%s", word);
        add_word(&root, word);
    }

    // 연결리스트 출력
    print_words(root);

    // 메모리 해제
    free_words(root);

    return 0;
}