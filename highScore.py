import math

def memoizer(func):
	maxima = {}
	def decorated_highScore(*args):
		if args not in maxima:
			maxima[args] = func(*args)
		return maxima[args]
	return decorated_highScore

@memoizer
def highScore(arr, i, best, sig):
	if i == len(arr):
		return best
	if arr[i] < 0 and best == 0:
		return highScore(arr, i+1, best, sig) # ignore
	sig += arr[i]
	if sig < 0:
		sig = 0
	best = max(best, sig)
	return highScore(arr, i+1, best, sig)

def findMax(arr, i, maxx):
	for k in range(len(arr)):
		if arr[k] > maxx:
			maxx = arr[k]
			i = k
	return i, maxx

def all_same_sign(arr):
	numP = 0; numN = 0
	for i in arr:
		if i >= 0:
			numP += 1
		else:
			numN += 1
	if numP == len(arr):
		print("{0, " + str(len(arr) - 1) + "}:", sum(arr))
		return True
	elif numN == len(arr):
		i = 0 ; maxx = -math.inf
		i, maxx = findMax(arr, i, maxx)
		print("{" + str(i) + ", " + str(i) + "}:", maxx)
		return True
	return False

if __name__ == '__main__':
	arr = (5, -3, -9, 10, 18)
	same = False
	same = all_same_sign(arr)
	if not same:
		print(highScore(arr, 0, 0, 0))
	