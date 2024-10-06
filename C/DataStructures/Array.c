#include <stdio.h>

int main(){
    int array[5] = {1, 2, 3, 4, };
    int zeros[100] = {0};
    char alphabet[30] = {'a', 'b', 'c', 'd'};

    for (int i=0; i < (int)(sizeof(array) / sizeof(int)); i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    for (int i=0; i<100; i++) {
        printf("%d ", zeros[i]);
    }
    printf("\n");

    int k = 0;
    while (alphabet[k] != 0) {
        printf("%c ", alphabet[k]);
        k++;
    }
    printf("%c %c ", alphabet[3], alphabet[4]);
    printf("%d %d ", (int)sizeof(alphabet[3]), (int)sizeof(alphabet[4]));

    return 0;
}