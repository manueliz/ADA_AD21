
from collections import defaultdict

class Graph:

	
	def __init__(self):

	
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u,v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] # * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge("rosario","petroleo")
g.addEdge("rosario", "tacuba")
g.addEdge("tacuba","tacubaya")
g.addEdge("tacuba","hidalgo")
g.addEdge("tacubaya","mixcoac")
g.addEdge("tacubaya","medico")
g.addEdge("tacubaya","balderas")
g.addEdge("mixcoac","tacubaya")
g.addEdge("mixcoac","zapata")
g.addEdge("zapata","mixcoac")
g.addEdge("zapata","medico")
g.addEdge("zapata","ermitar")
g.addEdge("ermitar","zapata")
g.addEdge("ermitar","chabacano")
g.addEdge("ermitar","atlalilco")
g.addEdge("atlalilco","ermitar")
g.addEdge("atlalilco","santaanita")
g.addEdge("santaanita","chabacano")
g.addEdge("santaanita","atlalilco")
g.addEdge("santaanita","jamaica")
g.addEdge("chabacano","medico")
g.addEdge("chabacano","ermitar")
g.addEdge("chabacano","suarez")
g.addEdge("chabacano","jamaica")
g.addEdge("jamaica","pantitlan")
g.addEdge("jamaica","santaanita")
g.addEdge("jamaica","candelaria")
g.addEdge("jamaica","chabacano")
g.addEdge("pantitlan","sanlazaro")
g.addEdge("pantitlan","jamaica")
g.addEdge("pantitlan","oceania")
g.addEdge("oceania","pantitlan")
g.addEdge("oceania","sanlazaro")
g.addEdge("oceania","consulado")
g.addEdge("consulado","martincarrera")
g.addEdge("consulado","raza")
g.addEdge("consulado","morelos")
g.addEdge("consulado","oceania")
g.addEdge("raza","deportivo")
g.addEdge("raza","petroleo")
g.addEdge("raza","consulado")
g.addEdge("raza","guerrero")
g.addEdge("petroleo","raza")
g.addEdge("petroleo","deportivo")
g.addEdge("petroleo","raza")
g.addEdge("deportivo","petroleo")
g.addEdge("deportivo","raza")
g.addEdge("deportivo","martincarrera")
g.addEdge("martincarrera","consulado")
g.addEdge("martincarrera","deportivo")
g.addEdge("guerrero","garibaldi")
g.addEdge("guerrero","hidalgo")
g.addEdge("hidalgo","bellasartes")
g.addEdge("hidalgo","balderas")
g.addEdge("hidalgo","guerrero")
g.addEdge("hidalgo","tacuba")
g.addEdge("balderas","tacubaya")
g.addEdge("balderas","medico")
g.addEdge("balderas","hidalgo")
g.addEdge("balderas","chabacano")
g.addEdge("garibaldi","morelos")
g.addEdge("garibaldi","guerrero")
g.addEdge("garibaldi","bellasartes")
g.addEdge("bellasartes","garibaldi")
g.addEdge("bellasartes","hidalgo")
g.addEdge("bellasartes","agua")
g.addEdge("bellasartes","suarez")
g.addEdge("agua","balderas")
g.addEdge("agua","suarez")
g.addEdge("agua","chabacano")
g.addEdge("agua","bellasartes")
g.addEdge("suarez","chabacano")
g.addEdge("suarez","candelaria")
g.addEdge("suarez","bellasartes")
g.addEdge("suarez","agua")
g.addEdge("candelaria","jamaica")
g.addEdge("candelaria","sanlazaro")
g.addEdge("candelaria","suarez")
g.addEdge("candelaria","morelos")
g.addEdge("sanlazaro","pantitlan")
g.addEdge("sanlazaro","morelos")
g.addEdge("sanlazaro","candelaria")
g.addEdge("sanlazaro","oceania")
g.addEdge("morelos","candelaria")
g.addEdge("morelos","sanlazaro")
g.addEdge("morelos","consulado")
g.addEdge("morelos","garibaldi")


print ("Distancia Grafos"
				" (empezando desde rosarito)")
g.BFS("rosario")

# This code is contributed by Neelam Yadav
