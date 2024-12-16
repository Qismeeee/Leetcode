def kth_symbol(n, k):
    if n == 1: return 0
    
    mid = 2 ** (n-2)
    
    if k <= mid:
        return kth_symbol(n-1, k)
    else:
        return 1-kth_symbol(n-1, k-mid)
        
solution = kth_symbol(3,3)
print(solution)