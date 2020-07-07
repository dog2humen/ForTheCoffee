package cn.codecor;

import cn.codecor.*;

public class shiyu_378 {
    public static void main(String[] args) {
        shiyu_378 test = new shiyu_378();
        int[][] mx = {{1,5,9},{10,11,13},{12,13,15}};

        System.out.println("输出数字是");
        System.out.println(test.kthSmallest(mx, 8-1));
    }

    public int kthSmallest(int[][] matrix, int k) {
        int[] mergeArr = new int[matrix.length * matrix.length];

        for(int i = 0;i < matrix.length;i++) {
            this.merge(mergeArr, i, matrix[i]);
        }
        return mergeArr[k-1];
    }

    public void merge(int[] all, int times, int[] matrixArr) {
        int allNum = times * matrixArr.length;

        //首行循环直接复制
        if(allNum == 0) {
            for(int i=0;i < matrixArr.length; i++) {
                all[i] = matrixArr[i];
            }
        } else {
            //非首行合并
            int i=0,j=0;
            int cycle = allNum + matrixArr.length;
            int[] tmp = new int[cycle];

            for(int c=0;c < cycle; c++) {
                if(i>= allNum) {
                    tmp[c] = matrixArr[j];
                    j++;
                }else if (j >= matrixArr.length) {
                    tmp[c] = all[i];
                    i++;
                }else{
                    if(all[i] >= matrixArr[j]) {
                        tmp[c] = matrixArr[j];
                        j++;
                    }else {
                        tmp[c] = all[i];
                        i++;
                    }
                }
            }
            for(int c=0;c < cycle; c++) {
                all[c] = tmp[c];
            }
        }
    }
}
