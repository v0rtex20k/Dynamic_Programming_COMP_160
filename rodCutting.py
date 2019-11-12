
x = 1

def memoizer(func):
	revenue = {}
	def decorated_cut_rod(*args):
		if args not in revenue:
			revenue[args] = func(*args)
		return revenue[args]
	return decorated_cut_rod

@memoizer
def cut_rod(prices, l):
	c = 1
	global x
	print(x)
	x += 1
	if l == 0:
		return 0							    # aka no rod left to cut
	best_price = max(prices[i] + cut_rod(prices, l - i - 1) - c for i in range(0, l))	# 1 ... (l - 1)
	return max(best_price, prices[l])


if __name__ == '__main__':
	prices = (0 , 1, 5, 8, 9, 10 , 12 , 13 , 4, 15 )#, 17 , 14 , 18 , 20 , 21 , 32 , 
		      #28 , 25 , 36 , 22 , 32 , 16 , 7 , 40 , 34 , 37)
	l = len(prices) - 1
	print("You can make at most $" + str(cut_rod(prices, l)) , "with a rod of length", l, "inches.")
