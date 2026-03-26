"""
=============================================================================
제3회 국제 창의 AI 드론 경진대회 - 자율비행 미션 코드
=============================================================================
드론: WhalesBot Eagle
환경: WhalesBot Python 전용 (from whalesbot import * 만 허용)
=============================================================================
★ 대회 당일 수정: 아래 좌표/높이/속도값을 실측 후 변경
★ fly_move_dis(방향, 거리) 방향값 확인 필수
=============================================================================
"""

from whalesbot import *

# ── 설정값 (대회 당일 수정) ──
FLIGHT_SPEED = 30
BASE_X = 15
BASE_Y = 15

# 장애물 좌표 (cm)
R1_X = 100
R1_Y = 100
R2_X = 200
R2_Y = 100
SB_X = 100
SB_Y = 200
DB_X = 200
DB_Y = 200
PL_X = 150
PL_Y = 150
PP_X = 250
PP_Y = 150
HR_X = 150
HR_Y = 250

# 장애물 높이 (cm)
R1_H = 70
R2_H = 100
SB_H = 60
DB_H = 60
PL_H = 80
PP_H = 80
HR_H = 50

# 전략: "default", "safe", "speed"
STRATEGY = "default"

# ── 초기화 ──
resettime()
fly_unlock()
wait(1)
fly_setspeed(FLIGHT_SPEED)
wait(1)
# AI_TagMapInit은 파라미터 필요 - 대회장에서 태그맵 크기 확인 후 추가
# 예: AI_TagMapInit(300, 300) 등

# ── 과제1: 이륙 (40점) ──
fly_start()
wait(3)
fly_moveto(0, 0, 80)
wait(3)
fly_hover()
wait(1)
cur_x = BASE_X
cur_y = BASE_Y
cur_h = 80
score = 40
DebugValue("score", score)

# ── 전략별 과제 순서 ──

if STRATEGY == "default":
    # --- 과제4: 이중 가로봉 (180점) ---
    # 높이 조정
    diff = DB_H - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = DB_H
    # X이동
    dx = DB_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    # Y이동
    dy = DB_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = DB_X
    cur_y = DB_Y
    fly_hover()
    wait(0.5)
    # 사이 통과
    fly_move_dis(0, 50)
    wait(2)
    fly_hover()
    wait(0.3)
    score = score + 40
    # 상승 후 회전
    fly_move_dis(4, 30)
    wait(2)
    fly_hover()
    wait(0.5)
    cur_h = cur_h + 30
    # 원호 360도 시계방향 (25cm 반경)
    i = 0
    while i < 12:
        fly_move_dis(0, 13)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.3)
    score = score + 60
    # 8자 비행: 반시계 360
    i = 0
    while i < 12:
        fly_move_dis(0, 13)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(-30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    # 8자 비행: 시계 360
    i = 0
    while i < 12:
        fly_move_dis(0, 13)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 80
    DebugValue("score", score)

    # --- 과제2: 링1 통과 (50점) ---
    diff = R1_H - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = R1_H
    dx = R1_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    dy = R1_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = R1_X
    cur_y = R1_Y
    fly_hover()
    wait(0.5)
    fly_move_dis(0, 80)
    wait(2)
    fly_hover()
    wait(0.5)
    score = score + 50
    DebugValue("score", score)

    # --- 과제2: 링2 통과 (50점) ---
    diff = R2_H - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = R2_H
    dx = R2_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    dy = R2_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = R2_X
    cur_y = R2_Y
    fly_hover()
    wait(0.5)
    fly_move_dis(0, 80)
    wait(2)
    fly_hover()
    wait(0.5)
    score = score + 50
    DebugValue("score", score)

    # --- 과제3: 장애물 통과 (100점) ---
    target_h = SB_H - 20
    diff = target_h - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = target_h
    dx = SB_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    dy = SB_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = SB_X
    cur_y = SB_Y
    # 아래 통과
    fly_move_dis(0, 60)
    wait(2)
    fly_hover()
    wait(0.3)
    score = score + 40
    # 상승 후 회전
    fly_move_dis(4, 40)
    wait(2)
    fly_hover()
    wait(0.5)
    cur_h = cur_h + 40
    i = 0
    while i < 12:
        fly_move_dis(0, 16)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.3)
    score = score + 60
    DebugValue("score", score)

    # --- 과제6: S자 비행 (80점) ---
    diff = PP_H - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = PP_H
    dx = PP_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    dy = PP_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = PP_X
    cur_y = PP_Y
    # 반시계 반원
    i = 0
    while i < 6:
        fly_move_dis(0, 18)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(-30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    # 시계 반원
    i = 0
    while i < 6:
        fly_move_dis(0, 18)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 80
    DebugValue("score", score)

    # --- 과제7: 수평 링 상승 통과 (70점) ---
    diff = HR_H - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = HR_H
    dx = HR_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    dy = HR_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = HR_X
    cur_y = HR_Y
    fly_hover()
    wait(0.5)
    fly_move_dis(4, 60)
    wait(2)
    fly_hover()
    wait(0.5)
    cur_h = cur_h + 60
    score = score + 70
    DebugValue("score", score)

    # --- 과제5: 기둥 선회 (60점) ---
    diff = PL_H - cur_h
    if diff > 0:
        fly_move_dis(4, diff)
        wait(2)
        fly_hover()
        wait(0.5)
    elif diff < 0:
        fly_move_dis(5, -diff)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_h = PL_H
    dx = PL_X - cur_x
    if dx > 0:
        fly_move_dis(3, dx)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dx < 0:
        fly_move_dis(2, -dx)
        wait(2)
        fly_hover()
        wait(0.5)
    dy = PL_Y - cur_y
    if dy > 0:
        fly_move_dis(0, dy)
        wait(2)
        fly_hover()
        wait(0.5)
    elif dy < 0:
        fly_move_dis(1, -dy)
        wait(2)
        fly_hover()
        wait(0.5)
    cur_x = PL_X
    cur_y = PL_Y
    i = 0
    while i < 12:
        fly_move_dis(0, 21)
        wait(2)
        fly_hover()
        wait(0.3)
        fly_turn(30)
        wait(2)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 60
    DebugValue("score", score)

# ── 과제8: 베이스 복귀 (40점) ──
diff = 80 - cur_h
if diff > 0:
    fly_move_dis(4, diff)
    wait(2)
    fly_hover()
    wait(0.5)
elif diff < 0:
    fly_move_dis(5, -diff)
    wait(2)
    fly_hover()
    wait(0.5)

dx = BASE_X - cur_x
if dx > 0:
    fly_move_dis(3, dx)
    wait(2)
    fly_hover()
    wait(0.5)
elif dx < 0:
    fly_move_dis(2, -dx)
    wait(2)
    fly_hover()
    wait(0.5)

dy = BASE_Y - cur_y
if dy > 0:
    fly_move_dis(0, dy)
    wait(2)
    fly_hover()
    wait(0.5)
elif dy < 0:
    fly_move_dis(1, -dy)
    wait(2)
    fly_hover()
    wait(0.5)

fly_hover()
wait(1)
fly_land()
wait(3)
fly_lock()
score = score + 40

DebugValue("final_score", score)
DebugValue("time_sec", seconds())
