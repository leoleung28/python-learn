a = [3,1,1,3,5,7]
b = [1,1,2,4,5]
dic = {}
ans = []
for i in a:
    if i in dic:  #通过字典的方式存放两个数组的元素及其出现次数
        dic[i][0] += 1
    else:
        dic[i] = [1,0]  #若字典中不存在，则创建新的键值对
for i in b:
    if i in dic:
        dic[i][1] += 1  #若b数组中有a数组的元素存在，更新记录
for i in dic:
    if (dic[i][1]!=0):
        num = min(dic[i])
        for k in range(num):  #寻找两个数组中共有的元素，且dic[i]中元素出现最少的次数为交集个数
            ans.append(i)
print (ans)

# example : dic ={3: [2, 0], 1: [2, 2], 5: [1, 1], 7: [1, 0]}