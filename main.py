# Python program to print successor and predecessor of given subset
# using rank and unrank methods
# Author Damian Lasecki

class PermutationSetup(object):
    def __init__(self, vertex, nextPos):
        self.vertex = vertex
        self.nextPos = nextPos

    def factorial(self, n):
        fact = 1
        for i  in range(1, n+1):
            fact = fact * i
        return fact
    
    def permUnrank(self, r, n):
        T = [None, 1] + ([None] * (n-1))
        r2 = 0
        for j in range(2, n + 1, 1):
            r1 = int((r * self.factorial(j))/ self.factorial(n))
            k = r1 - (j * r2)
            if r2 % 2 == 0:
                for i in range(j - 1, j - k -1, -1):
                    T[i + 1] = T[i]
                T[j-k] = j
            else:
                for i in range(j -1,  k + 1 - 1, -1):
                    T[i+1] = T[i]
                T[k+1] = j
            r2 = r1
        T = T[1:]
        return T

    def permRank(self, T, n):
        # hardcode to adjust indexes
        T.insert(0, None)
        
        r  = 0
        for j in range(2, n + 1, 1):
            k = 1
            i = 1 
            while T[i] != j:               
                if T[i] < j:
                    k = k + 1
                i = i + 1
            if r % 2 == 0:
                r = j * r + j - k
            else: 
                r = j * r + k - 1
        return r    

    def getSuccessorOrPredecessor(self):
        n = len(self.vertex)
        rank = self.permRank(self.vertex, n)
        if (rank == 0 and self.nextPos == -1 ):
            print("Can't get predecessor of the first element")
            return 
        else:
            newVector = self.permUnrank(rank + self.nextPos, n)
            return newVector


if __name__ == '__main__':

    vertex = list(map(int, input("Please type vertex as: num1, num2, num3, numx: ").split(',')))
    nextPos = int(input("Choose if you want to get successor or predecessor. Type 1 to get successor and -1 to get predecessor, respectively:  "))
  
    if vertex and nextPos:
        permutationSetup = PermutationSetup(vertex, nextPos)
        print(permutationSetup.getSuccessorOrPredecessor())
    else:
        print("Bad arguments")
