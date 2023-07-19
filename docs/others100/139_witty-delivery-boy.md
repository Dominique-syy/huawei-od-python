# 139 机智的外卖员

## 题目描述

外卖员每天在大厦中送外卖，大厦共有`L`层（0 < L <= 10^5），当他处于第`N`层楼时，可以每分钟通过步行梯向上达到`N+1`层，或向下达到`N - 1`层，或者乘坐电梯达到`2*N`层。

给定他所在位置`N`，以及外卖配送的目的楼层`M`，计算他送达的最短时间。

## 输入描述

当前所处楼层`N`和外卖配送的目的楼层`M`。

## 输出描述

送达的最短时间。

## 示例描述

### 示例一

**输入：**
```text
5 17
```

**输出：**
```text
4
```

## 解题思路

**基本思路：** 使用动态规划方法解题。
1. 动态规划步骤：
    - 确定dp数组以及下标的含义：dp[i]的定义是到达第i层楼的最短时间。
    - 确定递推公式：
        - 当i为偶数时，从上一层步行到达这一层，耗时+1或乘坐电梯到达这一层，耗时+1，则公式为`dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)`
        - 当i为奇数时，从上一层步行到达这一层，耗时+1或乘坐电梯再向下走一层，耗时+2，则公式为`dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)`
    - dp数组初始化：大于`N`楼层的值初始化为0，小于`N`楼层的值从1递增。
    - 确定遍历顺序：从`N+1`到`M+1`
    - 举例推导dp数组：当N为5时
        - 前4层楼的最短时间分别为4、3、2、1
        - 第6层楼的最短时间为`min(1, 3) = 1`
        - 第7层楼的最短时间为`min(2, 2) = 2`
2. 返回到达第`M`楼的最短时间`dp[M]`    


## 解题代码

```python
def solve_method(N, M):
    if N >= M:
        return 0

    dp = [0] * (M + 1)
    # 向下步行需要花费的时间
    for i in range(N + 1):
        dp[i] = N - i
    for i in range(N + 1, M + 1):
        if i % 2 == 0:
            # 从上一层步行到达这一层，耗时+1
            # 坐电梯到达这一层，耗时+1
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            # 从上一层步行到达这一层，耗时+1
            # 乘坐电梯再向下走一层，耗时+2
            dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)

    return dp[M]
```