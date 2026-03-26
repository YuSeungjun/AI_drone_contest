"""
=============================================================================
함수 파라미터 테스트 코드
=============================================================================
하나씩 주석 해제하면서 실행해보세요.
오류 안 나는 버전을 찾으면 알려주세요!
=============================================================================
"""

from whalesbot import *

# ── 테스트 1: 이륙 + 호버링 + 착륙 (이건 됨) ──
fly_unlock()
wait(1)
fly_setspeed(30)
wait(1)
fly_start(80)
wait(3)
fly_hover()
wait(2)

# ── 테스트 2: fly_moveto 파라미터 테스트 ──
# 아래 중 하나만 주석 해제해서 실행. 오류 안 나는 걸 찾기

# 2개: fly_moveto(x, y)
# fly_moveto(50, 0)

# 3개: fly_moveto(x, y, z)
# fly_moveto(50, 0, 0)

# 4개: fly_moveto(x, y, z, 속도)
# fly_moveto(50, 0, 0, 30)

# 5개: fly_moveto(x, y, z, 속도, 회전)
# fly_moveto(50, 0, 0, 30, 0)

# 6개: fly_moveto(x, y, z, 속도, 회전, 회전속도)
# fly_moveto(50, 0, 0, 30, 0, 0)

# wait(3)

# ── 테스트 3: fly_move_dis 파라미터 테스트 ──
# 아래 중 하나만 주석 해제

# 1개: fly_move_dis(거리)
# fly_move_dis(50)

# 2개: fly_move_dis(방향, 거리)
# fly_move_dis(0, 50)

# 3개: fly_move_dis(방향, 거리, 속도)
# fly_move_dis(0, 50, 30)

# 4개: fly_move_dis(x, y, z, 속도)
# fly_move_dis(50, 0, 0, 30)

# wait(3)

# ── 테스트 4: AI_GoToTag 파라미터 테스트 ──
# 아래 중 하나만 주석 해제

# 1개: AI_GoToTag(태그번호)
# AI_GoToTag(1)

# 2개: AI_GoToTag(태그번호, 속도)
# AI_GoToTag(1, 30)

# 3개: AI_GoToTag(태그번호, 고도, 속도)
# AI_GoToTag(1, 80, 30)

# wait(5)

# ── 테스트 5: AI_TagMapInit 파라미터 테스트 ──
# 1개
# AI_TagMapInit(1)

# 2개
# AI_TagMapInit(300, 300)

# ── 착륙 ──
fly_land()
wait(3)
fly_lock()
