def deco(f):
	print("deco!")
	return 41



# 데코레이터에 의해서
# double함수가 실행되면 사실상 deco(double)
# 즉 함수가 인자로 넘어가게 되는거지
# 그러면 deco함수가 실행은 되어야 하니까
# deco!가 실행되고 인자로 받은 함수를 리턴하게 된다면
# 외부에서 리턴받은값은 f그 자체가 되겠지
# 따라서 f그 자체를 리턴받았기 때문에 리턴받은 함수를 실행한다는건 문제가 없어
# 하지만 위 코드에서 return 을 함수로 하지 않고 정수 리터럴로 리턴한다고 생각해보자
# 그러면 얘기가 달라지지
# 똑같은 맥락으로 dobule함수가 실행이 되면, deco(double)까지는 일치해
# 이후 deco함수가 실행되고, print()가 실행되면서 return 41을 리턴하게 되지
# 그럼 똑같이 외부에서 해당 값을 리턴받았다고 생각해보자
# 그럼이게 41()이런식으로 동작이 가능한가?
# 외부에서 받은 값은 더 이상 f가 아닌 41이기 때문에
# 41은 함수가 아니자나 상수리터럴일 뿐이지
# 따라서 해당 값은 함수처럼 호출할 수 없다는 결론이 나와
# 명제로 따져보면 p 가 함수를 반환한다면 -> q는 함수다.
# 그럼 이걸 증명하기 위해서 모순증명법을 사용해보자
# deco가 함수를 반환한다면 q는 함수가 아니다.
# 만약 결과가 틀리다면 원래 명제가 맞는것.
# 만약 결과가 맞다면 원래 명제가 틀린것.

# deco가 함수를 반환한다면 q는 함수이기 때문에
# 원래 억지로 결론을 부정해버린 것이 틀리다는 사실을 알아냈고
# 원래 명제가 참임을 증명했어
# 그럼 반대로 deco함수를 반환하지 않는다면 q는 함수일까?
# deco함숳가 함수를 반환하지 않았는데 q가 함수일리가 없지
# 대우증명법을 통해서
# q가 함수가 아니면 deco는 함수를 반화하지 않았다.
# q가 함수가 아니기 때문에 deco는 함수를 반환하지 않은거야
# 그럼 함수처럼 쓸 수 있는 것은 함수를 반환 했을때 사용할 수 있는 방법인데
# 함수를 리턴하지 않았으므로 함수처럼 사용하지 못한다는 논리가 성립되는거지
# 
@deco
def double(num):
	return 2 * num

# 이렇게 한다고 해도
# a는 더 이상 함수가 아닌 상수 리터럴 일뿐이야 type체킹해보자?

# 애초에 불러지지도 않아 따라서 callable자체가 안된다는거야
# dobule(10) 이 == 41(10) 이런식으로 되어 버리기 때문이지
# ㅇㅋ?

if isinstance(double(10), int):
	print("INT")
else:
	print("Function")

assert add(2,3), "Expected Value"
