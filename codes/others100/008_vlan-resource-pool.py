# ȥ����β�հ��ַ�
input_str = input().strip()
request = int(input().strip())

# ������ ���
input_list = input_str.split(",")
result_set = set()

for i in input_list:
    # �ж��Ƿ���� "-"
    if "-" in i:
        # �� - ���˲��ת����
        start,end = map(int,i.split("-"))
        # �������
        for j in range(start,end +1):
            result_set.add(j)
    else:
        # �����ַ�ֱ�����
        result_set.add(int(i))

# ���б���ɾ��ָ��Ԫ��
result_set.remove(request)
# ת��Ϊ�б�
result_list = list(result_set)
# ��������
result_list.sort()

# ȷ����ʼ
start = result_list[0]
last = start
output_list = []

# �ӵڶ���Ԫ�ؿ�ʼ����
for i in range(1,len(result_list)):
    cur = result_list[i]
    # ���cur����last�ĺ���Ԫ��
    if cur == last +1:
        # ����β��
        last = cur
    else:
        # ����start��last��Ԫ����ӽ�output_list����
        output_list.append((start,last))
        # ������ʼ
        start = last = cur
# ��ʣ�µļ���
output_list.append((start,last))

# ʹ���б��Ƶ�ʽ����һ���ַ����б� output_str
# ��ʹ�� ",".join(output_str) �����Զ���Ϊ�ָ����������ӳ�һ���ַ�����
# �б��Ƶ�ʽ����ݷ�ΧԪ�� (start, last) �Ƿ���ȣ�
# ʹ�ò�ͬ�ĸ�ʽ���и�ʽ��
output_str =",".join(["{}-{}".format(i,j) if i!=j else "{}".format(i) for i,j in output_list])
print(output_str)