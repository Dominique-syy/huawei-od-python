# coding:utf-8
from typing import List
def solve_method(line:str)->None:
    # �����ַ����� �������ָ�
    split1 = line.split(";")
    right = True
    error_list:List[int] = []
    # ������һ����������
    limits = split1[-1].split(",")
    # �����ڶ���Ŀ��ֵ
    aims = split1[-2].split(",")
    # ���������ı���
    vars_=split1[-3].split(",")
    # ���������м���ʽ�Ӿ��м���
    for i in range(len(limits)):
        value =0
        # ��Ŀ��ֵת��Ϊ����
        aim = float(aims[i])
        #ϵ��
        split_=split1[i].split(",")
        for j in range(len(split_)):
            # ϵ���˱���
            value += float(split_[j]) * int(vars_[j])
        limit = limits[i]
        # ȡ���Բ�ֵ
        e = int(abs(value - aim))
        # ƥ����������
        if limit ==">":
            right = (value > aim) and right
            error_list.append(e)
        elif limit == "<":
            right = (value < aim) and right
            error_list.append(e)
        elif limit ==">=":
            right = (value >= aim)and right
            error_list.append(e)
        elif limit =="<=":
            right = (value <= aim)and right
            error_list.append(e)
        else:
            right = False
    print(right,max(error_list))

line = input()
solve_method(line)