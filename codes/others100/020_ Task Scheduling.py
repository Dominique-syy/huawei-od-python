# coding:utf-8
import sys
task_list = []
while True:
    line = sys.stdin.readline()#�ӱ�׼�����ȡһ��
    if not line:
        break
    task_list.append([int(x) for x in line.split(" ")])#����ȡ����ת��Ϊ�����б���ӵ������б���
time = 0 #��ʼ��ʱ��Ϊ0
waiting_list=[] #��ʼ���ȴ��б�Ϊ��
while len(task_list)>0:#ֻҪ�����б�Ϊ�վͼ���ִ��
    current_task=next((task for task in task_list if task[3]==time),None) #��ȡ��ǰʱ�������
    if current_task is not None:#����е�ǰʱ�������
        waiting_list.append(current_task)#��������ӵ��ȴ��б���
        waiting_List=sorted(waiting_List,key=lambda x: -x[1])#�������ȼ��Եȴ��б��������
        current_task=waiting_List[0]#��ȡ���ȼ���ߵ�����
    else:
        if len(waiting_List)!=0:#���û�е�ǰʱ������񵫵ȴ���Ϊ��
            current_task=waiting_List[0]#��ȡ���ȼ���ߵ�����
    if current_task is not None:#���������
        current_task[2]-=1#ִ������
        if current_task[2]==0 :#�������ִ�����
            print(str(current_task[0])+""+str(time+1))#��������ź����ʱ��
            task_list.remove(current_task)#�������б����Ƴ�����
            waiting_List.remove(current_task)#�ӵȴ������Ƴ�����
    time +=1 #ʱ���1