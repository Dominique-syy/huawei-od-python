# coding:utf-8

# def solveMethod(tag:str,source:str)->None:
#     p=0
#     # ����ɨ��
#     while p < len (source):
#         # ȡ�ַ�����0~1λ���ϵ�
#         curTag = source[p:p + 2]
#         # ��Ϊ��С��������Ҫ�����ƴ��
#         lenHEX = source[p + 6:p + 8] + source[p + 3:p + 5]
#         # ת��Ϊʮ����
#         lenDEC = int(lenHEX,16)
#         # �ж�ƥ��tag
#         if tag == curTag:
#             # ȡ������lenDEC��λ�õ��ַ�
#             value = source[p +9: p +9 + lenDEC * 3]
#             print(value)
#         p += 9 + lenDEC * 3

# if __name__ == '__main__':
#     tag = input()
#     source = input()
#     solveMethod(tag,source)

# �Ľ���
def solveMethod(tag:str,source:str)->None:
    p=0
    # ����ɨ��
    while p < len (source):
        # ȡ�ַ�����0~1λ���ϵ�
        curTag = source[p]
        # ��Ϊ��С��������Ҫ�����ƴ��
        lenHEX = source[p+2] + source[p+1]
        # ת��Ϊʮ����
        lenDEC = int(lenHEX,16)
        # �ж�ƥ��tag
        if tag == curTag:
            # ȡ������lenDEC��λ�õ��ַ�
            value = source[p +3: p +3 + lenDEC]
            print(' '.join(value))
        p += 3 + lenDEC

if __name__ == '__main__':
    tag = input()
    source = input().split(" ")
    solveMethod(tag,source)