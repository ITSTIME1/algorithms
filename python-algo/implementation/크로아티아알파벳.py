import sys
input = sys.stdin.readline

word = ["c=",
        "c-",
        "dz=", 
        "d-",
        "lj",
        "nj",
        "s=",
        "z="]
 
 
string = input().strip()

for i in word:
    # string에 해당 문자가 있다면 문자열변경
    if string.find(i) != -1:
        # replace은 문자열내에서 해당 부분이 있으면 전부 변경.
        string = string.replace(i, "*")
        # 이게 가능한 이유는 lj, nj, dz가 분리되서 보지 않고 하나로 보기 때문에 문자열 하나로 보는게
        # 가능하다 따라서 어떠한 한문자로 처리만 한다면 가능해진다.

print(len(string))


    