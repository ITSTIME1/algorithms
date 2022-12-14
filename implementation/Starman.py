
data = [[1967, 'DavidBowie'], [1969, 'SpaceOddity'], [1970, 'TheManWhoSoldTheWorld'], [1971, 'HunkyDory'],[1972, 'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'],
[1973, 'AladdinSane'], [1973, 'PinUps'], [1974, 'DiamondDogs'], [1975, 'YoungAmericans'], [1976, 'StationToStation'], 
[1977, 'Low'], [1977, 'Heroes'], [1979, 'Lodger'], [1980, 'ScaryMonstersAndSuperCreeps'], [1983, 'LetsDance'], [1984, 'Tonight'],
[1987, 'NeverLetMeDown'], [1993, 'BlackTieWhiteNoise'], [1995, '1.Outside'], [1997, 'Earthling'], [1999, 'Hours'], [2002, 'Heathen'],
[2003, 'Reality'], [2013, 'TheNextDay'], [2016, 'BlackStar']]

Q = int(input())

for i in range(Q):
	S, E = map(int, input().split())
	result = []
	for j in data:
		# S 시작 연도랑 같은 것들
		if S <= j[0] <= E:
			result.append(j)
	# 람다의 기본은 오름차순
	# 알파벳 순으로
	sorting_list = sorted(result, key = lambda x : x[0])
	print(len(result))
	for k in range(len(sorting_list)):
		year = sorting_list[k][0]
		album = sorting_list[k][1]
		print(str(year) + " " + str(album))