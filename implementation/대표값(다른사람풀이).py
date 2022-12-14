data = []

for _ in range(10) :
  data.append(int(input()))

print(sum(data) // 10)
print(max(data, key = data.count))
