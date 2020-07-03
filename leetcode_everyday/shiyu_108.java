package cn.codecor;

import java.util.LinkedList;
import java.util.Queue;

public class shiyu_108 {
    public static void main(String[] args) {
        shiyu_108 test = new shiyu_108();
        int[] arr = {-10,-3,0,5,9};
        TreeNode root = test.sortedArrayToBST(arr);
        System.out.println(root.left.val);
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        return cycle(nums, 0, nums.length - 1);
    }

    public TreeNode cycle(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }

        int mid = (left + right) / 2;

        TreeNode root = new TreeNode(nums[mid]);
        root.left = cycle(nums, left, mid - 1);
        root.right = cycle(nums, mid + 1, right);

        return root;
    }
}
