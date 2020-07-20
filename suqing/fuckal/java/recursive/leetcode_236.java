package recursive;
import java.util.*;
public class leetcode_236 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return lowestCommonAncestor_v1(root, p, q);
    }

    public TreeNode lowestCommonAncestor_v1(TreeNode root, TreeNode p, TreeNode q) {
        // 找到从root到p的路径 path_p, 找到root到q的路径path_q, 然后遍历两个路径找最近公共祖先
        List<TreeNode> path_p = new ArrayList<>();
        List<TreeNode> path_q = new ArrayList<>();
        getPath(root, p, new LinkedList<>(), path_p);
        getPath(root, q, new LinkedList<>(), path_q);
        TreeNode res = null;
        int size_p = path_p.size();
        int size_q = path_q.size();
        int i = 0, j = 0;
        while (i++ < size_p && j++ < size_q) {
            if (path_p.get(i) == path_q.get(j)) {
                res = path_p.get(i);
            }
        }
        return res;

    }

    public void getPath(TreeNode node, TreeNode target, List<TreeNode> curPath, List<TreeNode> res) {
        if (node == null) {
            return ;
        }
        if (node == target) {
            res.addAll(curPath);
            res.add(node);
            return;
        }
        curPath.add(node);
        getPath(node.left, target, curPath, res);
        curPath.remove(curPath.size() - 1);
        curPath.add(node);
        getPath(node.right, target, curPath, res);
        curPath.remove(curPath.size() - 1);

    }
}