def longestCommonSubsequence(A, B, i, j):
	if i >= len(A) or j >= len(B):
		return 0
	if A[i] == B[j]:
		return 1 + longestCommonSubsequence(A, B, i+1, j+1)
	return  max( longestCommonSubsequence(A, B, i+1, j) ,   # include A[i]
	 		     longestCommonSubsequence(A, B, i, j+1) )   # include B[j]

if __name__ == '__main__':
	word1 = "abcdef"
	word2 = "acbcf"
	print("LCS: (", longestCommonSubsequence(word1, word2, 0, 0), ")")