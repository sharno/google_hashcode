def paint_line(r1, c1, r2, c2):
	return "PAINT_LINE {} {} {} {}".format(r1, c1, r2, c2)

def erase_cell(r, c):
	return "ERASE_CELL {} {}".format(r, c)

def paint_square(r, c, s):
	return "PAINT_SQUARE {} {} {}".format(r, c, s)

def readfile(filename):
	file = open(filename)
	NM = [int(x) for x in file.readline().split()]
	N = NM[0]
	M = NM[1]

	grid = []
	for r in range(N):
		row = [0 if x == '.' else 1 for x in file.readline()]
		grid.append(row)
	return N, M, grid

def extract_singles(grid, N, M):
	singles = []
	for r in range(N):
		for c in range(M):
			if grid[r][c] == 1:
				right = c+1
				left = c-1
				above = r-1
				below = r+1

				if r == 0:
					above = below
				if r == N-1:
					below = above
				if c == 0:
					left = right
				if c == M-1:
					right = left

				if grid[above][c] == 0 and grid[below][c] == 0 and grid[r][left] == 0 and grid[r][right] == 0:
					singles.append((r, c))
	return singles

def extract_stripes(grid, N, M):
	hstripes = []
	for r in range(N):
		queue = []
		for c in range(M):
			if grid[r][c] == 1:
				queue.append((r,c))
			if grid[r][c] == 0 or c == M-1:
				if len(queue) > 1:
					hstripes.append(queue)
				queue = []

	vstripes = []
	for c in range(M):
		queue = []
		for r in range(N):
			if grid[r][c] == 1:
				queue.append((r,c))
			if grid[r][c] == 0 or r == N-1:
				if len(queue) > 1:
					vstripes.append(queue)
				queue = []
	return hstripes + vstripes

def solve_stripes(grid, N, M, stripes, singles,solution):
	#solution = []
	stripes = [[s, len(s)] for s in stripes]
	stripes.sort(key = lambda x: x[1])
	while len(stripes) != 0:
		s = stripes[-1]
		del stripes[-1]

		s[1] = 0
		for square in s[0]:
			if grid[square[0]][square[1]] == 1:
				s[1] += 1

		if len(stripes) == 0:
			if s[1] >0:
				for square in s[0]:
					grid[square[0]][square[1]] = 0
				solution.append(paint_line(s[0][0][0], s[0][0][1], s[0][-1][0], s[0][-1][1]))
		elif s[1] >= stripes[-1][1] and s[1] > 0:
			for square in s[0]:
				grid[square[0]][square[1]] = 0
			solution.append(paint_line(s[0][0][0], s[0][0][1], s[0][-1][0], s[0][-1][1]))
		elif s[1] == 0:
			pass
		else:
			stripes.append(s)
			stripes.sort(key = lambda x: x[1])

	for single in singles:
		if grid[single[0]][single[1]] == 1:
			solution.append(paint_square(single[0], single[1], 0))

	return solution
"""
N, M, grid = readfile("logo.in")
# N, M, grid = readfile("learn_and_teach.in")
# N, M, grid = readfile("right_angle.in")
singles = extract_singles(grid, N, M)
stripes = extract_stripes(grid, N, M)
solution = solve_stripes(grid, N, M, stripes, singles)

out = open("logo_solution.out", "w+")
# out = open("learn_solution.out", "w+")
# out = open("right_solution.out", "w+")

out.write(str(len(solution)) + "\n")
out.writelines("\n".join(solution))

"""




import math
def shortest_path(ra,rb,ca,cb):
    return math.ceil(math.sqrt((ra-rb)**2 + (ca-cb)**2))


"""
order_warehouses = {'W1':[0,0,1],'W2':[0,0,1],'W3':[0,0,1],'W4':[0,0,1]}
warehouses = {'W1':{'coordinates':(0,0)},'W2':{'coordinates':(16,0)},'W3':{'coordinates':(0,16)},'W4':{'coordinates':(16,16)}}
print center_of_mass(order_warehouses,warehouses)
"""

def center_of_mass(order_warehouses,dict_of_warehouses):
    list_of_warehouses = order_warehouses.keys()
    coordinates = [dict_of_warehouses[i]["coordinates"] for i in list_of_warehouses]
    x = [i for i,j in coordinates]
    y = [j for i,j in coordinates]
    centroid = (sum(x)/len(coordinates),sum(y)/len(coordinates))
    return centroid

