import json
import webbrowser
import os


"""
distances = {
	'A': {'B': 2, 'C': 5, 'D': 1},
	'B': {'A': 2, 'C': 3, 'D': 2},
	'C': {'A': 5, 'B': 3, 'D': 3, 'E': 1, 'F': 5},
	'D': {'A': 1, 'B': 2, 'C': 3, 'E': 1},
	'E': {'C': 1, 'D': 1, 'F': 2},
	'F': {'C': 5, 'E': 2}
}
"""


def dijkstra(graph):
	nodes = set()
	result = []  # to store the result before being save as .json file
	for n, _ in graph.items():
		nodes.add(n)

	for counter, n in enumerate(sorted(nodes)):
		unvisited = {node: None for node in nodes}  # using None as INFINITY
		previous = {node: None for node in nodes}
		visited = {}
		current = n
		currentDistance = 0
		unvisited[current] = currentDistance

		while True:
			for neighbour, distance in graph[current].items():
				if neighbour not in unvisited:
					continue
				newDistance = currentDistance + distance
				if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
					unvisited[neighbour] = newDistance
					previous[neighbour] = current
			visited[current] = currentDistance
			del unvisited[current]
			if not unvisited:
				break
			candidates = [node for node in unvisited.items() if node[1]]  # node is not None(NULL)
			current, currentDistance = min(candidates, key = lambda x: x[1])  # get the smallest distance of the visited nodes by comparing the second element of the tuple (x[1]) in each list's element

		result.append({'from': n})
		result[counter].update({'data': []})

		for k, v in sorted(visited.items()):  # k is the destination node and v is the shortest distance from n to k
			next_hop = temp = k
			while previous[temp] is not None:  # rewind back from the destination to the source to get the next hop for the original source
				next_hop = temp
				temp = previous[temp]
			result[counter]['data'].append({'to': k, 'distance': v, 'next_hop': next_hop})

	while True:
		LOCALHOST_DOCUMENT_ROOT_PATH = input('Input the absolute path to your localhost document root: ')
		LOCALHOST_DOCUMENT_ROOT_PATH = os.path.abspath(LOCALHOST_DOCUMENT_ROOT_PATH)

		if os.path.isdir(LOCALHOST_DOCUMENT_ROOT_PATH):
			break
		else:
			print('Directory doesn\'t exist')

	fp = open(LOCALHOST_DOCUMENT_ROOT_PATH + '/dijkstra/result.json', 'w')
	json.dump(result, fp, indent = 4)
	fp.close()
	webbrowser.open_new_tab('http://localhost/dijkstra')


if __name__ == "__main__":
	graph = {}
	currentNode = None

	print("-- Dijkstra's Algorithm --", "1. Insert node", "2. Update distance", "3. Show forwarding table", "0. Exit", sep = '\n')
	response = input()

	while response is not '0':
		if response is '1':
			currentNode = input("Insert new node: ")
			graph.update({currentNode: {}})
			while True:
				neighbour = input("Insert the neighbour of node " + currentNode + " (Type \"Exit\" to stop): ")
				if neighbour.lower() == "exit":
					break
				distance = input("Insert the distance from " + currentNode + " to " + neighbour + ": ")
				graph[currentNode].update({neighbour: float(distance)})
			""" This section of code is indented 1 tab more that it should be so the next elif can work
			elif response is '2':
				if currentNode is not None:
					neighbour = input("Insert the neighbour of node " + currentNode + ": ")
					distance = input("Insert the distance from " + currentNode + " to " + neighbour + ": ")

					#if type(distance) is int:
					graph[currentNode].update({neighbour: float(distance)})
					#elif type(distance) is float:
					#	graph[currentNode].update({neighbour: float(distance)})
					#else:
					#	print ("Distance should be a valid number")
				else:
					print("No node selected")
			"""
		elif response is '2':
			source = input("Input the source node: ")
			if source in graph:
				destination = input("Input the destination node: ")
				if destination in graph[source]:
					newDistance = input("Input the new distance from node " + source + " to " + destination + ": ")

					# if type(newDistance) is int:
					graph[source][destination] = float(newDistance)
					graph[destination][source] = float(newDistance)
					""" This section of code is indented 1 tab more that it should be so the next else can work
					elif type(newDistance) is float:
						graph[source][destination] = float(newDistance)
						graph[destination][source] = float(newDistance)
					else:
						print ("New distance should be a valid number")
					"""
				else:
					print("Unknown destination node")
			else:
				print("Unknown source node")
		elif response is '3':
			dijkstra(graph)
			break
		else:
			print('Unknown options')

		print("\n-- Dijkstra's Algorithm --", "1. Insert node", "2. Update distance", "3. Show forwarding table", "0. Exit",
		      sep = '\n')
		response = input()
