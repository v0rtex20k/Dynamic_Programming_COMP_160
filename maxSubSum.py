

# You can either include or exclude an element from your sum.
#	Include: arr[i] + sum
#   Exclude: sum

def maxSubSum(arr,i, prev):
	if i >= len(arr):
		return 0
	if arr[i] <= prev:
		return maxSubSum(arr, i+1, prev)
	return max( maxSubSum(arr, i+1, prev),  			#exclude
		        maxSubSum(arr, i+1, arr[i]) + arr[i] )	#include

if __name__ == '__main__':
	arr = [4,-1, -1, 10]
	print("Maximum Subsequence Sum of", arr, " = ", maxSubSum(arr,0, 0))
