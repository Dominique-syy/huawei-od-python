import sys

score =0
#         �������� ���� ���б� ��������λ��
def combine(ints,n,lst,index):
    global score
    # �ų�����С������Ϊ0ʱ����0�����Ӧλ�ã��������÷֣�
    if n <=0:
        # ����ֻ��ִ��һ��(�İ�)��ר�Ŵ���Ϊ0�����
        if n ==0:
            for i in range(len(lst)):
                ints[lst[i]]=0
            return True
    # ������ĩβ��ʼ��ǰ����
    for i in range(index,-1,-1):
        # �Ƿ����ֱ������ѭ��
        if n <0 or sum(ints)==0:
            break
        x = ints[i]
        if x ==0:
            continue
        lst.append(i)
        # �ݹ�
        if combine(ints,n-x,lst,i-1):
            count = sum(ints)
            if count ==0 or count % score !=0:
                break
            combine(ints,score,[],len(ints)-1)
        lst.pop()
    return sum(ints)==0

if __name__ == "__main__":
    t = int(input())
    p = input().split()
    # ȡ�����η���
    ints = [int( p[i] ) for i in range(t)]

    # �����ܷ�
    count = sum(ints)
    # ���������
    ints.sort()
    # �����ĵ���������Ϊ����
    min_score = ints[t -1]

    res =0
    # �����޵����ޱ������п��ܷ���
    for i in range(min_score,count //2):
        # ����������ʱ
        if count % i==0:
            score = i
            if combine(ints,score,[],t-1):
                res = score
                break
    print(count if res ==0 else res)