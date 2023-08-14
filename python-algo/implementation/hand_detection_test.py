
# 이게 서클들이 현재 있는 좌표들이고
circle_cordi = [(255, 30, id), (100, 40, id), (300, 10, id), (500, 120, id)]


# 현재 마우스의 위치를 보자
x, y = 255, 30

# 현재 마우스 위치가 circle_cordi에 포함되어 있는지를 검사해보면


if (x, y) in circle_cordi:
	# 있다면 그걸 잡아야하니까 hover효과를 주면서
	image.style.hover = true
	wordTarget = id
	# 그리고 주먹을 쥔 상태에서 wordTarget이 설정되어 있기 때문에
	# 현재 wordTarget의 left, top값을 두고
	# 마우스 이미지의 좌표값으로 변경해준다. 그러면 wordTarget이 따라오는 효과가 나게 된다.
	# 그렇다면 wordTarget이 이미지의 left, top값으로 따라오게 되니까
	# mousebear에 가까이 가게 되면 wordTarget이 넣어져야 한다.
	# 따라서 bear 영역의 좌표를 미리 설정해두고
	# wordTarget이 현재 bear좌표보다 작거나 같다면 push 함수를 실행한다.
	# 결국 핸드 트랙킹을 하는 것과 하지 않을떄를 구분을 해야 할거 같다.
	print("yes")
else:
	print("no")
