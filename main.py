from Cities import City, SOUDERTON, NEWYORK, PHILADELPHIA, BOSTON, PITTSBURGH, TRENTON, DOVER, RICHMOND
# Edges for graph
routes = {
  SOUDERTON: [PHILADELPHIA, TRENTON, NEWYORK, DOVER, RICHMOND, PITTSBURGH, BOSTON],
  NEWYORK: [PHILADELPHIA, BOSTON, PITTSBURGH, TRENTON, DOVER, RICHMOND],
  PHILADELPHIA: [NEWYORK, BOSTON, PITTSBURGH, TRENTON, DOVER, RICHMOND],
  BOSTON: [NEWYORK, PHILADELPHIA, PITTSBURGH, TRENTON, DOVER, RICHMOND],
  PITTSBURGH: [NEWYORK, PHILADELPHIA, BOSTON, TRENTON, DOVER, RICHMOND],
  TRENTON: [NEWYORK, PHILADELPHIA, BOSTON, PITTSBURGH, DOVER, RICHMOND],
  DOVER: [NEWYORK, PHILADELPHIA, BOSTON, PITTSBURGH, TRENTON, RICHMOND],
  RICHMOND: [NEWYORK, PHILADELPHIA, BOSTON, PITTSBURGH, TRENTON, DOVER]
}
# Returns city object from a string city name
StringToCity = {
  "SOUDERTON": SOUDERTON,
  "NEWYORK": NEWYORK,
  "PHILADELPHIA": PHILADELPHIA,
  "BOSTON": BOSTON,
  "PITTSBURGH": PITTSBURGH,
  "TRENTON": TRENTON,
  "DOVER": DOVER,
  "RICHMOND": RICHMOND
}

# Finds all posible paths to all cities
def CalculateAllPaths(adjacencyList, source, destination):
    Visited = {
        SOUDERTON: False,
        NEWYORK: False,
        PHILADELPHIA: False,
        BOSTON: False,
        PITTSBURGH: False,
        TRENTON: False,
        DOVER: False,
        RICHMOND: False
    }
    paths = []
    currentPath = []
    currentPath.append(source.Name)
    _dfs(adjacencyList, source, destination, Visited, currentPath, paths)
    return paths

# depth first search to all cities to find all routes
def _dfs(graph, source, destination, Visited, currentPath, paths):
    if source == destination:
        paths.append(currentPath[:])  
        return
    Visited[source] = True  
    for city in graph[source]:  
        if not Visited[city]:
            currentPath.append(city.Name)
            _dfs(graph, city, destination, Visited, currentPath, paths)
            currentPath.pop()
    Visited[source] = False 

# Checks if the path is valid by checking if the total volunteers through all cities past is greater than the needed sample size.
def ValidPath(path, DiseaseName, SampleSize):
    TotalSample = 0
    for city in path:
        TotalSample += StringToCity[city].DiseasesPopulation[DiseaseName]
    return TotalSample >= SampleSize   
# Finds the Distance from start to end of a given path
def PathDistance(path):
    TotalDistance = 0
    i = 0
    while i < len(path)-1:
        TotalDistance += StringToCity[path[i]].Distances[path[i+1]]
        i += 1
    return TotalDistance

# Uses a linear search to go through all paths found to find the one which satisfies the needed sample and has the shortest path
def FindBestPath(DiseaseName, SampleSize):
    paths = []
    BestDistance = float('inf')
    for destination in routes[SOUDERTON]:
        paths += CalculateAllPaths(routes, SOUDERTON, destination)
    
    for path in paths:
        if ValidPath(path, DiseaseName, SampleSize) and (PathDistance(path) < BestDistance):
            BestDistance = PathDistance(path)
            BestPath = path

    return (BestPath, BestDistance)

# Finds the max number of patients willing to participate in clinical studies through all cities included
def MaxPatients(DiseaseName):
    TotalPatients = 0
    for city in routes[SOUDERTON]:
        TotalPatients += city.DiseasesPopulation[DiseaseName]
    return TotalPatients

# Returns a list of the number of volunteers from all the cities visited
def VolunteersInEachCity(path, DiseaseName):
    PatientsInCities = []
    for city in path[0]:
        PatientsInCities.append(StringToCity[city].DiseasesPopulation[DiseaseName])
    return PatientsInCities