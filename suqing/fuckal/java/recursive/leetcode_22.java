package recursive;

import java.util.LinkedList;
import java.util.List;

public class leetcode_22 {
    public List<String> generateParenthesis(int n) {
        List<String> res = new LinkedList<>();
        helper(n, 0, 0, "", res);
        return res;
    }

    public void helper(int n, int leftNums, int rightNums, String cur, List<String> res) {
        // terminated
        if (leftNums == n && rightNums == n) {
            res.add(cur);
        }
        // current level
        if (leftNums < n) {
            helper(n, leftNums + 1, rightNums, cur + "(", res);
        }
        if (rightNums < leftNums) {
            helper(n, leftNums, rightNums + 1, cur + ")", res);
        }

    }

    public static void main(String[] args) {
        leetcode_22 obj = new leetcode_22();
        int n = 3;
        List<String> res = obj.generateParenthesis(n);
        System.out.println(res);
    }
}
