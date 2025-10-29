#####
def prints_status_at_start(status_game):
    print(status_game["display_screen"])
####
def prints_status_at_end(status_game):
    print(f"shots left: {(status_game["num_shooting"]) - (status_game["last_shooting"])},"
          f" remaining ships: {(status_game["num_ship"]) - (status_game["last_ship"])}")

#####
def printing_after_an_impact(status):
    if status:
        print("prefect hit")
    else:
        print("maybe next time")

####
def input_for_matrix_size():
    matrix_size = int(input("Select input for matrix size"))
    return matrix_size

####
def input_maximum_number_of_shots():
    matrix_shots = int(input("input_maximum_number_of_shots"))
    return matrix_shots

#####
def input_maximum_number_of_ship():
    matrix_shots = int(input("input_maximum_number_of_ship"))
    return matrix_shots
####
def choose_a_shooting_location():
    x = int(input("Select x"))
    y = int(input("Select y"))
    return x,y







