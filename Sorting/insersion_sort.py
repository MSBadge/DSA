# Insersion sort
def insersion(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i-1
        while j >= 0 and num[j]> key:
            num[j+1] = num[j]
            j-=1
        num[j+1] = key
    return num



a = [7,8,6,4,1,2,18,9]
print(insersion(a))