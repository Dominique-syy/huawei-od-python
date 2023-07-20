def main():
    # ��ȡ����� m��n �� R
    m, n, R = map(int, input().split())
    # ��ȡ������б� a �� b
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # ���� solve �������м��㣬������������� result ��
    result = solve(R, a, b)
    # ��������б����ÿһ������
    for r in result:
        print(r[0], r[1])

def solve(R, a, b):
    index = 0
    result = []
    for j in a:
        ints = [0, 0]
        while index < len(b):
            if j <= b[index] and b[index] - j <= R:
                ints[0] = j
                ints[1] = b[index]
                result.append(ints)
                break
            index += 1
    return result

if __name__ == "__main__":
    main()
