import sys

test_case = int(input())
result = 0

# Solution (1)
# for i in range(test_case):
#   a, b = map(int, sys.stdin.readline().split())
#   print(a+b)


# Solution(2)
def readline_function(test_case):
  for i in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    result = a+b
    print(result)


readline_function(test_case)