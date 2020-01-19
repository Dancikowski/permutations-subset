# Python program to print successor and predecessor of given subset
# using rank and unrank methods
# Author Damian Lasecki

class PermutationSetup(object):
    def __init__(self, vertex, k, n, nextPos):
        self.vertex = vertex
        self.k = k
        self.n = n
        self.nextPos = nextPos

    def newton(self, n, k):
        if k == 0 or k == n:
            return 1
        else:
            return n/ k * self.newton(n - 1, k - 1)

    def kSubsetRevDoorRank(self, T, k):
        r = - (k % 2)
        s = 1
        for i in range(k - 1, -1, -1):
            newton =  self.newton(T[i], i + 1)
            r = r + (s * newton)
            s = -s
        return r

    def kSubsetRevDoorUnrank(self, r, k, n):
        x = n
        T = [None] * k
        for i in range(k - 1, -1, -1):
            while self.newton(x, i + 1) > r:
                x = x - 1
            T[i] = x + 1
            r = self.newton(x + 1, i + 1) - r - 1
        return T


    def getSuccessorOrPredecessor(self):
        rank = self.kSubsetRevDoorRank(self.vertex, self.k)
        if (rank == 0 and self.nextPos == -1 ):
            print("Can't get predecessor of the first element")
            return 
        else:
            newVector = self.kSubsetRevDoorUnrank(rank + self.nextPos, self.k, self.n)
            return newVector


if __name__ == '__main__':

    vertex = list(map(int, input("Please type vertex as: num1, num2, num3, numx: ").split(',')))
    k = int(input("Please type lenght of vertex: "))
    n = int(input("Please type range of permutation: "))
    nextPos = int(input("Choose if you want to get successor or predecessor. Type 1 to get successor and -1 to get predecessor, respectively:  "))
  
    if vertex and k and n and nextPos:
        permutationSetup = PermutationSetup(vertex, k, n, nextPos)
        print(permutationSetup.getSuccessorOrPredecessor())
    else:
        print("Bad arguments")



