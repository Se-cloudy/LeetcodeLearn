# 15.50 摸鱼做做。还是操作函数不熟悉。
# 2512. 奖励最顶尖的 K 名学生

# 16.30 切片 列表推导式解决。例程报错。。麻了。
# 哦 只是忘了加限定k，，然后喜得超时。
# 要用哈希。set什么的。只能留一个res记录，用sort而不是sorted赋值。还得把计分函数写进去。。
# 哦 set没改进去。。那其实主要就是把输入的list改成Set，底层是哈希表。
#17.00 AC

positive_feedback = ["smart", "brilliant", "studious"]
negative_feedback = ["not"]
report = ["this student is not studious", "the student is smart"]
student_id = [1, 2]
k = 2

res = []  # List[int]
score = []

def count(words: str) -> int:
    ls = words.split(' ')
    cc = 0
    for i in ls:
        if i in positive_feedback:
            cc += 3
        elif i in negative_feedback:
            cc -= 1
    return cc


for i, word in zip(student_id, report):
    cnt = count(word)
    score.append((cnt, i))

res = sorted(score, key= lambda x: (-x[0], x[1]))
# 列表推导式
ls = [x[1] for x in res[:k]]
print(ls)
