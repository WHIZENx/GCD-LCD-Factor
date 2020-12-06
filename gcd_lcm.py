from math import sqrt
from functools import reduce

def gcd(x, y):
	while y:
		x, y = y, x%y
	return x

def cal_gcd(alist):
	for i in range(len(alist)):
		try:
			result = gcd(alist[0], alist[1])
			alist.pop(0)
			alist.pop(0)
			alist.insert(0, result)
		except:
			return alist[0]

def factors(n):
	step = 2 if n%2 else 1
	return sorted(list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))))

def factor_sum(alist):
	list_result = []
	for i in alist:
		list_result.append(factors(i))

	for i in range(len(list_result)):
		try:
			result = set(list_result[0]) & set(list_result[1])
			list_result.pop(0)
			list_result.pop(0)
			list_result.insert(0, result)
		except:
			return max(list(list_result[0]))

def lcmfactor(x, y):
	list_lcm = (x*y) // gcd(x, y)
	return list_lcm

def cal_lcm(alist):
	first = alist[0]
	array_list = alist[1:]
	for item in array_list: 
		first = (first*item) // gcd(first, item)
	return first

def prime_factors(n):
	i = 2
	factors = [1]
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors