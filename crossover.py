import random 

A = [1, 2, 3, 4, 5, 6, 7, 8]
B = [2, 4, 6, 8, 7, 5, 3, 1]

def cycle_crossover(A, B):
    n = len(A)
    child = [None] * n
    case = random.choice([0,1])
    case = 0
    if(case == 0):
        # the first cycle
        child[0] = A[0]
        cycle = [A[0]]
        n = B.index(A[0])
        child[n] = A[n]
        cycle.append(A[n])
        while(cycle[-1] != cycle[0]):
            n = B.index(cycle[-1])
            child[n] = A[n]
            cycle.append(A[n])

        i = child.index(None)
        child[i] = B[i]
        cycle = [B[i]]
        n = A.index(B[i])
        child[n] = B[n]
        cycle.append(B[n])
        while(cycle[-1] != cycle[0]):
            n = A.index(cycle[-1])
            child[n] = B[n]
            cycle.append(B[n])

        print(child)

        


cycle_crossover(A, B)


