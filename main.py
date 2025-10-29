from submarines.board import *
from submarines.placement import *
from submarines.game import *
from submarines.io import *

if __name__ == "__main__":
    size = input_for_matrix_size()
    number_of_ship = input_maximum_number_of_ship()
    number_of_shots = input_maximum_number_of_shots()
    matrix_0 = ship_matrix(size)
    matrix_false = shooting_matrix(size)

    old_status = game_status(matrix_0,matrix_false,number_of_ship, number_of_shots)
    mow_status = adding_random_submarines(old_status)
    while not (shooting_mode(mow_status) or submarine_mode(mow_status)):
        mow_status["display_screen"] = screen_matrix(matrix_0,matrix_false)
        prints_status_at_start(mow_status)
        x,y = choose_a_shooting_location()
        shot_status = selecting_anecdotes(mow_status,x,y)
        if shot_status[0]:
            board_update(mow_status,x,y)
            adding_a_shot(mow_status)
            was_there_an_injury = did_hit(mow_status,x,y)
            printing_after_an_impact(was_there_an_injury)
        else:
            print(shot_status[1])
        prints_status_at_end(mow_status)

    print(f"Final summary: {end_status(mow_status)}")






