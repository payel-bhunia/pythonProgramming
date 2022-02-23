def solve1(a):
	val = 0
	l = len(str(a)) - 1
	actual_val = a
	while a > 0 :
		val += (a % 10) * (10 ** l)
		l -= 1
		a = a // 10
	if val == actual_val:
		return 1
	else:
		return 0




if __name__ == '__main__':
	S = 121
	n = solve1(S)
	print(n)



