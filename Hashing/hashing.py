# a = [5,5,4,5,2,2,5,7,7,6]
# # 1st hashing
# dic = {}

# for i in range(len(a)):
#     if a[i] in dic:
#         dic[a[i]]+=1
#     else:
#         dic[a[i]]=1
# print(dic)

# # 2nd hashing
# hash_map = dict()

# for i in range(len(a)):
#     hash_map[a[i]] = hash_map.get(a[i],0)+1
# print(hash_map)





#############################################

a = [1,1,1,2,3,3,3,3,4,4,5,5,5,6,6,7,8,9,9,9,10,15]
b = [1,2,3,4,5,6,7,8,9,10,12,66]
#### 1st technique
# hash_list = [0]*11
# for i in range(len(a)):
#     hash_list[a[i]]+=1
# print(hash_list)
# for j in range(len(b)):
#     if j < 0 or j > 10:
#         print(0)
#     else:
#         # print(hash_list[b[j]])
#         print(f'{b[j]} : {hash_list[b[j]]}')
    

######### 2nd technique
dic = dict()
for i in range(len(a)):                 # this loop add list of a in dict
    if a[i] > 0 and a[i] <= 10:
        dic[a[i]] = dic.get(a[i],0)+1
print(dic)
for j in range(len(b)):                 # this loop check list of b count in list a using dict
    if b[j] in dic:
        print(f'{b[j]} : {dic[b[j]]}')