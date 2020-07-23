#include <stdio.h>
#include <stdlib.h>

int minPathSum(int** grid, int gridSize, int* gridColSize){
    size_t i = 0, j = 0, col_size;
    int mini = 0, pos = 0;
    //初始化最小路径和位置容器
    int **pos_mini = (int **)calloc(gridSize, sizeof(int));
    for(i=0;i<gridSize;i++) {
        *(pos_mini+i) = (int *)calloc(*(gridColSize+i), sizeof(int));
    }
    //每个位置最小和
    for(i = 0; i < gridSize; i++) {
        col_size = *(gridColSize+i);
        for(j = 0;j < col_size; j++) {
            pos = *(grid + j + col_size * i);
            if(i == 0 || j == 0) {
                *(pos_mini + j + col_size * i) = pos;
                continue;
            }
            if(*(grid + j + col_size * (i-1)) > *(grid + (j-1) + col_size * i)) {
                *(pos_mini + j + col_size * i) = pos + *(grid + (j-1) + col_size * i);
            } else {
                *(pos_mini + j + col_size * i) = pos + *(grid + j + col_size * (i-1));
            }
        }
    }
    //查找末尾行列最小值
    for(i = 1; i < gridSize; i++) {
        col_size = *(gridColSize+i);
        for(j = 1;j < col_size; j++) {
            if(gridSize == (i-1) || j == (col_size-1)) {
                if(*(pos_mini + j + col_size * i) < mini) {
                    mini = *(pos_mini + j + col_size * i);
                }
            }
        }
    }

    return mini;
}
