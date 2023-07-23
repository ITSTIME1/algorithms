for i in range(len(text)):
    i = i + idx
    if i >= l:  # 메시지가 끝났으면 break
       break
    loc = ord(text[i]) - ord('A')
    check[loc] += 1  # 개수 더하기
    if check[loc] == 3:  # 같은 알파벳이 3번 등장했으면
    	if i == l - 1 or text[i] != text[i + 1]:  # 마지막 알파벳이거나 다음 알파벳과 지금 알파벳이 다르면
            b = False  # 반복문 종료
            break
        else:
           check[loc] = 0  # 개수 0으로 초기화
           idx += 1  # 건너뛸 인덱스 1 추가