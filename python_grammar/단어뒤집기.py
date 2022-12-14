# 2
# I am happy today
# We want to win the first prize

N = int(input())

for i in range(N):
    word = input()
    word += " "
    string_stack = []
    new_string_stack = []
    for j in word:
        if j != " ":
            string_stack.append(j)
        else:
            new_change_string = ""
            for k in range(len(string_stack)):
                new_change_string += string_stack.pop()

            new_string_change_string = new_change_string + " "
            new_string_stack.append(new_string_change_string)
      
    print("".join(new_string_stack), end="\n")
