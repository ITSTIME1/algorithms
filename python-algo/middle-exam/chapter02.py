number = 3
str = "I eat %d apples." % 3
str1 = "I eat %d apples." % number
# 이 의미가. 소수점 둘째짜리 까지
# 출력하라는 의미가 된다.

# 13.123 이라면 12까지만 출력
# 결국 소수점 자릿수 어디까지를 출력할거냐는 얘기가 된다.
# 형식지정자로는 %d, 정수
# %f 실수
# %o 8진 정수
# %x 16진 정수
# %e, %E, 
str2 = "I eat %.2f" % 123.1235
print(str2)
# 변수로도 문자열 포맷팅이 가능하고, 직접 상수 리터럴을 주더라도 가능하지
print(str1)


# format같은 경우 키워드로도 지정이 가능함.
# name age이런식으로 
# 해당 키워드로 맵핑이됨
str3 = "name : {}, age: {}".format("kim", 45)
str3 = "name : {name}, age: {age}".format(name="kim", age=45)




# %b = 이진수
# %c = 캐릭터
# %d = 10진 정수
# %e = 지수
# %E = 지수 대문자 출력
# %f = 부동소수점 표현
# %g = 지수 또는 부동소수점
# %n = 숫자형식 사용 숫자 서식 지정
# %o = 8진수 정수
# %s = 문자열
# %x = 16진수, %X 16진수 대문자
# %% = %문자 출력

# format 스펙을 이용해서는 이런식으로 짜는게 가능함


print("'{0:>5}'".format("hi"))
# 우선적으로 4칸만 표시하고
# 12자리를 확보
print("'{0:12.4f}'".format(3.141592653))



# f-string 을 사용해볼건데
# name은 변수를 통해서 표현하는데
# 문자열 서식지정자를 사용함
# 10칸을 확보할건데 오른쪽 정렬을 하라는뜻임
name = "kim"
# print(f'{name:>5s}')
# {name:10d}
# {price:10.2f}
# 실수인데 두자리까지만 포함할거고 10칸을 확보해줘 라는 의미네
# 근데이때 만약 출력하고자 하는 자릿수가 더 적고 출력하고자 하는 숫자가 더 클때
# 나머지는 0으로 채워진다.


# 마찬가지로 10칸을 확보하고 name은 문자열이다.
# 오른쪽 정렬할건데 공백은 =이것으로 채운다.
print(f'{name:=>10s}')
# 우선 소수는 두자리까지만 출력하고 따로 공백을 확보하지 않을거야
# 출력하고자 하는 것은 sharee * price를 출력해줘라는 얘기지
# print(f'{shares*price:.2f}')


name = "hong"
age = 24
print(f'My name is {name} and i amd {age} years old.')



str1 = "Today's weather is {weather}".format(weather = "sunny")
print(str1)

cnt = 100
str2 = "I have %d apples" % cnt
print(str2)

info = {'이름': 'Alice', 
		'나이': 25}

make_str = "%s is %d years old." % (info['이름'], info['나이'])
print(make_str)

x, y = 1, 2
make_str2 = "%d + %d = %d" % (1, 2, 1 + 2)
print(make_str2) 

f = 10.2
make_str3 = "The success rate is %.2f%%." % f
print(make_str3)

frint = 10.1254251
make_str4 = f'{frint:.3f}'
print(make_str4)




