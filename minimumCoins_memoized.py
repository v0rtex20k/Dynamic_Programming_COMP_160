import math


def memoizer(func):
	piggy_bank = {}
	def decorated_minimumCoins(*args):
		if args not in piggy_bank:
			piggy_bank[args] = func(*args)
		return piggy_bank[args]
	return decorated_minimumCoins

@memoizer
def minimumCoins(coins, total, M):
	if M > total:
		return math.inf 	 # infinite value to not overthrow true min	
	elif M == total:
		return 0
	return  1 + min( minimumCoins(coins, total, M + coins[i]) for i in range(len(coins)) )  # include i_th coin, exlude all others



if __name__ == '__main__':
	coins = (1, 5, 6, 8)
	total = 200
	M = 0
	print("MC of", coins, " -> ", total, ": ", minimumCoins(coins, total, M))
