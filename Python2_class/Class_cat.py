# 定义类，首字母需要大写
class Cat:
    # 属性
    color = "orange"
    leg = 4
    # 方法,在类的方法中，是使用def 关键字定义
    # def 定义的 在类外叫做函数function, 在类内，叫做method
    def eat(self):
        print("猫在吃")
    def cry(self):
        print("猫在叫")

#类的属性可以直接用
print(Cat.color)
# 类的方法不能直接用，print(Cat.eat()) 即类的实例化
# 类在实例化时需要加括号
#Cat().eat()
cat = Cat()
cat.eat()

