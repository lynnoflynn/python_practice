#yield是生成器,只能通过next来读取下一个值

def provider():
    for i in range (0,10):
        print("开始")
        yield i #相当于return了i，同时记录了上一次的执行位置
        print("结束")

p = provider()
#直接调用生成器不会帮助执行
# print(p)

#需要调用next方法才可以执行
#第一个是print开始, yield
print(next(p))

#第二个是print 结束，print开始，yield
# print(next(p))
# print(next(p))

# for i in p:
#     print(i)