# ford-fulkerson-algorithm
### Python implemented Ford Fulkerson Algorithm to find maximum flow with graphical representation.

## Prerequisites ##

* [graphviz](https://pypi.org/project/graphviz/)
* [pydot](https://pypi.org/project/pydot/)


__Input:__
    __Graph Name__ __= {'node'__ __: [False(visited), [__ __'node'(edgeNode)__, __capacity__,__current-flow] ] }__


   __graph = {
    'A': [False,['B',10,0],['C',10,0]],
    'B': [False,['D',4,0],['E',8,0]],
    'C': [False,['F',9,0]],
    'D': [False,['F',10,0]],
    'E': [False,['D', 6,0],['F',10,0]],
    'F': [False]
}`__

__Output:__
  `Maximum Flow  = 19`

![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/0.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/1.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/2.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/3.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/4.png)
