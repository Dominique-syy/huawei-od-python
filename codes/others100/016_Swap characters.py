import sys

def solve_method(line:str)->None:
    # ��������ַ���ת��Ϊ�ַ��б� 
    chars = list(line)
    # ��ʼ����ʱ����Ϊ��һ���ַ�
    tmp = chars[0]
    # ��ʼ��λ�ñ���Ϊ0
    pos = 0
    for i in range(1,len(chars)):
        # �����ַ��б��е�ÿ���ַ�
        cur = chars[i]
        # �����ǰ�ַ�С�ڵ�����ʱ����
        if cur <= tmp:
            tmp = cur
            pos = i
    if pos != 0:
        # ����һ���ַ��ŵ�λ�ñ�����ָʾ��λ��
        chars[pos] = chars[0]
        # ����ʱ�����ŵ���һ��λ��
        chars[0] = tmp
    # ���ַ��б�ת��Ϊ�ַ��������
    sys.stdout.write("".join(chars))
def main():
    line = input().strip()
    solve_method(line)
if __name__ =="__main__":
    main()