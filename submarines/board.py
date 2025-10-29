######
def ship_matrix(size:int,file:int=0)->list[list[int]]:
    my_matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(file)
        my_matrix.append(line)
    return my_matrix

#####
def shooting_matrix(size:int,file:bool=False)->list[list[bool]]:
    my_matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(file)
        my_matrix.append(line)
    return my_matrix

#####
def screen_matrix(matrix_ship:list[list[int]],matrix_shooting:list[list[bool]])->list[list[str]]:
    new_matrix = []
    for i in range(len(matrix_ship)):
        new_line = []
        for j in range(len(matrix_ship)):
            if matrix_shooting[i][j] == False:
                new_letter = "o"
            elif matrix_shooting[i][j] == True and  matrix_ship[i][j] == 0:
                new_letter = "x"
            elif matrix_ship[i][j] == True and matrix_ship[i][j] == 1:
                new_letter = "v"
            new_line.append(new_letter)
        new_matrix.append(new_line)
    return new_matrix

#####
def game_status(ship,shooting,num_ship,num_shooting):
    return {
            "ship":ship,
            "shooting":shooting,
            "display_screen":screen_matrix(ship,shooting),
            "num_shooting":num_shooting,
            "last_shooting":0,
            "num_ship":num_ship,
            "last_ship":0
        }