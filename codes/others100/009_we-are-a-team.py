# coding:utf-8
import sys
# ��ȡ����һ�в��ָ�ת��Ϊ������ֵ��n��m
n,m = map(int,sys.stdin.readline().split())
# ��ϵ����
relationship_sets = []
# ����֤�Ĺ�ϵ
verify_relationships = []
# ��ȡm��
for i in range(m):
    relationship = sys.stdin.readline().strip().split()
    # �����ֵ
    x,y,relation = map(int,relationship)
    # ������0֤��Ҫ��֤
    if relation != 0:
        verify_relationships.append(relationship)
    else:
        set_added = False
        for j in range(len(relationship_sets)):
            # ȡ����ϵ�����е�ÿ��set
            set_ = relationship_sets[j]
            # ֻ��Ҫ�ж�����һ���Ƿ�������
            if x in set_ or y in set_:
                # ����ü���
                set_.add(x)
                set_.add(y)
                set_added = True
                break
        # �����������ⴴ���µļ��ϲ���xy����
        if not set_added:
            new_set = set()
            new_set.add(x)
            new_set.add(y)
            relationship_sets.append(new_set)
 # �������֤�ļ���
for i in range(len(verify_relationships)):
    relationship = verify_relationships[i]
    x,y,relation = map(int,relationship)
    if relation != 1:
        print("da pian zi")
        continue
    is_team = False
    for j in range(len(relationship_sets)):
        set_=relationship_sets[j]
        if x in set_ and y in set_:
            print("we are a team")
            is_team = True
            break
    if not is_team:
        print("we are not a team")