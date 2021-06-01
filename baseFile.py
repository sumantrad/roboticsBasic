#localize (sense, tracking and state estimation)
#Planner
#Smoother
#Controller






grid = [[0,0,1,0,0,0],
		[0,0,1,0,0,0],
		[0,0,0,0,1,0],
		[0,0,1,1,1,0],
		[0,0,0,0,1,0]]
init = [0,0]
goal = [len(grid)-1, len(grid[0])-1]
delta =[[-1,0],
		[0,-1],
		[1,0],
		[0,1]]
delta_name = ['^','<','v','>']
cost = 1

def search_path(grid,init,goal,delta):
	open_list =[] #convert this to heap
	path =[]
	path_length = 0
	explored =[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
	explored_seq = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
	path_graph = [['' for i in range(len(grid[0]))] for j in range(len(grid))]
	parent_array = [] #convert to linked list
	explored_counter = 0
	open_list.append([0,init[0],init[1]])
	explored[init[0]][init[1]] = 1
	explored_seq[init[0]][init[1]] = explored_counter
	parent_array.append([init[0],init[1],-1,-1])
	while len(open_list)>0:
		next_node = open_list.pop(0)
		path_length = next_node[0]
		path.append(next_node)
		#path_graph[next_node[1]][next_node[2]] = '0'
		if next_node[1]==goal[0] and next_node[2]==goal[1]:
			return get_parent(init, goal,parent_array)
		f = [next_node[1],next_node[2]]
		for neighbor in neighbors(next_node, grid, delta):
			sequence = path_length + 1
			if grid[neighbor[0]][neighbor[1]] != 1:
				if explored[neighbor[0]][neighbor[1]] != 1:
					open_list.append([sequence,neighbor[0],neighbor[1]])
					explored[neighbor[0]][neighbor[1]] = 1
					explored_counter += 1
					explored_seq[neighbor[0]][neighbor[1]] = explored_counter
					parent_array.append([neighbor[0],neighbor[1],f[0],f[1]])
	return 'fail'
	
#this should be heap
def find_min(_list):
	min = _list[0]
	for i in range(len(_list)):
		if _list[i][0]<min[0]:
			min = _list[i]
	return min

#use map here
def neighbors(_node, grid, delta):
	_neighbors = []
	for i in range(len(delta)):
		if (delta[i][0]+_node[1]) >= 0 and (delta[i][0] +_node[1]) < len(grid) and (delta[i][1] +_node[2]) >= 0 and (delta[i][1] + _node[2]) < len(grid[0]):
			_neighbors.append([delta[i][0] + _node[1], delta[i][1] + _node[2]])
	return _neighbors

#use a linked list
def get_parent(init,goal,parent_array,path=[]):
	if goal[0]==init[0] and goal[1]==init[1]:
		path.append(init)
		#print(init)
		return path
	for node in parent_array:
		if node[0]==goal[0] and node[1]==goal[1]:
			path.append([node[0],node[1]])
			#print([node[0],node[1]])
			return get_parent(init,[node[2],node[3]],parent_array)
			
def showOnGrid(path, grid, delta, delta_name):
	path_graph = [['' for i in range(len(grid[0]))] for j in range(len(grid))]
	for i in range(len(path)-1):
		for j in range(len(delta)):
			if path[i][0] == (path[i+1][0] + delta[j][0]) and path[i][1] == (path[i+1][1] + delta[j][1]):
				path_graph[path[i+1][0]][path[i+1][1]] = delta_name[j]
	return path_graph


print(showOnGrid(search_path(grid,init,goal,delta), grid, delta, delta_name))
		