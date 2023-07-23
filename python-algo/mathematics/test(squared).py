for i in range(5):
	for j in range(i):
		print(" ", end = "")

	for c in range(9-(i*2)):
		print("*", end = "")
	print()


for i in range(4, 0, -1):
	for j in range(i-1):
		print(" ", end = "")

	for k in range(9-((i-1)*2)):
		print("*", end = "")

	print()
