# 144 比赛的冠亚军

## 题目描述

有N（3＜＝N＜10000）个运动员，他们的id为0到N—1，他们的实力由一组整数表示。他们之间进行比赛，需要决出冠亚军。比赛的规则是0号和1号比赛，2号和3号比赛，以此类推，每一轮，相邻的运动员进行比赛，获胜的进入下一轮，实力值大的获胜，实力值相等的情况，id小的情况下获胜，轮空的直接进入下一轮。

默认季军为输给冠军的选手，如果半决赛不足四人，冠军直接战胜亚军，那么季军为输给亚军的选手。



## 输入描述

输入一行N个数字代表N的运动员的实力值（0＜＝实力值＜＝10000000000）。



## 输出描述

输出**冠、亚**、**季**的id，用空格隔开。



## 示例描述

### 示例一

**输入：**

```text
2 3 4 5
```

**输出：**

```text
3 1 2
```

**说明：**  

第一轮比赛，id为0 实力值为2的运动员和id为1 实力值为3的运动员比赛，1号胜出进入下一轮争夺冠亚军；

id为2的运动员和id为3的运动员比赛，3号胜出进入下一轮争夺冠亚军；

冠亚军比赛，3号胜1号；2号运动员是在冠亚军之前输给冠军3号的，所以季军是2号。

冠、亚、季军id分别为3、1、2。




## 解题思路

**基本思路：** 

1. 这道题的有趣之处在于，我们不能直接使用多键值排序和`sorted方法`，因为这种赛制下，亚军、季军不一定是实力第二、第三的运动员。
2. 因此，我们可以用`模拟法`，按照题目描述，一轮一轮地模拟比赛过程，确定冠亚季军。

- 首先确定，两两比赛需要多少轮？ 运动员两两比赛，那就取以2为底的对数，最后向上取整；但是Python可以用`int(浮点数)`来简单地对一个数向下取整，所以可以用以下地公式来求比赛轮次：

$$
epoch=\lceil log_2(players) \rceil=\lfloor log_2(players-1) \rfloor +1
$$

- 在每一轮，我们该怎么模拟运动员的胜利和失败？

我们可以用列表`rank`表示目前还未淘汰的运动员。然后遍历每个运动员，`运动员rank[i]`需要和`身边的运动员rank[i+1]`比拼；如果`运动员rank[i]`身旁没人（也就是他轮空，`i==len(rank)-1`），他直接算作这一轮的胜利者。

显然，我们在比赛过程中需要记录这一轮的胜利者，所以可以用`列表win`来记录`每一轮的胜利者`。

因为我们最后要输出亚军、季军（他们是和冠军争夺的失败者），在记录胜利者的同时，我们也可以记录`目前为止产生的失败者`，使用`列表lose`记录。

- 此外，我们可以记录半决赛（四强）时的决赛对阵情况，便于我们更方便地找到季军。

## 解题代码

```python
def solve_method(strengh: List[int]) -> str:
    nums = len(strengh)
    rank = list(range(0, nums))  # 初始顺序, 代表还要比赛的选手
    win = []  # 每一轮的胜者
    lose = []  # 和已经产生的失败者
    semi_final = {}  # 半决赛 对阵情况(便于输出季军)
    # 需要比较的轮次：n= log2(nums)的向上取整=log2(nums-1)向下取整+1
    n = int(math.log2(nums - 1)) + 1

    # 模拟法；模拟运动员两两比赛的过程，需要比赛n轮
    for epoch in range(0, n):
        # 如果还需比赛的选手不足 4人(半决赛)，为了便于输出季军，保存此时他们的对阵情况
        if 3 <= len(rank) <= 4:
            semi_final = {rank[0]: rank[1], rank[1]: rank[0]}
            if len(rank) == 4:
                semi_final.update({rank[2]: rank[3], rank[3]: rank[2]})

        # while 循环模拟每一轮比赛
        win.clear()
        i = 0
        while i < len(rank):
            player_id = rank[i]

            # 轮空的直接进入下一轮
            if i == len(rank) - 1:
                win.append(player_id)
                i += 1

            # 和相邻的比较
            else:
                neighbor_player = rank[i + 1]
                if strengh[player_id] >= strengh[neighbor_player]:
                    win.append(player_id)
                    lose.append(neighbor_player)
                else:
                    win.append(neighbor_player)
                    lose.append(player_id)
                # 同时处理了2个运动员;
                i += 2

        # 本轮胜出的选手参加下一轮比赛
        rank = win[:]

    # 循环终止时,rank[]里只包含冠军的id,lose[]的倒数第一位是亚军
    # 季军可以用之前的 semi_final 字典找到
    champion = rank[0]
    second_player = lose[-1]
    third_player = semi_final.get(champion, semi_final.get(second_player))
    ret = [str(champion), str(second_player), str(third_player)]
    return " ".join(ret)
```