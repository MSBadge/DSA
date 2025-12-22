# Selection sort Accending order

def selection(num):
    for i in range(len(num)):
        minindex = i
        for j in range(i+1, len(num)):
            if num[j] < num[minindex]:
                minindex = j
        num[i], num[minindex] = num[minindex], num[i]
    return num

a = [7,3,9,4,1,2,8]
print(selection(a))





# Selection sort Decending order

def selection(num):
    n = len(num)
    for i in range(n):
        maxindex = i
        for j in range(i+1,n):
            if num[j] > num[maxindex]:
                maxindex = j
        num[i], num[maxindex] = num[maxindex], num[i]
    return num

a = [7,3,9,4,1,2,8]
print(selection(a))
