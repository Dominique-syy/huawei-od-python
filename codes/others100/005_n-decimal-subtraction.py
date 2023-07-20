import string

# x����ת��n
def f35(n,x):
    # ���Ƿ�
    if x < 2 or x > 35 or x > n:
        return 'ERROR'
    
    # 0-9������
    lil = [i for i in range(10)]
    # ��������ASCII��ĸ
    li2 = list(string.ascii_letters)
    li3=['@','_']

    # ȫƴ��һ��
    li = lil + li2 + li3
    result =''
    # һ������ѭ��
    while True:
        # ������x�����µ���
        m = n //x
        # ��������
        r = n % x 
        # ˵��ת���Ѿ�������ֻʣ��һ����λ����
        if n < x:
            # ȡ��li����������Ϊn��Ԫ������resultƴ�Ӻ�����ѭ��
            result = str(li[n]) + result
            break
        # ����ƴ��
        result = str(li[r])+result
        # ����
        n = m
    return result

# ��num���n���Ƶ��ַ�����ת��Ϊʮ������
def any_to_decimal(num,n):
    # �����ֵ䣺ÿ���ַ���Ӧ��ʮ������
    baseStr = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19}
    new_num = 0
    # num���ȼ�һ�����λ���ݴη�
    nNum = len(num)-1
    for i in num:
        # ����n��nNum�η�
        new_num = new_num + baseStr[i] * pow(n,nNum)
        # �ݼ�һ
        nNum = nNum-1
    return new_num

def solve_method(line):
    split = line.split(" ")
    # ���ڶ�������Ԫ��
    if check(split[1]):return
    if check(split[2]):return
    # ���б��һ��ת��Ϊ���������ƣ�
    radix = int(split[0])
    # ��������radix����ת��Ϊʮ����
    minuend = any_to_decimal(split[1],radix)
    # ����
    subtrahend = any_to_decimal(split[2],radix)

    diff = int(minuend)-int(subtrahend)
    # �������
    sign = 0 if diff >=0 else 1
    # �������ֵ
    value = abs(diff)

    print("%d %s"%(sign,f35(value,radix)))

def check(str):
    # �ַ������ȴ���1����0��ͷʱ
    if len(str)>1 and str.startswith("0"):
        print(-1)
        return True
    # ���������쳣
    return False

line = input().strip()
solve_method(line)