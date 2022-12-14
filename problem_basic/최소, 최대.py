N = int(input())
N_list = list(map(int, input().split()))

result_min = min(N_list)
result_max = max(N_list)

print(str(result_min)+' '+str(result_max))