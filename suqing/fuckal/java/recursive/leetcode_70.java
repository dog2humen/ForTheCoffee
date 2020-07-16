package recursive;

import java.util.HashMap;
import java.util.Map;

public class leetcode_70 {

    private final Map<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        // 使用递归解法
        // f(n) = f(n - 1) + f(n - 2)
        if (n <= 2) {
            return n;
        }
        int res_1;
        int res_2;
        if (memo.containsKey(n - 1)) {
            res_1 = memo.get(n - 1);
        } else {
            res_1 = climbStairs(n - 1);
            memo.put(n - 1, res_1);
        }

        if (memo.containsKey(n - 2)) {
            res_2 = memo.get(n - 2);
        } else {
            res_2 = climbStairs(n - 2);
            memo.put(n - 2, res_2);
        }
        return res_1 + res_2;

    }
}
