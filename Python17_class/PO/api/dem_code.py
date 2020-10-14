#python不定长关键词传参

def demo(a,b,c):
    print(a)
    print(b)
    print(c)

#直接打印 是1，2，3
# demo(1,2,3)

#位置是颠倒的，打印出来依然是1，2，3
# demo(b=2,a=1,c=3)

data = {"a":1,"b":2,"c":3}
# demo(data) 字典不解包是不行的
#字典解包后，通过关键词传参的方式，给函数传递参数
demo(**data)