import library as l
while not at_goal():
    if wall_in_front():
        l.jump()
    else:
        move()
    if at_goal():
        break
    else:
        continue
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
        if not wall_on_right():
            turn_right()
            move()
            turn_right()
            break
    while front_is_clear():
        move()
        if not front_is_clear():
            turn_left()
            break
                    