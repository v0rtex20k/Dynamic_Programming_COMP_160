import math

def memoizer(func):
	maxima = {}
	def decorated_maxSub(*args):
		if args not in maxima:
			maxima[args] = maxSub(*args)
		return maxima[args]
	return decorated_maxSub

@memoizer
def maxSub(arr, start, end):
	if start >= len(arr):
		return -math.inf
	if start == end:
		return arr[start]
	return max(arr[end], arr[end] + maxSub(arr, start+1, end))

if __name__ == '__main__':
	arr = (-1, 20, -30, 5, 11, 2, -3, 4)
	maxSub(arr, 0, len(arr) - 1)
	
