result = []
for i in range(10):
  number = int(input())
  s = number%10
  result.append(s)

result = set(result)
print(len(result))