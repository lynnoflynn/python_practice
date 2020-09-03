# Define a fight funcion
# 多回合游戏， 谁剩余血量先为0，谁就输了
# ctrl D可以复制当前行

def fight():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 198
    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <=0:
            print("我的剩余血量为", my_hp)
            print("你的剩余血量为", your_hp)
            print("I lost")
            break
        elif your_hp <=0:
            print("我的剩余血量为", my_hp)
            print("你的剩余血量为", your_hp)
            print("U lost")
            break


# 调用function
fight()