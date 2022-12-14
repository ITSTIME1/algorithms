string = input()
arr = list(string)
result = []
for i in range(len(string)-2):
  for j in range(i+1, len(string)-1):
    for k in range(j+1, len(string)):
      result.append(arr[:j][::-1] + arr[j:k][::-1] + arr[k:][::-1])

# sort() 기본적으로 오름차순
result.sort()
print("".join(result[0]))