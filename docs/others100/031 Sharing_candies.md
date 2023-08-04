# 031 分糖果

## 题目描述

小明从糖果盒中随意抓一把糖果  

每次小明会取出一半的糖果分给同学们  

当糖果不能平均分配时

小明可以从糖果盒中(假设盒中糖果足够)取出一个或放回一个糖果

小明至少需要多少次(取出放回和平均分配均记一次)能将手中糖果分至只剩一颗

## 输入描述

抓取糖果数(小于 `1000000` )，例如 15

## 输出描述

最少分至一颗糖果的次数，例如 5

## 示例描述

### 示例一

**输入：**

```Plain Text
15
```

**输出：**

```Plain Text
5
```

**说明：
解释：**

1. 15+1 =16

2. 16/2 = 8

3. 8/2 = 4

4. 4/2 = 2

5. 2/2 = 1

## 解题思路

**基本思路：** 采取递归的方式计算放回或取出的次数

1. 当x=2时，返回1

2. 当x为偶数时，x除以2进行计算，返回的结果+1

3. 当x为奇数时，(x+1)或(x-1)计算，返回结果+1，最后选择最少的次数

4. 返回最后的结果

## 解题代码

```Python
def solve(x: int):
    if x > 1000000:
      return False
    # 当x=2时，返回1
    if x == 2:
        return 1  
    # 当x为偶数时
    if x % 2 == 0:
        return solve(x // 2) + 1  
    # 当x为奇数时
    else:
        return min(solve(x + 1) + 1, solve(x - 1) + 1)
 
 
if __name__ == "__main__":
    n = int(input()) 
    result = solve(n)
    print(result)
```
