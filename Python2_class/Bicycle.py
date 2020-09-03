class Bicycle:
    def run(self,km):
        print(f"用脚一共骑行了{km}km，太辛苦啦")
# 继承Bicycle
# 继承之后，子类可以调用父类的属性和方法
class Ebicycle(Bicycle):
    # 类属性，类体内，方法之外
    #构造方法
    def __init__(self,Volume):
        #实例属性，类体内，方法之内，以"self.变量名"的方式去定义的变量
        #普通属性，类体内，方法内，局部变量，只在当前方法有用"变量名"
        self.Volume = Volume
    def fill_charge(self,vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电还有{vol+self.Volume}度")

    def run(self,km):
        #有电的时候用self.Volume，能骑到的公里数是电量X10 km
        e_km = self.Volume*10
        print(f"用电能够骑行的总公里数{e_km}km")
        # 没电的时候用run 方法骑行，加入传入的骑行里数
        # 用电就可以到:e_km > km
        if e_km - km >= 0:
            print(f"用电一共骑行了{km}km")
        # 用电到不了，e_km<km, 电的e_km +用脚蹬车=km

        else:
            print(f"用电一共骑行了{e_km}km")
        #调用父类的方法
            super().run(km-e_km)

    pass
# 继承之后子类可以调用父类的属性和方法
# 构造函数的参数，需要再实例化类的时候传递
Ebike = Ebicycle(100)
# 当子类中有和父类重名的方法或属性，那么首先选择的是子类的
Ebike.run(10000)

