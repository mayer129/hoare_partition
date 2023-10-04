A = [13, 19, 9, 5, 12 ,8, 7, 4, 11, 2, 6, 21]
first_index = 0
last_index = 11

def hoare_partition(A, p, r):
    x = A[p]
    i = p-1
    j = r+1
    while True:
        print(i)
        print(j)
        print(A)
        while True:
            j = j-1
            if (A[j]<=x): break
        while True:
            i = i+1
            if (A[i]>=x): break
        if i < j:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
        else:
            return j
    
    
    
    
print(hoare_partition(A, first_index, last_index))