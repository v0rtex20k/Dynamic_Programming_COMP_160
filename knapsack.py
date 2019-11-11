
# I FREAKING DID IT AGAIN! WTF!!

class item(object):
	"""Pass it a weight and a value"""
	def __init__(self, weight, value):
		self.weight = weight
		self.value  = value
	def __str__(self):
		return "{" + str(self.weight) + ", " + str(self.value) + "}"
		
# Include an item: 
#		
		
def addToKnapsack(items, W, i):
	if i >= len(items):
		return 0
	if W - items[i].weight < 0:
		return addToKnapsack(items, W, i+1)  # ignore the element
	return max( addToKnapsack(items, W, i+1), # ignore
				addToKnapsack(items, W-items[i].weight, i+1) + items[i].value)

if __name__ == '__main__':
	
	A = item(1,1)
	B = item(3,4)
	C = item(4,5)
	D = item(5,7)
	W = 7 									 # maximum knapsack weight

	items = [A, B, C, D]
	print("[Optimal Knapsack] ", str(items[0]), 
								 str(items[1]), 
								 str(items[2]), 
								 str(items[3]), 
		  ":\n Value = ", addToKnapsack(items, W, 0))