# 180 统计监控

## 题目描述

在一长方形停车场内，每个车位上方都有对应监控器，当且仅当在当前车位或者前后左右四个方向任意一个车位范围停车时，监控器才需要打开，给出某一时刻停车场的停车分布，请统计最少需要打开多少个监控器。



## 输入描述

第一行输入m,n表示长宽，满足1<m,n <=20

后面输入m行，每行有n个0或1的整数，整数间使用一个空格隔开，

表示该行已停车情况，其中0表示空位，1表示已停。



## 输出描述

最少需要打开监控器的数量。



## 示例描述

### 示例一

**输入：**

```text
3 3
0 0 0
0 1 0
0 0 0
```



**输出：**

```text
5
```

### 示例二

**输入：**

```text
3 3
1 0 0
0 1 0
0 0 0
```



**输出：**

```text
6
```





## 解题思路

**基本思路：**

一遍广度优先搜索就行了

1. 查找出所有汽车停车的位置，先count+1安上监控
2. 对每个汽车周围进行一次广度优先遍历，安上监控count+1，已经安上监控的或者停着车的位置跳过。

## 解题代码

```python
def solve_method(m,n,nums):
    count = 0
    # 查找出所有停车位位置，先count+1安上监控
    cars = []
    for i in range(m):
        for j in range(n):
            if nums[i][j]==1:
                count+=1
                cars.append((i,j))
    # 对每个汽车周围进行一次广度优先遍历，安上监控
    while cars:
        i, j = cars.pop()
        for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0<=x<m and 0<=y<n and nums[x][y]==0:
                count+=1
                nums[x][y]=1
    return count


if __name__ == '__main__':
    assert solve_method(3,3,[[0, 0, 0],[0, 1, 0],[0, 0, 0]]) == 5
    assert solve_method(3,3,[[1, 0, 0],[0, 1, 0],[0, 0, 0]]) == 6
```


