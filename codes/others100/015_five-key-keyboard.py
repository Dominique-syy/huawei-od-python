def solve_method(nums):
    # ������������ַ����ָ���б�
    nums_list = nums.split(" ")
    # ��ʼ������ builder��select �� copy
    builder = ""
    select = ""
    copy = ""
    # ���������б�
    for op in nums_list:
        if op == "1":
            # ִ�в���1����� select������ builder ����� 'A'
            select = empty(builder, select)
            builder += 'A'
        elif op == "2":
            # ִ�в���2������ select ��ֵ�� copy
            if select != "":
                copy = select
        elif op == "3":
            # ִ�в���3����� select��builder �� copy ��ֵ
            if select != "":
                copy = select
                select = ""
                builder = ""
        elif op == "4":
            # ִ�в���4����� select������ builder ����� copy ��ֵ
            select = empty(builder, select)
            builder += copy
        elif op == "5":
            # ִ�в���5���� builder ��ֵ���� select
            if len(builder) != 0:
                select = builder
        else:
            pass
    # ��� builder �ĳ���
    print(len(builder))

def empty(builder, select):
    # ��� select �� builder �е�ֵ������ select ��Ϊ���ַ���
    if select != "":
        builder = builder.replace(select, "")
        select = ""
    return select

def main():
    # ��ȡ����������ַ��������� solve_method �������д���
    nums = input()
    solve_method(nums)

if __name__ == '__main__':
    main()
