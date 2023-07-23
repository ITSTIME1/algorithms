import math

if __name__=='__main__':
    case = int(input())
    for _ in range(case):
        n, m = map(int, input().split())
        result = math.factorial(m)//(math.factorial(m-n) * math.factorial(n))
        print(result)


