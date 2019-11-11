import math
class subArray(object):
	def __init__(self, val, start, length):
		self.val = val
		self.left = start
		self.right = start + length - 1
		
summations = {}

def memoizer(func):
	global summations
	def decorated_maximumSubscore(*args):
		if args not in summations:
			summations[args] = func(*args)
	return decorated_maximumSubscore

@memoizer
def maximumSubscore(arr, start, end):
	if start == len(arr) - end:
		return arr[start]
	return max(arr[-end] + maximumSubscore(arr, start, end + 1))
	#return max(sum(arr[start:-i]) for i in range(len(arr)))


if __name__ == '__main__':
	arr= (-1, 1, -3, 5, 11, 2, -3, 1)
	for i in range(len(arr)):
		maximumSubscore(arr, i, 1)
	winner = max(summations, key=lambda k: summations[k])
	print(summations)
	print(winner, summations[winner])
