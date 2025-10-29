import random
####
def adding_random_submarines(status_game):
    num = status_game["num_ship"]
    while num:
        random_1 = random.randint(0,len(status_game["ship"])-1)
        random_2 = random.randint(0, len(status_game["ship"])- 1)
        if status_game["ship"][random_1][random_2] == 0:
            status_game["ship"][random_1][random_2] = 1
            num -= 1
    return status_game