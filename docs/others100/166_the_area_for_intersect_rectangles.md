# 166 矩形相交的面积

## 题目描述

给出3组点坐标(x , y , w , h)，-1000 <x, y<1000，w, h为正整数。

(x , y , w , h)表示平面直角坐标系中的一个矩形:

- x, y为矩形左上角坐标点，w, h 向右 w，向下 h。

- (x, y, w, h)表示x轴(x, x+w)和y轴(y, y-h)围成的矩形区域;。

- (0, 0, 2, 2)表示×轴(0, 2)和y轴(0, -2)围成的矩形区域;。

- (3, 5, 4, 6)表示×轴(3, 7)和y轴(5, -1)围成的矩形区域;

  

求3组坐标构成的矩形区域重合部分的面积。

## 输入描述

3行输入分别为3个矩形的位置，分别代表"左上角x坐标"，“左上角y坐标”，“矩形宽”，“矩形高”

-1000 <= x, y <1000


## 输出描述

输出3个矩形相交的面积，不相交的输出0。


## 示例描述
### 示例一

**输入：**

```python
1 6 4 4
3 5 3 4
0 3 7 3
```

**输出：**

```
2
```

**说明：**

给定3个矩形A，B，C

A:左上角坐标(1,6)，宽4，高4

B:左上角坐标(3,5)，宽3，高4

C:左上角坐标(0,3)，宽7，高3



## 解题思路
**基本思路：**

相交区域一定是由矩形组成的左上坐标和右下坐标围成的最小面积，如何最小化面积？找每个坐标的最小或最大值即可。

最小值让右边和上面的点矩形尽量往左边和下面靠，最大值让左边和下面的点尽量往上面和右边靠。

## 解题代码

```python
def solve_method(s1, s2, s3):
    areas = [s1, s2, s3]
    new_points = []
    # 输入字符串，转化为整数坐标
    # 后面两个坐标转化成正常值（变成右下角）
    for area in areas:
        x, y, w, h = list(map(int, area.split()))
        new_points.append([x, y, x+w, y-h])
    
    # 初始化一个空的相交区域为原点，记录它的左上角和右下角的坐标值
    inter_area = []
    
    # 这里我们将所有的area，每个坐标通过zip函数分别集合到一起
    # 比如三个area的左上x，左上y，右下x，右下y
    # 然后我们找左上x里的较大值（注意坐标系左负右正，上正下负），即靠右，能满足最小的矩形
    #         找左上y里的较小值，即靠下
    #         找右下x里的较小值，即靠左
    #         找右下y里的较大值，即靠上
    # 这四个极值找到后就是重叠区域的左上和右下坐标
    for ind, coro in enumerate(zip(*new_points)):
        if ind == 0 or ind==3:
            inter_area.append(max(coro))
        if ind == 1 or ind==2:
            inter_area.append(min(coro))
    # print((inter_area[0], inter_area[1]), (inter_area[2], inter_area[3]))
    
    # 右下x一定大于左上x，左上y一定大于右下x,否则不存在相交区域
    # 如果不相交，也会求取一个面积，为他们最近点围成的面积
    if (inter_area[2]-inter_area[0])<=0 or (inter_area[1]-inter_area[3])<=0:
        return 0
    else:
        return (inter_area[2]-inter_area[0])*(inter_area[1]-inter_area[3])


if __name__ == '__main__':
    assert solve_method("1 6 4 4", "3 5 3 4", "0 3 7 3") == 2 # 相交，面积为2
    assert solve_method("2 0 2 2", "0 2 2 2", "4 2 2 2") == 0 # 不相交，面积为0
    assert solve_method("1 7 2 2", "4 2 2 2", "8 7 2 2") == 0 # 不相交，面积为15

```


