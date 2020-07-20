## 7月leetcode每日一题

| 题目| enName | 序号| 链接 |
| :---: | :---: | :---: | :---: |
| 有序矩阵中第K小的元素 | kth-smallest-element-in-a-sorted-matrix | 378 | [link](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/) |
| 将有序数组转换为二叉搜索树 | convert-sorted-array-to-binary-search-tree | 108 | [link](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/) |
| 最长有效括号 | longest-valid-parentheses | 32 | [link](https://leetcode-cn.com/problems/longest-valid-parentheses/) |
| 最长重复子数组 | maximum-length-of-repeated-subarray | 718 | [link](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/) |
| 通配符匹配 | wildcard-matching | 44 | [link](https://leetcode-cn.com/problems/wildcard-matching/) |
| 不同路径 II | unique-paths-ii | 63 | [link](https://leetcode-cn.com/problems/unique-paths-ii/) |
| 路径总和 | path-sum | 112 | [link](https://leetcode-cn.com/problems/path-sum/) |
| 跳水板 | diving-board-lcci | 面试题16.11 | [link](https://leetcode-cn.com/problems/diving-board-lcci/) |
| 恢复空格 | re-space-lcci | 面试题17.13 | [link](https://leetcode-cn.com/problems/re-space-lcci/) |
| 最佳买卖股票时机含冷冻期 | best-time-to-buy-and-sell-stock-with-cooldown | 309 | [link](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |
| 计算右侧小于当前元素的个数 | count-of-smaller-numbers-after-self | 315 | [link](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/) |
| 地下城游戏 | dungeon-game | 174 | [link](https://leetcode-cn.com/problems/dungeon-game/) |
| 两个数组的交集 II | intersection-of-two-arrays-ii | 350 | [link](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/) |
| 三角形最小路径和 | triangle | 120 | [link](https://leetcode-cn.com/problems/triangle/) |
| 不同的二叉搜索树 | unique-binary-search-trees | 96 | [link](https://leetcode-cn.com/problems/unique-binary-search-trees/) |
| 判断二分图 | is-graph-bipartite | 785 | [link](https://leetcode-cn.com/problems/is-graph-bipartite/) |
| 搜索插入位置 | search-insert-position | 35 | [link](https://leetcode-cn.com/problems/search-insert-position/) |
| 交错字符串 | interleaving-string | 97 | [link](https://leetcode-cn.com/problems/interleaving-string/) |
| 戳气球 | burst-balloons | 312 | [link](https://leetcode-cn.com/problems/burst-balloons/) |
| 两数之和 II - 输入有序数组 | two-sum-ii-input-array-is-sorted | 167 | [link](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) |



### 动态规划系列
#### 最长公共子串, 最长公共子序列系列
参考一下文章理解: [link](https://mp.weixin.qq.com/s/XJyujBI5nofVE9CUbStemA)
#### 股票买卖系列
参考一下文章理解: [link](https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/tuan-mie-gu-piao-wen-ti)

### 关于字典树(Trie树)
- 基本结构: 字典树是一种树形结构.典型应用是用于统计和排序大量的字符串(但不仅限于字符串), 经常被搜索引擎用于文本词频统计.
- 优点: 最大限度的减少无谓的字符串比较, 查询效率比哈希表高
- 基本性质:
 - 结点本身不存完整单词
 - 从根结点到某一结点, 路径上经过的字符连接起来, 为该结点对应的字符串
 - 每个结点的所有子结点路径代表的字符都不相同
- 核心思想:空间换时间, 利用字符串公共前缀来降低查询时间
- 实现: 请参照右边连接[link](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
