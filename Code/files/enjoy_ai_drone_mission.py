"""
=============================================================================
제3회 국제 창의 AI 드론 경진대회 (Enjoy AI Korea) - 자율비행 미션 코드
=============================================================================

드론: WhalesBot Eagle (가이온에듀테크 이글드론)
필드: 300x300cm, 비전 태그 기반 위치 인식
제한시간: 라운드당 180초
환경: WhalesBot Python 전용 (import whalesbot만 허용)

과제별 배점:
  1. 이륙                               : 40점
  2. 링 통과 x2                         : 50 x 2 = 100점
  3. 장애물 통과 (아래+회전)             : 40 + 60 = 100점
  4. 이중 가로봉 (사이+회전+8자)         : 40 + 60 + 80 = 180점
  5. 기둥 선회                           : 60점
  6. 두 기둥 S자 비행                    : 80점
  7. 수평 링 상승 통과                   : 70점
  8. 베이스 복귀                         : 40점
  이론 만점: 720점

=============================================================================
★ 대회 당일 수정 포인트 ★

1. FLIGHT_SPEED          → 드론 테스트 후 속도 조정
2. OBSTACLES 좌표        → 워밍업 시간에 실제 필드 측정
3. OBSTACLE_HEIGHTS      → 실제 장애물 높이 측정
4. fly_move_dis 파라미터 → 방향값 확인 (0~5 중 어떤 값이 어떤 방향인지)
5. STRATEGY              → 맨 아래에서 전략 선택
=============================================================================
"""

import whalesbot

# ─────────────────────────────────────────────
# [설정값] 대회 당일 조정
# ─────────────────────────────────────────────

FLIGHT_SPEED = 30   # fly_setspeed 파라미터

BASE_POS_X = 15     # 베이스 중심 X (cm)
BASE_POS_Y = 15     # 베이스 중심 Y (cm)

# 장애물 좌표 (cm) - 대회 당일 수정 필수!
OBS_RING1_X = 100
OBS_RING1_Y = 100
OBS_RING2_X = 200
OBS_RING2_Y = 100
OBS_SBAR_X = 100
OBS_SBAR_Y = 200
OBS_DBAR_X = 200
OBS_DBAR_Y = 200
OBS_PILLAR_X = 150
OBS_PILLAR_Y = 150
OBS_PPAIR_X = 250
OBS_PPAIR_Y = 150
OBS_HRING_X = 150
OBS_HRING_Y = 250

# 장애물별 높이 (cm) - 대회 당일 수정 필수!
H_RING1 = 70
H_RING2 = 100
H_SBAR = 60
H_DBAR = 60
H_PILLAR = 80
H_PPAIR = 80
H_HRING = 50

# ─────────────────────────────────────────────
# [상태 변수]
# ─────────────────────────────────────────────

cur_x = BASE_POS_X
cur_y = BASE_POS_Y
cur_h = 0
score = 0

# ─────────────────────────────────────────────
# [기본 비행 함수]
# ─────────────────────────────────────────────

def init_drone():
    whalesbot.fly_unlock()
    whalesbot.wait(1)
    whalesbot.fly_setspeed(FLIGHT_SPEED)
    whalesbot.wait(1)
    whalesbot.AI_TagMapInit()
    whalesbot.wait(1)


def takeoff(height_cm):
    global cur_h
    whalesbot.fly_start()
    whalesbot.wait(3)
    if height_cm > 0:
        whalesbot.fly_moveto(0, 0, height_cm)
        whalesbot.wait(3)
    whalesbot.fly_hover()
    whalesbot.wait(1)
    cur_h = height_cm


def land():
    global cur_h
    whalesbot.fly_land()
    whalesbot.wait(3)
    whalesbot.fly_lock()
    cur_h = 0


def forward(cm):
    whalesbot.fly_move_dis(0, cm)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)


def backward(cm):
    whalesbot.fly_move_dis(1, cm)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)


def go_left(cm):
    whalesbot.fly_move_dis(2, cm)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)


def go_right(cm):
    whalesbot.fly_move_dis(3, cm)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)


def go_up(cm):
    global cur_h
    whalesbot.fly_move_dis(4, cm)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)
    cur_h = cur_h + cm


def go_down(cm):
    global cur_h
    whalesbot.fly_move_dis(5, cm)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)
    cur_h = cur_h - cm


def turn_cw(deg):
    whalesbot.fly_turn(deg)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)


def turn_ccw(deg):
    whalesbot.fly_turn(-deg)
    whalesbot.wait(2)
    whalesbot.fly_hover()
    whalesbot.wait(0.5)


def hover(sec):
    whalesbot.fly_hover()
    whalesbot.wait(sec)


def set_height(target_cm):
    global cur_h
    diff = target_cm - cur_h
    if diff > 0:
        go_up(diff)
    elif diff < 0:
        go_down(-diff)
    cur_h = target_cm


# ─────────────────────────────────────────────
# [네비게이션] 좌표 기반 이동
# ─────────────────────────────────────────────

def navigate(tx, ty, th):
    """현재 위치에서 (tx, ty) 좌표, th 높이로 이동"""
    global cur_x, cur_y

    set_height(th)

    dx = tx - cur_x
    dy = ty - cur_y

    # X축 (좌우)
    if dx > 0:
        go_right(dx)
    elif dx < 0:
        go_left(-dx)

    # Y축 (전후)
    if dy > 0:
        forward(dy)
    elif dy < 0:
        backward(-dy)

    hover(0.5)
    cur_x = tx
    cur_y = ty


# ─────────────────────────────────────────────
# [원호 비행] 직선+회전 조합
# ─────────────────────────────────────────────

