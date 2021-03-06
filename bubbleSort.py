from helper import swap

def bubble_sort(list):
  ''' best and worst case: Θ(n^2) '''
  
    for i in range(0, len(list) - 1):                # after n-1 iterations, n-1 largest elements in right subarray
        for j in range(0, len(list) - i -1):
            if list[j] > list[j + 1]:
                swap(list, j, j + 1)
               
def optimized_bubble_sort(list):
  ''' best case: Θ(n) '''
  ''' worst case: Θ(n^2) '''
  
    for i in range(0, len(list) - 1):
        sorted = True
        for j in range(0, len(list) - i -1):         # best case: exit after i=0 iteration
            if list[j] > list[j + 1]:
                swap(list, j, j + 1)
                sorted = False
        if sorted:
            break
 
