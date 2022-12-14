
# 14:00:00
# 13:52:30
h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

t1 = (h1*3600) + (m1*60) + s1
t2 = (h2*3600) + (m2*60) + s2
total = t2-t1
if t1 > t2:
	total += 24 * 3600
r_h = total // 3600
r_m = (total % 3600) // 60
r_s = total % 60

print("%02d:%02d:%02d" % (r_h, r_m, r_s))