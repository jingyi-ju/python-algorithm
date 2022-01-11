
from helper import swap

# **************************************************************************************************************

def selection_sort(list):
  ''' best and worst case runtime: Θ(n^2) '''
    for i in range(0,len(list)-1):              # after n-1 iterations, n-1 smallest elements in L subarray
        min = i
        for j in range(i+1,len(list)):          # elements are compared in both B-case and W-case
            if list[j] < list[min]:             
                min = j
        swap(list,min,i)

# **************************************************************************************************************
