x = 1

maxima = {}
def memoizer(func):
	def decorated_maxSub(*args):
		if args not in maxima:
			maxima[args] = func(*args)
		return maxima[args]
	return decorated_maxSub

@memoizer
def maxSub(arr, i, j):
	global x
	print(x)
	x += 1
	if i >= len(arr):
		return 0
	if i == j:
		return arr[i]
	return max(arr[i], arr[i] + maxSub(arr, i+1, j))

if __name__ == '__main__':
	arr = (-3, -1, 5, 10, -2, 1, 1, 9)
	for h in range(1, len(arr)):
		maxSub(arr, 0, len(arr) - h)
	max_score= max(maxima, key=lambda k: maxima[k])
	print("(" + str(max_score[1]) + ", " + str(max_score[2]) + "):", maxima[max_score])
