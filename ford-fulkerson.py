from copy import deepcopy
import pydot, os

class FordFulkersonAlgorithm:
    def __init__(self,s,d,g):
        self.src = []
        self.src.append(s)
        self.src.append(0)
        self.src.append(0)
        self.dest = d
        self.augPaths = []
        self.augPathsGraph = []
        self.graph = g
        self.createGraph()


    def createGraph(self, graph = None,augPath=None,flag=0):
        self.G = pydot.Dot(graph_name="ford", graph_type="digraph",rankdir="LR",nodesep=0.5, pad=.1)
        if graph == None and augPath == None:
            for k in self.graph:
                node = pydot.Node(k,fontname="Bold",style="filled", fillcolor="green")
                self.G.add_node(node)
            for k, j in  self.graph.items():
                for e in range (1,len(j)):
                    st = str(j[e][2])+'/' + str(j[e][1])
                    edge = pydot.Edge(k, j[e][0],label=st,fontname="Bold",arrowhead='vee')
                    self.G.add_edge(edge)
            self.augPathsGraph.append(self.G)
        elif augPath == None:
            G = pydot.Dot(graph_name="ford", graph_type="digraph",rankdir="LR",nodesep=.5, pad=.1)
            for k in graph:
                node = pydot.Node(k,fontname="Bold",style="filled", fillcolor="green")
                G.add_node(node)
            for k, j in  graph.items():
                for e in range (1,len(j)):
                    st = str(j[e][2])+'/' + str(j[e][1])
                    edge = pydot.Edge(k, j[e][0],label=st,fontname="Bold",arrowhead='vee')
                    G.add_edge(edge)
#             im = Image(G.create_png())
#             display(im)
            if flag != 0:
                self.augPathsGraph.append(G)
        else:
            G = pydot.Dot(graph_name="ford", graph_type="digraph",rankdir="LR",nodesep=.5, pad=.1)
            for k in graph:
                node = pydot.Node(k,fontname="Bold",style="filled", fillcolor="green")
                G.add_node(node)
            temp = []
            for k, j in  graph.items():
                for e in range (1,len(j)):
                    st = str(j[e][2])+'/' + str(j[e][1])
                    edge = pydot.Edge(k, j[e][0],label=st,fontname="Bold",arrowhead='vee')
                    G.add_edge(edge)
            for  i in range(len(augPath)-1):
                value = self.graph[augPath[i][0]]
                for j in range(1,len(value)):
                    if value[j][0] == augPath[i+1][0]:
                        temp.append(str(value[j][2])+'/'+str(value[j][1]))
            for i in range(len(augPath)-1):
                G.del_edge(augPath[i][0],augPath[i+1][0])
                edge = pydot.Edge(augPath[i][0],augPath[i+1][0],label=temp[i],\
                                  fontname="Bold",arrowhead='vee',color='red')
                G.add_edge(edge)
            self.augPathsGraph.append(G)

    def showGraph(self, graph=None):
        if graph == None:
            im = Image(self.G.create_png())
            display(im)
        else:
            self.createGraph(graph)

    def checkPath(self,path, graph3,mini):
        i = 0
        src = path[i][0]
        dest = path[-1][0]
        while src != dest:
            for n in range(1, len(graph3[src])):
                if graph3[src][n][0] == path[i+1][0]:
                    if graph3[src][n][2]+mini > graph3[src][n][1] or \
                    graph3[src][n][2] == graph3[src][n][1] : #n = node
                        return False
                    break
            i+=1
            src = path[i][0]
        return True

    def updateWeigth(self,s , d, mi):
        for i in range(1, len(self.graph[s])):
            if self.graph[s][i][0] == d:
                self.graph[s][i][2] += mi
                return 0

    def augumentedPaths(self, src, dest, graph, path=[]):
        graph[src[0]][0] = True
        path.append(src)
        src = src[0]
        if src == dest:
            temp = deepcopy(path)
            self.augPaths.append(temp)
        else:
            for i in range(1, len(graph[src])):
                if graph[graph[src][i][0]][0] == False:
                    self.augumentedPaths(graph[src][i], dest, graph , path)
        path.pop()
        graph[src][0] = False

    def maximumFlow(self):
        self.augumentedPaths(self.src, self.dest, self.graph)
        maxFlow = 0
        for p in self.augPaths:
            mini = []
            for j in range(1, len(p)):
                mini.append(p[j][1])
            mini = min(mini)
            if self.checkPath(p, self.graph, mini):
                maxFlow += mini
                for j in range(len(p)-1):
                    self.updateWeigth(p[j][0] , p[j+1][0],mini)
                self.createGraph(self.graph, p)
        self.createGraph(self.graph,None,1)
        return maxFlow


if __name__ == '__main__':
    graph = {
    'A': [False,['B',10,0],['C',10,0]],
    'B': [False,['D',4,0],['E',8,0]],
    'C': [False,['F',9,0]],
    'D': [False,['F',10,0]],
    'E': [False,['D', 6,0],['F',10,0]],
    'F': [False]
}
    src = 'A'
    dest = 'F'
    obj = FordFulkersonAlgorithm(src, dest, graph)
    print( "Maximum Flow = ", obj.maximumFlow())


    # print graphs
    j = 0
    for i in obj.augPathsGraph:
        if not os.path.exists('Graphs'):
            os.makedirs("Graphs")
        i.write_png('Graphs/'+ str(j)+'.png')
        # im = Image(i.create_png())
        j+=1
        # display(im)
