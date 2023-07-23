
# 줄 2, 10, 15
N = int(input())
w_list = []
for i in range(N):
  w_list.append(int(input()))

w_list.sort(reverse=True)

max_weight_list = []

for j in range(N):
  max_weight_list.append(w_list[j] * (j+1))

print(max(max_weight_list))
  

    
  

