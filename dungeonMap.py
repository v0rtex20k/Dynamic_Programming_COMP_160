import math

def dungeonMap(Dungeon, row, col, HP):
	if row < 0 or col < 0:
		return math.inf
	if row == 0 and col == 0:
		print ("DONE", HP)
		return HP
	#print("HP = ", HP , " after visiting", row, ",", col)
	return min(dungeonMap(Dungeon, row - 1, col, HP + Dungeon[row][col]),  # UP
		 	   dungeonMap(Dungeon, row, col - 1, HP + Dungeon[row][col]))  # LEFT
	
if __name__ == '__main__':
	w, h = 4, 4
	Dungeon = [[0 for x in range(w)] for y in range(h)] 
	Dungeon[3][3] = 10
	Dungeon[3][2] = 5
	Dungeon[2][3] = 5
	Dungeon[2][2] = -3
	Dungeon[1][1] = -3
	Dungeon[3][0] = -3
	Dungeon[0][3] = -3
	Dungeon[1][2] = 5
	Dungeon[2][1] = 5
	endHP = 1
	print("MIN HP: ", dungeonMap(Dungeon, 3, 3, endHP))
