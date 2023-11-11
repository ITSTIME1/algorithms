# closure = 외부 함수에 내부 함수를 정의 외부함수가 내부 함수를 리턴(조건) 만족해야 클로저
import time

class TimeDecorator:
    def __init__(self, func, radius = 100):
        self.func = func
        self.radius = radius

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(self, *args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start} seconds")

        

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @TimeDecorator
    def getArea(self, *args, **kwargs):
    	# 여기에서 넘어온 self는 결국 TimeDecorator의 self
    	# 따라서 Timedecorator의 radius를 참조하지 못하기 때문에 발생됨
    	# 그럼 timedecorator에 radius를 준다면?
    	a = 3.14 * self.radius * self.radius
    	print(f"결과 {a}")

a = Circle(100)
a.getArea(100)


# a라는 객체가 생성이 되고
# 생성되는 시점에 decorator가 호출이되는가?

# # 1 time deco -> circle
# a = Circle(100)
# a.getArea()



# def time_decorator(*args):
# 	print(args)
# 	def decorated(*args):
# 		start = time.time();
# 		args[0]
# 		args[1]
# 		end = time.time();
# 		print(f"{end - start} seconds")


# 	return decorated


# @time_decorator
# @TimeDecorator
# def myfunc():
# 	for i in range(4):
# 		print(f"{i}, args =  {args}")


# @time_decorator
# def myfunc2():
# 	for i in range(100):
# 		print(i)

# myfunc(1,2,3,4

# class logit(object):

#     _logfile = 'out.log'

#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args):
#         log_string = self.func.__name__ + " was called"
#         print(log_string)
#         # Open the logfile and append
#         with open(self._logfile, 'a') as opened_file:
#             # Now we log to the specified logfile
#             opened_file.write(log_string + '\n')
#         # Now, send a notification
#         self.notify()

#         # return base func
#         return self.func(*args)




# import numpy as np
# # range()함수는 정수형 시퀀스를 생성한다.
# # print(range(1.0, 5.0, 0.2))
# a = np.arange(1, 4, 0.2).reshape((3,5))
# # 1 1.2 1.4 1.6 1.8 
# # 2.2.2 2.4 2.6 2.8 
# # 4
# b = np.linspace(1, 4, 15).reshape(3, 5)
# print(a)
# print(b)

# # 정수형 난수를 생성 size에 shape를 주면 해당 차원 만큼을 정수를 생성해서 만들어줌
# c = np.random.randint(1, 100, 15).reshape(3, 5)
# c1 = np.random.randint(1, 100, (3,5))
# print(c)
# print(c1)