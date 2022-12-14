def factorial(n):
    # ans = 1로 둔 이유는 0!, 1! = 모두 1 이기 때문이다
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans



# 즉 이항계수에서 (n/k) 가 나오면 순서 없이
# 뽑는 조합을 의미한다
# 즉 n! // r! // n-r! 과 같다
def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)