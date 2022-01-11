
def insertion_sort(list):  
  ''' for each element aj, jϵ[1,n-1], compare aj with all elements in left subarray (sorted), ai, iϵ[j-1,j-2...0], 
      shift each aj right until aj is smaller than ai, then insert aj at this position'''
  
  ''' best case: Θ(n) '''
  ''' worst case: Θ(n^2) '''
  
    for j in range(1, len(list)):           # after n-1 iterations, n elements originally at these positions are sorted
        key = list[j]                      
        i = j - 1                          
        while (i >= 0) & (list[i] > key):   # best case: tj = 1, worst case: tj = j
            list[i + 1] = list[i]           
            i = i - 1;                     
        list[i + 1] = key;                 
    
