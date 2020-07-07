
import java.util.*;
import java.util.stream.Collectors;

public class pastqing_378 {

    public int kthSmallest(int[][] matrix, int k) {
        return kthSmallest_v1(matrix, k);
    }

    /*
        利用堆排序
     */
    public int kthSmallest_v1(int[][] matrix, int k) {
        // 使用java stream 将矩阵偏平
        int[] data = Arrays.stream(matrix).flatMapToInt(row -> Arrays.stream(row)).toArray();

        // PriorityQueue 默认是小顶堆
        // 取第k小, 即取len(matrix) - k + 1大
        int size = data.length - k + 1;
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(size);
        for (int num : data) {
            if (heap.size() < size) {
                heap.offer(num);
            } else if (heap.peek() < num) {
                heap.poll();
                heap.offer(num);
            }
        }
        int res = 0;
        for (int i = 0; i < size; i++) {
            res = heap.poll();
            break;
        }
        return res;


    }

    public int kthSmallest_v2(int[][] matrix, int k) {
        return 0;
    }

    public static void main(String[] args) {
//        int[][] input = {{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};
        int[][] input = {{-5}};
        Leetcode_378 obj = new Leetcode_378();
        int res = obj.kthSmallest(input, 1);
        System.out.println(res);
    }
}

