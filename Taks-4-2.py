from robot import *

while(is_free_right() and is_free_down()):
    
    nStepsDown = 0
    nStepsUp = 0
    
    while is_free_down():
        paint()
        move_down()
        nStepsDown += 1
        
    if(is_free_right()):
        paint()
        move_right()
        paint()
        
    while(nStepsDown > nStepsUp):
        paint()
        move_up()
        nStepsUp += 1

paint()