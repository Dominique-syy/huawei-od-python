def solve_method(num):
    # ����ռ��ϴ洢����
    factors=set()
    tmp = num
    # ��ʼ����Ϊ2
    f = 2
    while tmp != 1:
        # �ж�tmp�Ƿ��ܱ�f����
        if tmp % f != 0:
            # �������1
            f+=1
        else:
            # ���������������Ӽ���set��
            factors.add(f)
            # ����
            tmp //f
    # ˫��ѭ���ж��������ӳ˻��Ƿ�Ϊnum
    for f1 in factors:
        for f2 in factors:
            if f1 * f2 == num:
                min_factor = min(f1,f2)
                max_factor = max(f1,f2)
                # ��ʽ�����
                print(f"{min_factor}{max_factor}")
                return
    print("-1 -1")

if __name__ == "__main__":
    num = int(input())
    solve_method(num)