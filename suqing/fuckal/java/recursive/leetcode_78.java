package recursive;
import java.util.*;
/*
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 */
public class leetcode_78 {
    public List<List<Integer>> subsets(int[] nums) {
        return subsets_v1(nums);
    }

    public List<List<Integer>> subsets_v1(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        helper(nums, 0, new LinkedList<Integer>(), res);
        return res;
    }

    public void helper(int[] nums, int start, List<Integer> cur, List<List<Integer>> res) {

        res.add(new ArrayList<>(cur));
        for (int i = start; i < nums.length; i++) {
            cur.add(nums[i]);
            helper(nums, i + 1, cur, res);
            cur.remove(cur.size() - 1);
        }
    }

    public static void main(String[] args) {
        leetcode_78 obj = new leetcode_78();
        int[] nums = {1, 2, 3};
        List<List<Integer>> res = obj.subsets(nums);
        System.out.println(res);
    }
}
