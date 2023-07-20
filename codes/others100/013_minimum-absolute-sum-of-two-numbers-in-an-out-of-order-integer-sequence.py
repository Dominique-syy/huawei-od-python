# coding: utf-8
import sys

def solve_method(nums_str):
    # ������������ַ���ת��Ϊ�����б�
    nums = list(map(int, nums_str.split()))
    # ȥ���ظ�������
    nums = list(set(nums))
    # ��ʼ����С��Ϊϵͳ���ֵ
    min_sum = sys.maxsize
    # ��ʼ���������
    res_set = set()
    # ���������б�
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            a, b = nums[i], nums[j]
            if a != b:
                # ���㵱ǰ�������ֵľ���ֵ��
                cur_sum = abs(a + b)
                if cur_sum < min_sum:
                    # �����ǰ��С����С�ͣ��������С�ͺͽ������
                    min_sum = cur_sum
                    res_set = set([a, b])
    # ���������ϲ�Ϊ�գ��������������е����ֺ���С��
    if len(res_set) != 0:
        print(*res_set, min_sum)

if __name__ == "__main__":
    # ���������ַ��������� solve_method �������д���
    nums_str = input()
    solve_method(nums_str)