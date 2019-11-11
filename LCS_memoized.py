def memoizer2D(func):
	memo = {}
	def memodFoo (* args ):
		if args not in memo :
			memo [ args ] = func (* args )
		return memo [ args ]
	return memodFoo


@memoizer2D
def longestCommonSubsequence(A, B, i, j) -> str:
	if i >= len(A) or j >= len(B):
		return ''
	if A[i] == B[j]:
		return str(A[i]) + longestCommonSubsequence(A, B, i+1, j+1)
	return  max( longestCommonSubsequence(A, B, i+1, j) ,   # include A[i]
	 		     longestCommonSubsequence(A, B, i, j+1) , key = len)   # include B[j]

if __name__ == '__main__':
	word1 = "abcdef"
	word2 = "acbcf"
	print("LCS: (", longestCommonSubsequence(word1, word2, 0, 0), ")")
