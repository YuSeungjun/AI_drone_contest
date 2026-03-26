"""
=============================================================================
제3회 국제 창의 AI 드론 경진대회 - 자율비행 미션 코드
=============================================================================
드론: WhalesBot Eagle
환경: WhalesBot Python 전용 (from whalesbot import * 만 허용)
=============================================================================
★ 대회 당일 수정: 아래 좌표/높이/속도값을 실측 후 변경
★ fly_moveto(고도, 속도, x오프셋, y오프셋) = 상대이동
★ fly_start(고도) = 자동이륙
=============================================================================
"""

from whalesbot import *

# ── 설정값 (대회 당일 수정) ──
SPD = 30
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

STRATEGY = "default"

# ── 초기화 ──
resettime()
fly_unlock()
wait(1)
fly_setspeed(SPD)
wait(1)

# ── 과제1: 이륙 (40점) ──
fly_start(80)
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
    # 베이스 -> 이중가로봉 위치로 이동
    dx = DB_X - cur_x
    dy = DB_Y - cur_y
    fly_moveto(DB_H, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = DB_X
    cur_y = DB_Y
    cur_h = DB_H
    # 사이 통과: 전진 50cm
    fly_moveto(cur_h, SPD, 0, 50)
    wait(3)
    fly_hover()
    wait(0.5)
    cur_y = cur_y + 50
    score = score + 40
    # 상승
    cur_h = cur_h + 30
    fly_moveto(cur_h, SPD, 0, 0)
    wait(3)
    fly_hover()
    wait(0.5)
    # 원호 360도 시계방향 (25cm 반경, 12스텝)
    i = 0
    while i < 12:
        fly_moveto(cur_h, SPD, 0, 13)
        wait(2)
        fly_turn(30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 60
    # 8자 비행: 반시계 360
    i = 0
    while i < 12:
        fly_moveto(cur_h, SPD, 0, 13)
        wait(2)
        fly_turn(-30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    # 8자 비행: 시계 360
    i = 0
    while i < 12:
        fly_moveto(cur_h, SPD, 0, 13)
        wait(2)
        fly_turn(30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 80
    DebugValue("score", score)

    # --- 과제2: 링1 통과 (50점) ---
    dx = R1_X - cur_x
    dy = R1_Y - cur_y
    fly_moveto(R1_H, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = R1_X
    cur_y = R1_Y
    cur_h = R1_H
    # 링 통과: 전진 80cm
    fly_moveto(cur_h, SPD, 0, 80)
    wait(3)
    fly_hover()
    wait(0.5)
    cur_y = cur_y + 80
    score = score + 50
    DebugValue("score", score)

    # --- 과제2: 링2 통과 (50점) ---
    dx = R2_X - cur_x
    dy = R2_Y - cur_y
    fly_moveto(R2_H, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = R2_X
    cur_y = R2_Y
    cur_h = R2_H
    # 링 통과: 전진 80cm
    fly_moveto(cur_h, SPD, 0, 80)
    wait(3)
    fly_hover()
    wait(0.5)
    cur_y = cur_y + 80
    score = score + 50
    DebugValue("score", score)

    # --- 과제3: 장애물 통과 (100점) ---
    target_h = SB_H - 20
    dx = SB_X - cur_x
    dy = SB_Y - cur_y
    fly_moveto(target_h, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = SB_X
    cur_y = SB_Y
    cur_h = target_h
    # 아래 통과: 전진 60cm
    fly_moveto(cur_h, SPD, 0, 60)
    wait(3)
    fly_hover()
    wait(0.5)
    cur_y = cur_y + 60
    score = score + 40
    # 상승 후 회전
    cur_h = cur_h + 40
    fly_moveto(cur_h, SPD, 0, 0)
    wait(3)
    fly_hover()
    wait(0.5)
    i = 0
    while i < 12:
        fly_moveto(cur_h, SPD, 0, 16)
        wait(2)
        fly_turn(30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 60
    DebugValue("score", score)

    # --- 과제6: S자 비행 (80점) ---
    dx = PP_X - cur_x
    dy = PP_Y - cur_y
    fly_moveto(PP_H, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = PP_X
    cur_y = PP_Y
    cur_h = PP_H
    # 반시계 반원
    i = 0
    while i < 6:
        fly_moveto(cur_h, SPD, 0, 18)
        wait(2)
        fly_turn(-30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    # 시계 반원
    i = 0
    while i < 6:
        fly_moveto(cur_h, SPD, 0, 18)
        wait(2)
        fly_turn(30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 80
    DebugValue("score", score)

    # --- 과제7: 수평 링 상승 통과 (70점) ---
    dx = HR_X - cur_x
    dy = HR_Y - cur_y
    fly_moveto(HR_H, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = HR_X
    cur_y = HR_Y
    cur_h = HR_H
    # 수직 상승 60cm
    cur_h = cur_h + 60
    fly_moveto(cur_h, SPD, 0, 0)
    wait(3)
    fly_hover()
    wait(0.5)
    score = score + 70
    DebugValue("score", score)

    # --- 과제5: 기둥 선회 (60점) ---
    dx = PL_X - cur_x
    dy = PL_Y - cur_y
    fly_moveto(PL_H, SPD, dx, dy)
    wait(5)
    fly_hover()
    wait(1)
    cur_x = PL_X
    cur_y = PL_Y
    cur_h = PL_H
    i = 0
    while i < 12:
        fly_moveto(cur_h, SPD, 0, 21)
        wait(2)
        fly_turn(30)
        wait(1)
        fly_hover()
        wait(0.3)
        i = i + 1
    fly_hover()
    wait(0.5)
    score = score + 60
    DebugValue("score", score)

# ── 과제8: 베이스 복귀 (40점) ──
dx = BASE_X - cur_x
dy = BASE_Y - cur_y
fly_moveto(80, SPD, dx, dy)
wait(5)
fly_hover()
wait(1)
fly_land()
wait(3)
fly_lock()
score = score + 40

DebugValue("final_score", score)
DebugValue("time_sec", seconds())
