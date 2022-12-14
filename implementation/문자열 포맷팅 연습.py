# %s = 문자열
# %d = 정수
# %f = 부동소수점 실수

string = "내 이름은 %s 입니다." % "홍길동"

string1 = "나의 os 는 %s 입니다" % "windows"
print(string1)

string2 = "My age is %d." % 24
print(string2)

string3 = "One is %f." % 3.14444
print(string3)

string4 = "%d 곱하기 %d = %d" % (2, 3, 6)
print(string4)

name = "Tom"
age = 13

print("%s is %d years old" % (name, age))

# 10 / 3 = 3.333 

a = 10
b = 3
# 부동소수점을 나타내는 %f 는
# 소수점의 자릿수를 나타낼 수 있는데
# 소수점 첫번째 짜리 까지 나타내고 싶다면
# %.1f
# 두번째라면
# %.2f
# 세번째라면
# %.3f

# 이렇게 %.(d)f 정수 값을 넣어준다음 f 를 붙여주면
# 원하는 자릿수의 소수점 포맷팅이 된다.

print("%d / %d = %.1f" % (a, b, a/b))


# 고급형식지정 문자열
# %20s
# %(d)s 라고 한다면 s 앞에 d만큼의 공백이 생긴다.

# "[%-20s]" % "A"
# 이렇게 하면 이번엔 d가 아니라 d 앞에 -가 붙었기 때문에
# 반대로 뒤에 20칸을 채워준다

# 즉 고급형식지정 문자열에서 %ds를 한다면 d만큼의 공백을 앞에서 부터 채워주고
# %-ds 라고 한다면
# 먼저 지정된 문자열을 출력해준 뒤 그 뒤에 d만큼의 공백을 채워준다.

# "[%-20.6f]" % x  
# 이건 %-d.df 형식인데 부동 소수점을 의미하며
# 위에서 지정했던 소수점 자리를 생각한다면 6자리까지 소수점을 나타내고
# -d 만큼이라면 소수점 .6자리까지 출력한 뒤에 그 뒤에 20칸의 공백을 차지한다는 얘기다

# ```
#        3
# x     12
# --------
#       36
# ```

a = 3
b = 12


# 첫번째 방법
print("%7d" % a)
print("x"+"%6d" % b)
print("--------")
print("%7d" % (a*b))

print()
# 두번째 방법
print("%7d" % a + "\n" + "x"+"%6d" % b + "\n" + "--------" + "\n" + "%7d" % (a*b))


# ```
#    123,456
# +    7,890 
# ----------
#    131,346
# ```
print()
a = 123456
b = 7890

print("%9d" % a)
print("+"+"%8d" % b)
print("---------")
print("%9d" % int(a+b))

# "[%-20d]" % 123  # 20칸의 공백의 앞쪽에 123을 인쇄한다.`


# format 함수


string = "내 이름은 {} 입니다.".format("홍길동")
print(string)
string = "내 이름은 {{{}}} 입니다.".format("홍길동")
print(string)

string = "{0}이의 수학{2}는 {1}입니다.".format("태선", 100, "점수")
print(string)

# "[{:<20}]".format("*")
# {:>20} = 이 의미는 전체공간 d에서 > 앞쪽에다 공백을 먼저 추가하고 그 다음에 .format("")그다음 format 된거를
# 추가하라는 의미이다.

# {:<20} = 의미는 < d 만큼의 크기가 있는데 < 뒤쪽에다가 공백을 주고 즉 문자열은
# 앞쪽에다가 주라는 의미이다.

# "[{:20.5f}]".format(1 / 3)
# 전체 공간 20에다가.소수점 5자리 까지 출력한다.

# "[{:20,}]".format(1234567890)
# 이건 전체공간 20의 , 천의자리 숫자마다 즉 3자리씩 끊어서 ,를 넣어준다

num = 100000000000
print("{:,}".format(num))
num = 20000000000000000000000
print("[{:>50,}]".format(num))
print("[{:<50,}]".format(num))

num = 2
print("%02d" % num)