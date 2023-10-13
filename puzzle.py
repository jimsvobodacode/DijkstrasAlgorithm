from dijkstra import Dijkstra, Vertex

class Puzzle:

    def Process(self):
        self.InitializeData()
        dijkstra1 = Dijkstra(self._vertices, "A")
        dijkstra1.Process()
        dijkstra1.PrintPath(self.GetVertexByName("B"))
        d1 = self.GetVertexByName("B").distance
        print()

        self.InitializeData()
        dijkstra2 = Dijkstra(self._vertices, "B")
        dijkstra2.Process()
        dijkstra2.PrintPath(self.GetVertexByName("C"))
        d2 = self.GetVertexByName("C").distance
        print()
        print(f"Total Distance: {(d1 + d2) * .621} miles")


    def GetVertexByName(self, name):
        for v in self._vertices:
            if v.name == name:
                return v
        return None

    def InitializeData(self):
        self._vertices = []
        self._vertices.append(Vertex("A", 41.2379, 96.0156))
        self._vertices.append(Vertex("B", 41.2588, 96.0130))
        self._vertices.append(Vertex("C", 41.244, 96.007))

        self._vertices.append(Vertex("Other1", 41.244, 96.013))
        self._vertices.append(Vertex("Other2", 41.238, 96.007))
        self._vertices.append(Vertex("Other3", 41.2486, 96.012))
        self._vertices.append(Vertex("Other4", 41.247, 96.006))
        self._vertices.append(Vertex("Other5", 41.2473, 96.0071))
        self._vertices.append(Vertex("Other6", 41.258, 96.007))

        #A
        v = self.GetVertexByName("A")
        v.adjacent.append(self.GetVertexByName("Other1"))
        v.adjacent.append(self.GetVertexByName("Other2"))

        #B
        v = self.GetVertexByName("B")
        v.adjacent.append(self.GetVertexByName("Other5"))
        v.adjacent.append(self.GetVertexByName("Other6"))

        #C
        v = self.GetVertexByName("C")
        v.adjacent.append(self.GetVertexByName("Other1"))
        v.adjacent.append(self.GetVertexByName("Other2"))
        v.adjacent.append(self.GetVertexByName("Other4"))

        #Other1
        v = self.GetVertexByName("Other1")
        v.adjacent.append(self.GetVertexByName("A"))
        v.adjacent.append(self.GetVertexByName("C"))
        v.adjacent.append(self.GetVertexByName("Other3"))

        #Other2
        v = self.GetVertexByName("Other2")
        v.adjacent.append(self.GetVertexByName("A"))
        v.adjacent.append(self.GetVertexByName("C"))

        #Other3
        v = self.GetVertexByName("Other3")
        v.adjacent.append(self.GetVertexByName("Other1"))
        v.adjacent.append(self.GetVertexByName("Other4"))
        v.adjacent.append(self.GetVertexByName("Other5"))

        #Other4
        v = self.GetVertexByName("Other4")
        v.adjacent.append(self.GetVertexByName("C"))
        v.adjacent.append(self.GetVertexByName("Other3"))

        #Other5
        v = self.GetVertexByName("Other5")
        v.adjacent.append(self.GetVertexByName("B"))
        v.adjacent.append(self.GetVertexByName("Other3"))
        v.adjacent.append(self.GetVertexByName("Other6"))

        #Other6
        v = self.GetVertexByName("Other6")
        v.adjacent.append(self.GetVertexByName("B"))
        v.adjacent.append(self.GetVertexByName("Other5"))


    
        