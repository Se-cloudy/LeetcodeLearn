# 21.14
# 2103. 环和杆
# 统计集齐了三种颜色的杆的数目

rings = "B0B6G0R6R0R6G9"
# 输出：1

# 以不变应万变
res = 0
mem = ['' for i in range(10)]
for i in range(0,len(rings),2):
    loc = int(rings[i+1])
    if not rings[i] in mem[loc]:
        mem[loc] += rings[i]
        if len(mem[loc])==3:
            res += 1
print(res)
