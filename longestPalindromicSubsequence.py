
def longestPalindromicSubsequence(word, i, j):
	if i == j:
		return 1
	if word[i] == word[j]:
		return 2 + longestPalindromicSubsequence(word, i+1, j-1) # match
	return max( longestPalindromicSubsequence(word, i+1, j),     # include unmatched left
				longestPalindromicSubsequence(word, i, j-1)  	 # include unmatched right
			  )


if __name__ == '__main__':
	word = "aba"
	print("LPS: (", longestPalindromicSubsequence(word, 0, len(word)-1), ")")