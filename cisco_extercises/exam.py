class entry(object):
    def __init__(self, v=0, dist=0):
        self.v = v
        self.dist = dist
 
 
def solveSnakesNLaddersPro(matrixSize1, maxDice1, numCoordinates1, startPoint1, endPoint1):
    visited = [False] * matrixSize1
    queue = [] 
    visited[0] = True
    queue.append(entry(0, 0))
 
    qe = entry()
    while queue:
        qe = queue.pop(0)
        v = qe.v 
 
        if v == matrixSize1 - 1:
            break
 
        j = v + 1
        while j <= v + maxDice1 and j < matrixSize1:
            if visited[j] is False:
                a = entry()
                a.dist = qe.dist + 1
                visited[j] = True
                a.v = endPoint1 if endPoint1 != -1 else j
 
                queue.append(a)
 
            j += 1

    return [qe.dist]

