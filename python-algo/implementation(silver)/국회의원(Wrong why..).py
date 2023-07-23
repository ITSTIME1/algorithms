
# O(N) max(int_arr) = N 의 max N N
N = int(input())
arr = [input() for _ in range(N)]
int_arr = list(map(int, arr))

cnt = 0
if len(int_arr) == 1:
  print(0)
else:
  dasom = int_arr.pop(0)
  while dasom <= max(int_arr):
    int_arr[int_arr.index(max(int_arr))]-=1
    # 그냥 문제점이 cnt 를 계속 더하고 있었음... 멍청하게..
    dasom+=1
    cnt+=1
  print(cnt)

