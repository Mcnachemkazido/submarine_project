#####
def selecting_anecdotes(status_game,x,y):
    if x < len(status_game["ship"]) and  y < len(status_game["ship"]):
        if status_game["shooting"][x][y] == False:
            message = (True,"new place")
        else:
            message = (False,"no new place")
    else:
        message = (False,"out of range")
    return message

####
def board_update(status_game,x,y):
    status_game["shooting"][x][y] = True


####
def adding_a_shot(status_game):
    status_game["last_shooting"] += 1


####
def did_hit(status_game,x,y):
    if status_game["ship"][x][y] == 1:
        status_game["last_ship"] += 1
    return status_game["ship"][x][y] == 1

#####
def shooting_mode(status_game):
    return status_game["last_shooting"] >= status_game["num_shooting"]

#####
def submarine_mode(status_game):
    return status_game["last_ship"] >= status_game["num_ship"]

def end_status(status_game):
    display_screen = status_game["display_screen"]
    if not submarine_mode(status_game):
        ship = status_game["ship"]
        for i in range(len(display_screen)):
            for j in range(len(display_screen)):
                if display_screen[i][j] == "o":
                    if ship[i][j] == 1:
                        display_screen[i][j] = 1
        return display_screen
    else:
        return True




