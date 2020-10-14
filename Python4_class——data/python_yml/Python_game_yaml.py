import yaml
# yaml_data = yaml.safe_load(open("data2.yml"))
# print(yaml_data)
class Game:
    def __init__(self):
        data = yaml.safe_load(open("game.yml"))
        #通过字典的列表获取字典的索引
        self.my_hp = data["me"]["hp"]
        self.my_power = data["me"]["power"]
        self.your_hp = data["you"]["hp"]
        self.your_power = data["you"]["power"]
    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.your_power
            self.your_hp = self.your_hp - self.my_power
            if self.my_hp <= 0:
                print("我的剩余血量为", self.my_hp)
                print("你的剩余血量为", self.your_hp)
                print("I lost")
                break
            elif self.your_hp <= 0:
                print("我的剩余血量为", self.my_hp)
                print("你的剩余血量为", self.your_hp)
                print("U lost")
                break
game = Game()
game.fight()
