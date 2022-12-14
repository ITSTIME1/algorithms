# Day = 0
# arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
# x, y = map(int,input().split())
 
# for i in range(x-1):
#     Day = Day + arrList[i]
#     print(Day)

# Day = (Day + y) % 7
# print(Day)
# print(weekList[Day])



import calendar

# 대신 이떄 리스트는 0월요일 이런식으로 해야됨
# 위 코드에서 리스트는 1월1일이 월요일이라는 값 때문에
# 인덱스 0 부터 시작하는걸 1의 위치에 월요일을 둔것.
day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

day = calendar.weekday(2007, x, y)
print(day_list[day])