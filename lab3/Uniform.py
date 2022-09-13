from queue import PriorityQueue
def uniform_cost_search(goal, start):
	global graph,cost
	# set the answer to max value
	answer = 10**8
	# create a priority queue
	pq = PriorityQueue()
	pq.put((0, start))
	
	# map to store visited node
	visited = {}

	while not pq.empty():
		u = pq.get()
		print(u)
		if (u[1] == goal):	
			# if the cost is less
			if (answer > u[0]):
				answer = u[0]
				return answer
		
		if u[1] not in visited :
			for i in range(len(graph[u[1]])):
				pq.put( (u[0] + cost[(u[1], graph[u[1]][i])], graph[u[1]][i]))
		# mark as visited
		visited[u[1]] = 1
	return answer



if __name__ == '__main__':
    graph,cost = [[] for i in range(8)],{}

    # add edge
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    goal = 6

    answer = uniform_cost_search(goal, 0)

    print("Minimum cost from 0 to 6 is = ",answer)
    
