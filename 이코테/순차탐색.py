
def sequential_search(n, target, array):
	for i in range(n):
		if array[i] == target:
			return i
		else:
			print("계속 찾는 중입니다")
# create number of word, want to find target word
input_data = input().split()

n = int(input_data[0])
target = input_data[1]

# word list
array = input().split()

print(sequential_search(n, target, array))