def fly_arc(radius_cm, angle_deg, cw):
    """
    원호 비행
    cw = 1 이면 시계방향, cw = 0 이면 반시계방향
    """
    steps = angle_deg // 30
    if steps < 4:
        steps = 4
    step_angle = angle_deg / steps
    half_rad = (step_angle / 2.0) * 3.14159265 / 180.0
    step_dist = 2.0 * radius_cm * whalesbot.math_sin(half_rad)
    rounded_dist = whalesbot.math_round(step_dist)
    rounded_angle = whalesbot.math_round(step_angle)

    i = 0
    while i < steps:
        forward(rounded_dist)
        if cw == 1:
            turn_cw(rounded_angle)
        else:
            turn_ccw(rounded_angle)
        i = i + 1


# ─────────────────────────────────────────────
# [과제 수행 함수]
# ─────────────────────────────────────────────

def task_takeoff():
    """과제 1: 이륙 (40점)"""
    global score
    init_drone()
    takeoff(80)
    hover(1)
    score = score + 40
    whalesbot.DebugValue("score", score)


def task_ring(rx, ry, rh):
    """과제 2: 수직 링 통과 (50점)"""
    global score
    navigate(rx, ry, rh)
    hover(0.5)
    forward(80)
    hover(0.5)
    score = score + 50
    whalesbot.DebugValue("score", score)


def task_obstacle():
    """과제 3: 장애물 통과 (40+60 = 100점)"""
    global score

    # 가로봉 아래로 통과
    navigate(OBS_SBAR_X, OBS_SBAR_Y, H_SBAR - 20)
    forward(60)
    hover(0.3)
    score = score + 40

    # 상승 후 가로봉 주위 360도 회전
    go_up(40)
    fly_arc(30, 360, 1)
    hover(0.3)
    score = score + 60
    whalesbot.DebugValue("score", score)


def task_double_bar():
    """과제 4: 이중 가로봉 (40+60+80 = 180점)"""
    global score

    navigate(OBS_DBAR_X, OBS_DBAR_Y, H_DBAR)

    # 두 가로봉 사이 통과
    forward(50)
    hover(0.3)
    score = score + 40

    # 가로봉 하나 주위 회전
    go_up(30)
    fly_arc(25, 360, 1)
    hover(0.3)
    score = score + 60

    # 8자 비행
    fly_arc(25, 360, 0)  # 반시계
    fly_arc(25, 360, 1)  # 시계
    hover(0.5)
    score = score + 80
    whalesbot.DebugValue("score", score)


def task_pillar():
    """과제 5: 기둥 선회 (60점)"""
    global score
    navigate(OBS_PILLAR_X, OBS_PILLAR_Y, H_PILLAR)
    fly_arc(40, 360, 1)
    hover(0.5)
    score = score + 60
    whalesbot.DebugValue("score", score)


def task_s_flight():
    """과제 6: 두 기둥 S자 비행 (80점)"""
    global score
    navigate(OBS_PPAIR_X, OBS_PPAIR_Y, H_PPAIR)
    fly_arc(35, 180, 0)  # 첫 번째 기둥 반시계 반원
    fly_arc(35, 180, 1)  # 두 번째 기둥 시계 반원
    hover(0.5)
    score = score + 80
    whalesbot.DebugValue("score", score)


def task_horizontal_ring():
    """과제 7: 수평 링 상승 통과 (70점)"""
    global score
    navigate(OBS_HRING_X, OBS_HRING_Y, H_HRING)
    hover(0.5)
    go_up(60)
    hover(0.5)
    score = score + 70
    whalesbot.DebugValue("score", score)


def task_return():
    """과제 8: 베이스 복귀 착륙 (40점)"""
    global score, cur_x, cur_y
    set_height(80)
    dx = BASE_POS_X - cur_x
    dy = BASE_POS_Y - cur_y

    if dx > 0:
        go_right(dx)
    elif dx < 0:
        go_left(-dx)

    if dy > 0:
        forward(dy)
    elif dy < 0:
        backward(-dy)

    hover(1)
    land()
    cur_x = BASE_POS_X
    cur_y = BASE_POS_Y
    score = score + 40
    whalesbot.DebugValue("score", score)


# ─────────────────────────────────────────────
# [메인 실행]
# ─────────────────────────────────────────────
# 전략: "default" = 고배점 우선, "safe" = 쉬운것부터, "speed" = 가까운것부터

STRATEGY = "default"

whalesbot.resettime()

# 과제 1: 이륙 (필수)
task_takeoff()

if STRATEGY == "default":
    task_double_bar()
    task_ring(OBS_RING1_X, OBS_RING1_Y, H_RING1)
    task_ring(OBS_RING2_X, OBS_RING2_Y, H_RING2)
    task_obstacle()
    task_s_flight()
    task_horizontal_ring()
    task_pillar()

elif STRATEGY == "safe":
    task_ring(OBS_RING1_X, OBS_RING1_Y, H_RING1)
    task_ring(OBS_RING2_X, OBS_RING2_Y, H_RING2)
    task_pillar()
    task_obstacle()
    task_s_flight()
    task_horizontal_ring()
    task_double_bar()

elif STRATEGY == "speed":
    task_ring(OBS_RING1_X, OBS_RING1_Y, H_RING1)
    task_obstacle()
    task_pillar()
    task_ring(OBS_RING2_X, OBS_RING2_Y, H_RING2)
    task_double_bar()
    task_s_flight()
    task_horizontal_ring()

# 과제 8: 베이스 복귀 (필수)
task_return()

# 결과 표시
whalesbot.DebugValue("final_score", score)
whalesbot.DebugValue("time_sec", whalesbot.seconds())
