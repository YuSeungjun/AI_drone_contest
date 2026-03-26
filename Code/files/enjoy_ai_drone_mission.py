from whalesbot import *

fly_unlock()
fly_start(80)
wait(3)

# 전진 x3
fly_moveto(FRONT, 55)
wait(3)
fly_moveto(FRONT, 55)
wait(3)
fly_moveto(FRONT, 55)
wait(3)

# 오른쪽
fly_moveto(RIGHT, 55)
wait(3)

# 뒤로
fly_moveto(BACK, 55)
wait(3)

# 왼쪽
fly_moveto(LEFT, 55)
wait(3)

# 전진
fly_moveto(FRONT, 55)
wait(3)

# 오른쪽
fly_moveto(RIGHT, 55)
wait(3)

# 높이 90으로 수정 (현재 80 -> 10cm 상승)
fly_moveto(UP, 10)
wait(3)

# 오른쪽 27cm
fly_moveto(RIGHT, 27)
wait(3)

# 높이 60으로 (현재 90 -> 30cm 하강)
fly_moveto(DOWN, 30)
wait(3)

fly_land()
wait(3)
fly_lock()
