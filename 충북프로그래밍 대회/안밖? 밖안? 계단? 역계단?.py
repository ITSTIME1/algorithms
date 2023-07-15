import sys
input = sys.stdin.readline

word = ["fdsajkl;", "jkl;fdsa", "asdf;lkj", ";lkjasdf", "asdfjkl;", ";lkjfdsa"]


string = input().strip()


answer = [i for i in range(len(word)) if word[i] == string]


result = ""

if len(answer) == 0:
    print("molu")
    exit()
    
if answer[0] == 0 or answer[0] == 1:
    result = "in-out"

elif answer[0] == 2 or answer[0] == 3:
    result = "out-in"

elif answer[0] == 4:
    result = "stairs"

else:
    result = "reverse"

print(result)


