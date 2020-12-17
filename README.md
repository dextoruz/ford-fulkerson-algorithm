# ford-fulkerson-algorithm
### Python implemented Ford Fulkerson Algorithm to find maximum flow with graphical representation.

## Dependencies ##

* [graphviz](https://pypi.org/project/graphviz/)
* [pydot](https://pypi.org/project/pydot/)
* sudo apt install graphviz 

__Input:__
```
    Graph Name = {
      'node': [ False (visited), [ 'node'(edgeNode), capacity, current-flow ] ] }
```


``` javascript
  # Example
   graph = {
    'A': [False,['B',10,0],['C',10,0]],
    'B': [False,['D',4,0],['E',8,0]],
    'C': [False,['F',9,0]],
    'D': [False,['F',10,0]],
    'E': [False,['D', 6,0],['F',10,0]],
    'F': [False]
    }
```


__Output:__
  `Maximum Flow  = 19`

![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/0.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/1.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/2.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/3.png)
![q](https://github.com/linxnerd/ford-fulkerson-algorithm/blob/master/Graphs/4.png)
