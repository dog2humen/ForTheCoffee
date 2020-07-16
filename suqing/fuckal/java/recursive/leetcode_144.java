package recursive;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class leetcode_144 {

    public List<Integer> preorderTraversal(TreeNode root) {
//        return preorderTraversal_v1(root);
//        return preorderTraversal_v2(root);
        return preorderTraversal_v3(root);


    }

    public List<Integer> preorderTraversal_v1(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        helper(root, res);
        return res;
    }

    public void helper(TreeNode node, List<Integer> res) {
        if (node != null) {
            res.add(node.val);
            helper(node.left, res);
            helper(node.right, res);
        }
    }

    public List<Integer> preorderTraversal_v2(TreeNode root) {
        // stack
        if (root == null) {
            return new ArrayList<>();
        }

        Deque<TreeNode> stack = new LinkedList<>();
        List<Integer> res = new ArrayList<>();

        stack.addFirst(root);
        while (!stack.isEmpty()) {
            TreeNode curNode = stack.removeFirst();
            res.add(curNode.val);
            if (curNode.right != null) {
                stack.addFirst(curNode.right);
            }
            if (curNode.left != null) {
                stack.addFirst(curNode.left);
            }
        }


        return res;
    }

    public List<Integer> preorderTraversal_v3(TreeNode root) {
        Deque<TreeNode> stack = new LinkedList<>();
        List<Integer> res = new LinkedList<>();
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                res.add(root.val);
                stack.addFirst(root.right);
                root = root.left;
            } else {
                root = stack.removeFirst();
            }
        }
        return res;
    }
}
