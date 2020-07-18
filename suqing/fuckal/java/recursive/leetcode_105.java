package recursive;

import javax.swing.*;
import java.util.Arrays;
import java.util.stream.IntStream;

public class leetcode_105 {

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // 前序和中序序列构造bst
        // preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        // 从preorder选择根,
        // 根据根划分下次递归的区间
        return helper(preorder, inorder, 0, 0, inorder.length - 1);
    }

    public TreeNode helper(int[] preorder, int[] inorder, int pStart, int iStart, int iEnd) {

        if (pStart > preorder.length - 1 || iStart > iEnd) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[pStart]);
        int inorderIdx = 0;
        for (int i = iStart; i <= iEnd; i++) {
            if (inorder[i] == root.val) {
                inorderIdx = i;
            }
        }

        root.left = helper(
                preorder,
                inorder,
                pStart + 1,
                iStart,
                inorderIdx - 1
        );

        root.right = helper(
                preorder,
                inorder,
                pStart + inorderIdx - iStart + 1,
                inorderIdx + 1,
                iEnd

        );
        return root;
    }
}

