# coding: utf-8

def solve_method(ip:str):
    # ��#�ָ��ַ���
    strings = ip.split("#")
    # ��ȡ����
    length = len(strings)
    count = 0
    # ��Ϊ�Ϸ�
    is_valid = True
    # ���ȸ��ַ���������С��
    if length == 4:
        for i in range(length):
            # ȡ��ÿһ����
            n = int(strings[i])
            # ��һ������ȡֵ��Χ��1~128
            if i==0 and (n < 1 or n > 128):
                is_valid = False
                break
            # ��������λ���ϵķǷ�
            elif n < 0 or n > 255:
                is_valid = False
                break
            # �����ɵó�һ����ֵ��Ӧ��λʮ��������Ҳ���ǰ�λ��������
            # λ�������ƣ�3-i������λ
            count+=n<<(8*(3-i))
    else:
        is_valid = False
    if is_valid:
        print(count)
    else:
        print("invalid IP")

if __name__ =='__main__':
    ip = input()
    solve_method(ip)