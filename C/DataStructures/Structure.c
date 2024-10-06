#include <stdio.h>

typedef struct {
    char name[20];
    int price;
} Fruit;

enum Direction {
    NORTH, EAST, SOUTH, WEST
};

typedef enum {
    APP_NONE,
    APP_SCENE_1,
    APP_SCENE_2,
    APP_SCENE_3,
    APP_SCENE_4,
    APP_COUNT
} App_id_t; // Alias

int main() {
    Fruit f1 = {"Apple", 1500};
    Fruit f2 = {"Peach", 2000};

    Fruit f[3] = {f1, f2, {"Melon", 4500}};
    for (int i=0; i < 3; i++) {
        printf("%s, %d\n", f[i].name, f[i].price);
    }

    enum Direction dir = EAST;
    if (dir == EAST) {
        printf("동쪽으로 이동\n");
    }

    return 0;
}