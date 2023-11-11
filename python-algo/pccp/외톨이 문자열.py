from collections import Counter
def solution(input_string):
    answer = []
    two_dict = defaultDict(list)
    two_list = list(k for k, v in two_dict.items() if v >= 2)
    
    while two_list:
        word = two_list.pop()
        
        startIndex = input_string.find(word)
        visited = [False] * len(input_string)
        visited[startIndex] = True
        # 다른 문자를 만날때까지
        for i in range(startIndex + 1, len(input_string)):
            if input_string[i] != word:
                break
            else:
                if visited[i] == False:
                    visited[i] = True
            
        # 외톨이
        for i in range(len(input_string)):
            if input_string[i] == word and visited[i] == False:
                answer.append(word)
                break
    
    answer.sort()
    return "".join(answer) if answer else "N"
