package cn.codecor;

import java.util.Arrays;
import java.util.Stack;
import cn.codecor.*;


public class shiyu_112{
    public static void main(String[] args) {
        shiyu_112 test = new shiyu_112();
        TreeNode cc = new TreeNode(1);

        test.hasPathSum(cc, 20);
    }

    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null) {
            return false;
        }

        if(root.left == null && root.right == null) {
            return sum-root.val == 0;
        }

        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
