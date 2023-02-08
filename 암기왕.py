# 문제분석

import sys
import heapq
from collections import deque
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline


t = int(input())


for i in range(t):
	s1_n = int(input())
	s1_num = list(map(int, input().split()))

	s1_dic = {i: 0 for i in s1_num}


	s2_n = int(input())
	s2_num = list(map(int, input().split()))

	for j in s2_num:
		if j in s1_dic:
			print("1")
		else:
			print("0") 	