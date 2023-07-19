# coding:utf-8
import collections
def solve_method(ints):
    # �����洢ÿ�����ֵ�Ƶ��
    map = collections.defaultdict(int)
    for pair in ints:
        for i in range(pair[0],pair[1] + 1):
            map[i] += 1
    # ����һ����Ԫ����ɵ��б�ÿ��Ԫ�����һ�����ֺ�����Ƶ��
    list = [(k,v) for k,v in map.items()]
    # �������ֵ�Ƶ�ʶ��б���н�������
    list.sort(key=lambda x:x[1],reverse=True)
    print(list[0][0])

if __name__ =="__main__":
    n = int(input().strip())
    ints = [list(map(int,input().strip().split())) for _ in range(n)]
    solve_method(ints)