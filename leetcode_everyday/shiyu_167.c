#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int i, j;

    for(i = 0;i<numbersSize;i++) {
        for(j = i+1;j<numbersSize;j++) {
            if(*(numbers+i) + *(numbers+j) == target) {
                *returnSize = 2;
                int *returnNum = (int *)malloc(sizeof(int) * *returnSize);
                *returnNum = (i+1);
                *(returnNum+1) = (j+1);

                return returnNum;
            }else if(*(numbers+i) + *(numbers+j) < target) {
                continue;
            }else {
                break;
            }
        }
    }

    return NULL;
}

int main(int argc, char* argv[]) {
    int returnSize = 0;
    int *numbers = malloc(sizeof(int) * 4);
    *(numbers+0) = 2;
    *(numbers+1) = 7;
    *(numbers+2) = 11;
    *(numbers+3) = 15;

    int *ret = twoSum(numbers, 4, 9, &returnSize);

    printf("%d\n", returnSize);
    printf("%d\n", *ret);
    printf("%d\n", *(ret+1));

    //free(returnSize);
    free(numbers);
    free(ret);

    return 0;
}
