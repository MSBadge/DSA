# merge sort (divide and merge)

def merge_array(l,r):               # this function merge two sorted array
    result = []
    i = j = 0
    n, m, = len(l), len(r)
    while i < n and j < m:
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    if i < n :
        while i < n:
            result.append(l[i])
            i += 1
    if j < m:
        while j < m:
            result.append(r[j])
            j += 1
    return result
        
def div_array(arr):                 # this function divide array in two parts
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_half = div_array(left)
    right_halg = div_array(right)
    return merge_array(left_half,right_halg)



print(div_array([7,8,4,4,9,3,1,49,1,0]))