# coding:utf-8

def solve_method(n,jobs):
    # time��ʱ��
    # more����ʱ��
    time,more = 0, 0
    for i in jobs:
        # ��ǰ��������֮ǰ�ĳ�ʱʱ��ᳬ��ʱ��γ���
        if i + more > n:
            # �����Ĳ��ֱ����浽more��
            more =i+more -n
        else:
            # ��ǰ����û�г���ʱ��γ���
            more = 0
        # ����������
        time +=1
    # �����������ѭ��ִ������
    while more > 0:
        more -n
        time +=1
    print(time)

if __name__ == '__main__':
    n, length = map(int,input().split())
    jobs = list(map(int,input().split()))
    solve_method(n,jobs)




# n = int(input())
# len = int(input())
# l = list(map(int,input().split()))
# time,more=0,0
# for i in l:
#     if i+more > n:
#         more = i+more-n
#     else:
#         more = 0
#     time += 1
# while more > 0:
#     more -= n
#     time += 1
# print(time)