
def binary_search(list,p,r,x):
    ''' Θ(log(n)) '''
    if p > r:
        return -1
    q = math.floor((p+r)/2)
    if list[q] == x:
        return q
    elif x < list[q]:
        return binary_search(list,p,q-1,x)
    elif x > list[q]:
        return binary_search(list,q+1,r,x)
       
