from whalesbot import *

fly_unlock()
wait(1)
fly_setspeed(30)
wait(1)
fly_start(80)
wait(3)
fly_hover()
wait(2)

fly_moveto(50, 0, 0, 30)
wait(3)

fly_land()
wait(3)
fly_lock()
