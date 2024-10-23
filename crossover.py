import random 

def cycle_crossover(A, B):
    n = len(A)
    child = [None] * n
    case = random.choice([0,1])
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

        while(None in child):
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
       
            if None not in child:
                break
            i = child.index(None)
            child[i] = A[i]
            cycle = [A[i]]
            n = B.index(A[i])
            child[n] = A[n]
            cycle.append(A[n])
            while(cycle[-1] != cycle[0]):
                n = B.index(cycle[-1])
                child[n] = A[n]
                cycle.append(A[n])

        return child

    if(case == 1):
        # the first cycle
        child[0] = B[0]
        cycle = [B[0]]
        n = A.index(B[0])
        child[n] = B[n]
        cycle.append(B[n])
        while(cycle[-1] != cycle[0]):
            n = A.index(cycle[-1])
            child[n] = B[n]
            cycle.append(B[n])

        while(None in child):
            i = child.index(None)
            child[i] = A[i]
            cycle = [A[i]]
            n = B.index(A[i])
            child[n] = A[n]
            cycle.append(A[n])
            while(cycle[-1] != cycle[0]):
                n = B.index(cycle[-1])
                child[n] = A[n]
                cycle.append(A[n])
       
            if None not in child:
                break
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
        
        return child

A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z', 'Y', 'Q']
B = ['A', 'D', 'G', 'B', 'F', 'E', 'C', 'Y', 'Z', 'Q']

print(cycle_crossover(A, B))


