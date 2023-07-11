# coding: gbk
# Ҫ���ñ���
n = int(input()) #��������

lights = []

for x in range(n):
    # input��ȡ�û������ʹ��split���ո�ָ���һ���ַ����б���ͨ��map��ÿ��Ԫ��ӳ�������
    input_data = list(map(int, input().split()))
    # ���������ν����б��Ԫ������
    id = input_data[0]
    x1 = input_data[1]
    y1 = input_data[2]
    x2 = input_data[3]
    y2 = input_data[4]
    # ��id,xy�����ƽ��ֵ������Ĳ�ֵһ�루Ҳ���ǵ��ݵĿ�뾶����ϳ�һ��������ѹ��lights��
    lights.append([id, (x1 + x2)//2, (y1 + y2)//2,(x2-x1)//2])

# �������ú�����������
# ע��lambda ��һ����Python�����ڴ������������Ĺؼ��֡�
#   ����������һ��û�����Ƶĺ�����ͨ�����ڱ�д��̵Ĺ��ܴ��롣
# �÷���
#   ��lambda arguments: expression
#       arguments �Ǻ����Ĳ�����������һ��������
#       expression �Ǻ���ִ�еı��ʽ��Ҳ���������������������ص�ֵ
# ���������������������ʵ���൱�� 
# def key(a): 
#   a[2] # ����������ĵ���������
# �������������Ĳ�����a���飬��lights�����key��lights��ÿ������ĵ�����Ԫ�أ�Ҳ����y�����ƽ��ֵ
# ʹ��lights�е�Ԫ�����ΰ�y�����д�С��������
lights.sort(key=lambda a: a[2])

# ����������lights����

result = []
# ÿһ�е���ʼ����
row_start_index = 0
for i in range(1,n):
    # Ҫ�������Ƹߵ�ƫ������ư뾶��ͬһ��
    # �ж�y����֮��Ҳ���ǵƸ߶Ȳ��Ƿ�С�ڵƵİ뾶
    # ����������ʾ���µ�һ����
    if lights[i][2] - lights[row_start_index][2] > lights[row_start_index][3]:
        # ����ʼ��row_start_index����ǰ��i�����б�������򣬰���ÿ��Ԫ��� x �����������
        lights[row_start_index:i] = sorted(lights[row_start_index:i],key=lambda a:a[1])
        # ʹ���б��Ƶ�ʽ����ʼ�е���ǰ�е� id �����б���ӵ� result �б��У��������£�
        #   ���б� lights[row_start_index:i] �е�ÿ��Ԫ�� light
        #   ȡ�����еĵ�һ��Ԫ�أ�������ЩԪ�����һ���µ��б�
        result.extend([light[0] for light in lights[row_start_index:i]])
        # ������ʼ�е���������������Ϊ��ǰ�е�����
        row_start_index = i
# ��Ϊ�����һ��ifһֱ�̵���ȥ�����Եö�ʣ�µ����������β����
lights[row_start_index:n] = sorted(lights[row_start_index:n],key=lambda a:a[1])
result.extend([light[0]for light in lights[row_start_index:n]])

# ���б� result �е�Ԫ��ת��Ϊ�ַ���������������������
print(' '.join(map(str,result)))