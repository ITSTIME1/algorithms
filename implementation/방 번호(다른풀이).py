import sys
N = sys.stdin.readline().strip()
nums = list(0 for _ in range(10))
for i in N:
    nums[int(i)] += 1
    if i == '6' and nums[6] > nums[9]:
        nums[6] -= 1
        nums[9] += 1
        print(nums)
    elif i == '9' and nums[9] > nums[6]:
        nums[9] -= 1
        nums[6] += 1
        print(nums)

nums.sort(reverse=True)
print(nums[0])
