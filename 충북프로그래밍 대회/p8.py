

# 처음엔 복호화키가 주어지고
# 두번째엔 암호화 된 문자가 주어진다. (최대 80)


# 복호화 키가 주어지면
# a-e
# b-y
# c-d
# d-b

# 그럼 dic에 a,b,c,d,e,f,g 알파벳을 생성하고
# 복호화키를 가지고 온다음에
# a부터시작해서 해당 복호화키를 리스트에 담는다.
# 그럼 복호화키가 다 들어갈거고
# 두번째에 암호화된 문자가 주어지니까

# 해당 암호에 맞는
# 문자를 찾은뒤 
from string import ascii_lowercase

alpha = list(ascii_lowercase)

dic = {}

b = list(input().strip())
am = list(input().strip())


for i in range(len(b)):
	dic[alpha[i]] = [b[i]]
# 'a': ['e']
# 만약 어디에도 해당하는 문자가 없다면
# 공백출력
# eydbkmiqugjxlvtzpnwohracsf
# Kifq oua zarxa suar bti yaagrj fa xtfgrj

ans = ""
for i in am:
	if i.isupper():
		c = i.lower()
		ans += dic[c][0].upper()

	elif i.islower():
		ans += dic[i][0]
	elif i == " ":
		ans += " "
print(ans)







