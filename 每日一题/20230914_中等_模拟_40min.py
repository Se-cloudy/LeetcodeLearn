#2023.9.14.17:17
#1222. 可以攻击国王的皇后

#检测八个方向的最近皇后即可。
#17.29构建好方向定义;17,35暂停修改方向
#20:20继续 细化判断即可。。
#20:38 AC 但是太蠢了。

queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
res = [[] for i in range(8)]  # 约定正东为0，顺时针
for i in queens:
    if i[0] == king[0]:
        if i[1] > king[1]: #正东
            if not res[0]:
                res[0] = i
            elif i[1] < res[0][1]:
                res[0] = i
        else: # 西
            if not res[4]:
                res[4] = i
            elif i[1] > res[4][1]:
                res[4] = i
    elif i[1] == king[1]:
        if i[0] < king[0]:  # 北
            if not res[6]:
                res[6] = i
            elif i[0] > res[6][0]:
                res[6] = i
        else:  # 南
            if not res[2]:
                res[2] = i
            elif i[0] < res[2][0]:
                res[2] = i
    elif (i[0]-king[0])==(i[1]-king[1]):
        if i[0] > king[0]:
            if not res[1]:
                res[1] = i
            elif i[1] < res[1][1]:
                res[1] = i
        else:
            if not res[5]:
                res[5] = i
            elif i[1] > res[5][1]:
                res[5] = i
    elif (i[0]-king[0])== (-i[1]+king[1]):
        if i[0] > king[0]:
            if not res[3]:
                res[3] = i
            elif i[0] < res[3][0]:
                res[3] = i
        else:
            if not res[7]:
                res[7] = i
            elif i[0] > res[7][0]:
                res[7]= i
cur = []
for i in res:
    if i:
        cur.append(i)
print(cur)