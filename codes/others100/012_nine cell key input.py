# coding:utf-8
buttonWords = [
    [' '],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', '1'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]

def main():
    # ����һ���ַ���
    line = input()
    solveMethod(line)

def solveMethod(line):
    # ��ʾ��ǰģʽ������ģʽ����ĸģʽ��
    numMode = True
    # ���ڹ����ַ������
    builder = ""
    inputs = list(line)
    i = 0
    while i < len(inputs):
        # ��ȡ��ǰ�ַ�
        c = inputs[i]
        if c.isdigit() and c != '0':
            if numMode:
                # ��������ӵ�β��
                builder += c
            else:
                last = c
            count = 0
            while i < len(inputs) and last == inputs[i]:
                last = inputs[i]
                count += 1
                i += 1
            num = int(c)
            buttonWord = buttonWords[num]
            # ƫ����Ϊ (count - 1) % len(buttonWord)����ȡ�����������ѭ��ѡ��ť��Ӧ����ĸ
            word = buttonWord[(count - 1) % len(buttonWord)]
            builder += word
            i -= 1
        # �����л�ģʽ�Ϳո�����
        if c == '#':
            numMode = not numMode
        elif c == '0':
            builder += '0' if numMode else ' '
        i += 1
        continue
    # ����������ַ������
    print(builder)

if __name__ == '__main__':
    main()
