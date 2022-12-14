import sys

li = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", 
      "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]
N = int(sys.stdin.readline().strip())

result = N % 14
div = N // 14
string = str(li[result-1])

if string == "tururu" or string == "turu":
	re_string = str(li[result-1] + "ru" * div)
	if re_string.count("r") >= 5:
		print("tu+ru"+"*"+ str(re_string.count("r")))
	else:
		print(re_string)
else:
	print(string)
