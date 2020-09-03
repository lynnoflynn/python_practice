# 定义类，首字母需要大写
class Google_Pixel3:
    # 属性
    classification = "Cellphone"
    model = "Pixel 3"
    color = "black"
    Android_Version = 10
    # 方法,在类的方法中，是使用def 关键字定义
    # def 定义的 在类外叫做函数function, 在类内，叫做method
    def call(self):
        print("打电话")
    def music(self):
        print("听音乐")

#类的属性可以直接用
print(Google_Pixel3.call)

GP = Google_Pixel3()
GP.call()
GP.music()

