package recursive;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class leetcode_77 {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new LinkedList<>();
        helper(n, k, 1, new LinkedList<>(), res);
        return res;
    }

    public void helper(int n, int k, int start, List<Integer> cur, List<List<Integer>> res) {

        if (cur.size() == k) {
            res.add(new LinkedList<>(cur));
        }

        for (int i = start; i <= n; i++) {
            cur.add(i);
            helper(n, k, i + 1, cur, res);
            cur.remove(cur.size() - 1);
        }

    }

    public static void main(String[] args) {
        leetcode_77 obj = new leetcode_77();
        int n = 4;
        int k = 2;
        System.out.println(obj.combine(n, k));

    }


}
