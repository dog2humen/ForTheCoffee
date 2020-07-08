#include <stdlib.h>
#include <stdio.h>

int* divingBoard(int shorter, int longer, int k, int* returnSize){
    if(k == 0) {
        *returnSize = 0;
        return 0;
    }

    if(shorter == longer) {
        *returnSize = 1;
        int* p = (int*)malloc(sizeof(int));
        *p = shorter * k;
        return p;
    }

    *returnSize = k + 1;
    int* lengths = (int*)malloc(sizeof(int) * (k + 1));

    int i;
    int shortest = shorter * k;
    for (i = 0; i <= k; i++) {
        lengths[i] = shortest + (longer - shorter) * i;
    }

    return lengths;
}


int main(int argsc, char* argsv[]) {
    int s = 1, l = 2, k = 10;
    int* size = (int*)malloc(sizeof(int));;
    int* ret = NULL;

    ret = divingBoard(s, l, k, size);

    int i;
    for (i = 0; i < *size; i++) {
        printf("i: %d, ret: %d\n", i, *(ret + i));
    }

    return 0;
}
