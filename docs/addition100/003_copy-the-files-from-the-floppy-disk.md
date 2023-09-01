# 003 通过软盘拷贝文件 

## 题目描述

有一名科学家想要从一台古董电脑中拷贝文件到自己的电脑中加以研究。但此电脑除了有一个3.5寸软盘驱动器以外，没有任何手段可以将文件持贝出来，而且只有一张软盘可以使用。因此这一张软盘是唯一可以用来拷贝文件的载体。科学家想要尽可能多地将计算机中的信息拷贝到软盘中，做到软盘中文件内容总大小最大。

已知该软盘容量为1474560字节。文件占用的软盘空间都是按块分配的，每个块大小为512个字节。一个块只能被一个文件使用。拷贝到软盘中的文件必须是完整的，且不能采取任何压缩技术。

## 输入描述

第1行是一个整数`N`，表示计算机中的文件数量，取值范围是1 <= N <= 1000。

接下来的第2行到第`N+1`行（共`N`行），每行为一个整数，表示每个文件的大小`Si`，单位为字节。取值范围是0 <= i <= N、0 <= Si <= 1000000。

## 输出描述

科学家最多能拷贝的文件总大小。

**备注：** 

为了充分利用软盘空间，将每个文件在软盘上占用的块记录到本子上，即真正占用软盘空间的只有文件内容本身。

## 示例描述

### 示例一

**输入：**
```text
3
737270
737272
737288
```

**输出：**
```text
1474542
```

**说明：**  

3个文件中，每个文件实际占用的大小分别为737280字节、737280字节、737792字节。

只能选取前两个文件，总大小为1474542字节。虽然后两个文件总大小更大且未超过1474560字节，但因为实际占用的大小超过了1474560字节，所以不能选后两个文件。

### 示例二

**输入：**
```text
6
400000
200000
200000
200000
400000
400000
```

**输出：**
```text
1400000
```

**说明：**  

从6个文件中，选择3个大小为400000的文件和1个大小为200000的文件，得到最大总大小为1400000。

也可以选择2个大小为400000的文件和3个大小为200000的文件，得到的总大小也是1400000。

## 解题思路

**基本思路：** xxxxx（注：如果存在基本思路，可编写）

1. xxxxx
2. xxxxx
3. xxxxx
4. 返回结果。

## 解题代码