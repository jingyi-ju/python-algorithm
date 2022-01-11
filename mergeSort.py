
def merge(list, p, q, r):
    ''' theta(n) '''
    L = [list[i] for i in range(p, q + 1)]
    R = [list[j] for j in range(q + 1, r + 1)]
    i = 0
    j = 0
    for k in range(p, r + 1):
        if i >= len(L):
            list[k] = R[j]
            j = j + 1
        elif j >= len(R):
            list[k] = L[i]
            i = i + 1
        elif L[i] <= R[j]:
            list[k] = L[i]
            i = i + 1
        else:
            list[k] = R[j]
            j = j + 1

def merge_sort(list, p, r):
    ''' theta(n log(n)) '''
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(list, p, q)
        merge_sort(list, q + 1, r)
        merge(list, p, q, r)
         
