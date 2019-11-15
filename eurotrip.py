class Node:
    def __init__(self, name, i):
        self.city = name
        self.index = i

def printCities(arr):
    for node in arr:
        print(node.city)

def cCity(cities, queue):
    stringVersion = []
    for element in queue:
        stringVersion.append(cities[element].city);

    stringVersion.sort()

    #print(stringVersion[0])
    return stringVersion[0]

def cIndex(cities, city):
    for node in cities:
        if node.city == city:
            return node.index

#def khansAlgorithm(cities, adjacencyL, numEdges):
    #Add queue

inputFile = open("input.txt", "r")
inputList = inputFile.read().split("\n")
#print(inputList)

#Number of Cities
numberOfCities = int(inputList[0])
#Number of Edges
numberOfEdges = int(inputList[numberOfCities+1][2:])

#Array of City Nodes
arrayOfCities = []

for i in range(numberOfCities):
    arrayOfCities.append(Node(inputList[i+1], i))

#Dictionary adjacency list, KEY = City Name & VALUE = index
adjacencyList = {}

#Adding list to each city
for i in range(numberOfCities):
    adjacencyList[i] = []


#Putting values into the adjacency list
for i in range(numberOfEdges):
    #print(inputList[i+numberOfCities+2])
    city = int(inputList[i+numberOfCities+2][:1])
    edge = int(inputList[i+numberOfCities+2][2:])

    adjacencyList[edge].append(city)

#print("ADJACENCY LIST: ", end=" ")
#print(adjacencyList)

#Creating indegree list
indegree = []
for key in adjacencyList:
    indegree.append(len(adjacencyList[key]))

#print("NUM OF EDGES", end=" ")
#print(indegree)

queue = []
resultList = []

#Putting initial nodes with degree 0 into the queue
for i in range(len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

#print(indegree)
#While queue is not empty:
while len(queue) > 0:

    correctCity = ''
    correctIndex = None

    #If there are multiple degree 0's determine which to go first
    #Else only one element and put it in the ordering
    if len(queue) > 1:
        correctCity = cCity(arrayOfCities, queue)
        correctIndex = cIndex(arrayOfCities, correctCity)
        resultList.append(correctCity)
    else:
        correctCity = arrayOfCities[queue[0]].city
        correctIndex = queue[0]
        resultList.append(correctCity)

    for key in adjacencyList:
        if key != correctIndex:
            if correctIndex in adjacencyList[key]:
                adjacencyList[key].remove(correctIndex)
                indegree[key] -= 1
                if indegree[key] == 0:
                    queue.append(key)

    queue.pop(queue.index(correctIndex))

print(resultList)