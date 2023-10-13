import math

# based on Data Structure and Algorithm Analysis in Java pp. 372-379
class Dijkstra:
    def __init__(self, vertices, startName):
        self._vertices = vertices
        self._startName = startName
     
    def Process(self):
        start = self.GetVertexByName(self._startName)
        start.distance = 0
        while self.UnknownExists():
            v = self.SmallestUnknownDistanceVertex()
            v.known = True
            for adj in v.adjacent:
                if adj.known == False:
                    distance = self.GetDistanceKm(v, adj)
                    if v.distance + distance < adj.distance:
                        adj.distance = v.distance + distance
                        adj.previousVertex = v

    # Haversine formula
    def GetDistanceKm(self, vertex1, vertex2):
        R = 6371
        dlat = self.deg2rad(vertex1.lat - vertex2.lat)
        dlon = self.deg2rad(vertex1.lon - vertex2.lon)
        a = math.sin(dlat/2) ** 2 + math.cos(self.deg2rad(vertex1.lat)) * math.cos(self.deg2rad(vertex2.lat)) * math.sin(dlon/2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c
    
    def deg2rad(self, deg):
        return deg * (math.pi/180)
    
    def PrintPath(self, toDestination):
        if toDestination.previousVertex != None:
            self.PrintPath(toDestination.previousVertex)
            print(" to ", end='')
        print(toDestination.name, end='')

    def SmallestUnknownDistanceVertex(self):
        distance = math.inf
        smallest = None
        for v in self._vertices:
            if v.known == False and v.distance < distance:
                smallest = v
                distance = v.distance
        return smallest

    def UnknownExists(self):
        for v in self._vertices:
            if v.known == False:
             return True
        return False
    
    def GetVertexByName(self, name):
        for v in self._vertices:
            if v.name == name:
                return v
        return None
    

class Vertex:
   def __init__(self, name, lat, lon):
      self.name = name
      self.lat = lat
      self.lon = lon
      self.distance = math.inf
      self.known = False
      self.adjacent = []
      self.previousVertex = None