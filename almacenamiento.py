def maximizar(As, D):
    As = mergeSort(As)
    total = 0
    secuencia = []

    i = 0

    while total < D and i < len(As):
        if total + As[i][1] <= D:
            total =  total + As[i][1]
            secuencia.append(As[i])
        else:
            return secuencia

        i = i + 1

#------------------------------------------------------------------
#                            Merge Sort
#------------------------------------------------------------------
def mergeSort(A): 
    if len(A) >1: 
        mid = len(A) // 2 
        left = A[:mid]  
        right = A[mid:] 
  
        mergeSort(left) 
        mergeSort(right) 
        i = j = k = 0
          
        while i < len(left) and j < len(right): 
            if left[i][1] < right[j][1]: 
                A[k] = left[i] 
                i = i + 1
            else: 
                A[k] = right[j] 
                j = j + 1
            k+= 1
          
        while i < len(left): 
            A[k] = left[i] 
            i = i + 1
            k = k + 1
          
        while j < len(right): 
            A[k] = right[j] 
            j = j + 1
            k = k + 1

    return A