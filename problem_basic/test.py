import sys

N = int(sys.stdin.readline())
array = []
for i in range(N):
    player = sys.stdin.readline()
    array.append(player)

start = ""
count = 0
player = []
new_player = []
set_list = []
for j in range(len(array)):
    start = array[j][0]

    for k in range(len(array)-1):
        # 같은 문자열이 있을때
        if(start == array[k][0]):
            player.append(array[k][0])
            if(player.count(start) >= 5):
                new_player.append(start)
        else:
            # 같은 문자열이 없을때
            continue

for v in new_player:
    if v not in set_list:
        set_list.append(v)
set_list.sort()
print(set_list)
if(len(set_list) == 0 ):
    string_word = "PREDAJA"
    print(string_word.strip('""'))
else:
    string_word = "".join(set_list)
    print(string_word.strip('""'))

        