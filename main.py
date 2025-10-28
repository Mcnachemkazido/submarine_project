from submarines.board import shooting_matrix,ship_matrix,game_status
from submarines.placement import adding_random_submarines
from submarines.game import *

if __name__ == "__main__":
    ship = ship_matrix(5)
    shooting = shooting_matrix(5)
    first_status = game_status(ship,shooting,5,10)
    status = adding_random_submarines(first_status)
    print(status)
    shot = selecting_anecdotes(status,4,4)
    print(shot)
    if shot[0]:
        board_update(status,4,4)
        print(status)
        adding_a_shot(status)
        print(status)
        print(did_hit(status,4,4))
        print(end_status(status))




