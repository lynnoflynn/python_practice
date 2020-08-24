# Define a fight funcion
# 单回合游戏，谁剩余血量多，谁就赢了

def fight():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    my_final_hp = my_hp - your_power
    your_final_hp = your_hp - my_power
    if my_final_hp > your_final_hp:
        print("I won")
    elif my_final_hp < your_final_hp:
        print("U won")
    else: print("Tie")

# 调用function
fight()