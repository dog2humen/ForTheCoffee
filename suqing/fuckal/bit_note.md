## 位运算相关运算

- 基本位运算: 左移<<, 右移>>, 按位或|, 按位与&, 按位异或^, 按位取反~
- 常用位运算:
    - 判断奇偶(取最低位): x & 1 == 1(奇), x & 1 == 0(偶)
    - 清零最低位的1: x = x & (x - 1) 
    - 得到最低位的1: res = x & ~x
    - x & -x = 0
- 异或的一些操作:
    - x ^ 0 = x
    - x ^ 1s = ~ x (1s = ~0)
    - x ^ ~x = 1s
    - x ^ x = 0
    - 交换两个数a, b: c = a ^ b, a ^ c = b, b ^ c = a
    - 结合律: a ^ b ^ c = (a ^ b) ^ c = a ^ (b ^ c)

- 指定二进制位的常用操作:
    - 将x最右边的n位清零: x & (~0 << n)
    - 获取x的第n位的值: (x << n) & 1
    - 获取x的第n位的幂值: x & (1 << (n - 1))
    - 仅将第n位置变为1: x | (1 << n)
    - 仅将第n位置变为0: x & (~(1 << n))
    - 将x的最高位到第n位置清零: x & ((1 << n) - 1)
    - 将第n位至第0位清零: x & (~((1 << (n + 1) - 1))