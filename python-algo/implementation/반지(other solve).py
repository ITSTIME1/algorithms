import sys
fw = sys.stdin.readline().replace("\n","")
n = int(sys.stdin.readline())

# 이런 방법이 있구나
# 문자열을 한칸씩 밀어봐서
# 있는지 확인하면 되는거지
# 해당 문자열을 다 돌면
def finds(fw, word):
    ans = 0
    if word.find(fw) >= 0:
        ans = 1
    for i in range(len(fw)):
        word = word[-1] + word[0:len(word)-1]
        print(word)
        
    return ans

real_ans = 0
for _ in range(n):
    word = sys.stdin.readline().replace("\n", "")
    real_ans += finds(fw,word)
print(real_ans)