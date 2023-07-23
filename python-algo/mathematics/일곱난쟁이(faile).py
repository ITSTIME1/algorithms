N = 9
arr = [int(input()) for _ in range(N)]
# 완탐으로풀면..
arr.sort()
total = []
for i in range(N-8):
	for j in range(i+1, N-5):
		for k in range(j+1, N-4):
			for l in range(k+1, N-3):
				for c in range(l+1, N-2):
					for n in range(c+1, N-1):
						for m in range(n+1, len(arr)):
							if arr[i] + arr[j] + arr[k] + arr[l] + arr[c] + arr[n] + arr[m] == 100:			
								total.append([arr[i], arr[j], arr[k], arr[l], arr[c], arr[n], arr[m]])
								print(*total[0], sep="\n")
								exit()


