x, y = map(str, input().split())

result = str(int(x[::-1]) + int(y[::-1]))
print(result[::-1])