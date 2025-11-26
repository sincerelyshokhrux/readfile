def reverse(z):

    new = []
    
 
    for i in range(len(L) - 1, -1, -1):
        if isinstance(L[i], list):
           
            reversed_inner = []
            for j in range(len(L[i]) - 1, -1, -1):
                reversed_inner.append(L[i][j])
            new.append(reversed_inner)
        else:
            new.append(L[i])
    
    
    L.clear()
    for element in new:
        L.append(element)
    
L = [[1, 2], [3, 4], [5, 6, 7]]
reverse(L)
print(L) 