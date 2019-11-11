maxima = {}
def memoizer(func):
	def decorated_maxSub(*args):
		if args not in maxima:
			maxima[args] = func(*args)
		return maxima[args]
	return decorated_maxSub

@memoizer
def maxSub(arr, start, end):
	if start >= len(arr):
		return 0
	if start == end:
		return arr[start]
	return arr[start] + maxSub(arr, start+1, end)

if __name__ == '__main__':
	arr = (20, -20, 3, -1, 5, 20, 10, -2, 12, 14)
	for i in range(1, len(arr)):
		maxSub(arr, 0, len(arr) - i)
	max_score= max(maxima, key=lambda k: maxima[k])
	print(len(arr), " - (" + str(max_score[1]) + ", " + str(max_score[2]) + "):", maxima[max_score])
