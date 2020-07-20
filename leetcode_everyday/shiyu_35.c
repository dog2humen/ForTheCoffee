#include <stdio.h>
#include <stdlib.h>

int searchInsert(int* nums, int numsSize, int target){
    int half = 0, left = 0, right = numsSize - 1, pos = numsSize;

    while(left <= right) {
        half = ((right - left) >> 1) + left;

        if (*(nums+half) >= target) {
            pos = half;
            right = half - 1;
        }else{
            left = half + 1;
        }
    }

    return pos;
}

int main(int argc, char* argv[]) {
    int i;
    int numsSize = 10;
    int *nums = (int *)malloc(sizeof(int) * numsSize);

    for(i = 0;i<numsSize;i++) {
        *(nums+i) = i*2;
    }

    printf("%d\n", searchInsert(nums, numsSize, 6));

    free(nums);

    return 0;
}
