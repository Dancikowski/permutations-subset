# Python program to print successor and predecessor of given subset
# using rank and unrank methods
# Author Damian Lasecki

"""HELLO CLI
Usage:
  main.py --vertex=VERTEX --k=<k> --n=<n> --nextPos=<nextPos>

Options:
  -h --help            show this help message and exit
  --vertex=VERTEX      Comma separated list of numbers
  --k=<k>              Number describes length of vertex
  --n=<n>              Number describes range of numbers
  --nextPos=<nextPos>  Describes if we want to get successor (1) or predecessor (-1)
"""

from docopt import docopt

class PermutationSetup(object):
    def __init__(self, vertex, k, n, nextPos):
        self.vertex = vertex
        self.k = k
        self.n = n
        self.nextPos = nextPos

    def Newton(self, n, k):

        result = 1
        for i in range( 1, k+1 ):
            result = result * ( n - i + 1 ) / i
        return result

        t = int( raw_input() )

        for i in range(t):
            n,k = map( int, raw_input().split() )
            if k == 0 or k == n : print('1')
            else : print(Newton(n,k))

    def kSubsetRevDoorRank(self, T, k):
        r = - (k % 2)
        s = 1
        for i in range(k - 1, -1, -1):
            newton =  self.Newton(T[i], i + 1)
            r = r + (s * newton)
            s = -s
        return r

    def kSubsetRevDoorUnrank(self, r, k, n):
        x = n
        T = range(k)
        for i in range(k - 1, -1, -1):
            while(self.Newton(x, i + 1) > r):
                x = x - 1
            T[i] = x + 1
            r = self.Newton(x + 1, i + 1) - r - 1
        return T


    def getSuccessorOrPredecessor(self):
        rank = self.kSubsetRevDoorRank(self.vertex, self.k)
        newVector = self.kSubsetRevDoorUnrank(rank + self.nextPos, self.k, self.n)
        return newVector


if __name__ == '__main__':
    args = docopt(__doc__)
    args['--vertex'] = [int(x) for x in args['--vertex'].split(',')]
    vertex, k, n, nextPos = args['--vertex'], int(args['--k']), int(args['--n']), int(args['--nextPos'])

    if vertex and k and n and nextPos:
        permutationSetup = PermutationSetup(vertex, k, n, nextPos)
        print(permutationSetup.getSuccessorOrPredecessor())
    else:
        print(args)



