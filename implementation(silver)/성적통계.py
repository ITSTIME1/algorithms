K = int(input())

x = 0 
for i in range(K):
  grade = list(map(int, input().split()))
  grade.pop(0)
  grade.sort(reverse=True)
  x += 1
  result = [grade[j] - grade[j+1] for j in range(len(grade)-1)]
  print("Class %d" % x)  
  print("Max %d, Min %d, Largest gap %d" % (max(grade), min(grade), max(result)))