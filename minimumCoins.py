import math

def minimumCoins(coins, total, M):
	if M > total:
		return math.inf 	 # infinite value to not overthrow true min	
	elif M == total:
		return 0
	return  1 + min(  minimumCoins(coins, total, M + coins[0]),  # include coin1, exlude all others
		              minimumCoins(coins, total, M + coins[1]),  # include coin2, exlude all others
		        	  minimumCoins(coins, total, M + coins[2]),  # include coin3, exlude all others
		        	  minimumCoins(coins, total, M + coins[3]),  # include coin4, exlude all others
		        )

if __name__ == '__main__':
	coins = [1, 5, 6, 8]
	total = 20
	M = 0
	print("MC of", coins, " -> ", total, ": ", minimumCoins(coins, total, M))
