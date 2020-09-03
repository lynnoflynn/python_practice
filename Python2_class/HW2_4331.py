# 定义天山童姥类
class Tonglao:
    # 定义属性血量，通过传入参数得到
    def __int__(self, My_HP):
        self.My_HP = My_HP
    # 定义属性武力值，通过传入参数得到
    def __int__(self,My_Power):
        self.My_Power = My_Power
    #定义see_people 方法
    def see_people(self,name):
        #如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
         if name == "WYZ":
             print("师弟！！！！")
         elif name == "李秋水":
             print("呸，贱人")
         elif name == "丁春秋":
             print("呸，贱人")
         else:
            print("来者何人？")
    #定义fight_zms方法（天山折梅手），
    def fight_zms(self,Enemy_HP,Enemy_Power):
        #调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        self.My_HP = self.My_HP*10
        self.My_Power = self.My_Power*0.5
        #需要传入敌人的hp，power
        Enemy_HP = Enemy_HP
        Enemy_Power  = Enemy_Power
        #进行一回合制对打
        My_final_HP = self.My_HP - Enemy_Power
        Enemy_final_HP = Enemy_HP - self.My_Power
        #打完之后，比较双方血量。血多的一方获胜。
        if My_final_HP > Enemy_final_HP:
            print("天山童姥获胜啦 ^_^")
        elif My_final_HP == Enemy_final_HP:
            print("平局")
        else:
            print("敌人获胜 :（")
# 定义一个XuZhu类，继承于天山童姥。
class Xuzhu(Tonglao):
    def read(self):
        print("虚竹：我不想打架嘛，罪过罪过")
#虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
#调用class天山童姥 和虚竹 示例
TL = Tonglao()
TL.see_people(name = "WYZ")
TL.My_HP = 101
TL.My_Power = 10
TL.fight_zms(Enemy_HP=100,Enemy_Power=10)
Xuzhu().read()
