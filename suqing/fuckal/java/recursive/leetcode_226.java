package recursive;

import java.util.Deque;
import java.util.LinkedList;

public class leetcode_226 {
    public TreeNode invertTree(TreeNode root) {
//        return invertTree_v1(root);
        return invertTree_v2(root);

    }

    public TreeNode invertTree_v1(TreeNode root) {

        if (root != null) {
            TreeNode tmp;
            tmp = root.left;
            root.left = root.right;
            root.right = tmp;
            invertTree_v1(root.left);
            invertTree_v1(root.right);

        }
        return root;
    }

    public TreeNode invertTree_v2(TreeNode root) {
        Deque<TreeNode> stack = new LinkedList<>();
        TreeNode node = root;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                TreeNode tmp = root.left;
                root.left = root.right;
                root.right = tmp;
                stack.addFirst(root.right);
                root = root.left;
            } else {
                root = stack.removeFirst();
            }
        }

        return node;
    }
}
