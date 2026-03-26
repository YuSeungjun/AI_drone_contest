"""
=============================================================================
제3회 국제 창의 AI 드론 경진대회 (Enjoy AI Korea) - 자율비행 미션 코드
=============================================================================

대회 필드: 300×300cm 실내, QR코드 기반 위치 인식
드론 스펙: 쿼드콥터, 80~120g, 휠베이스 125~130mm, 5V/1150mAh 배터리
제한시간: 라운드당 180초

과제별 배점:
  1. 이륙 (Takeoff)                    : 40점
  2. 링 통과 (Ring Pass) x2            : 50점 x 2 = 100점
  3. 장애물 통과 (Obstacle)             : 40 + 60 = 100점
  4. 이중 가로봉 (Double Bar)           : 40 + 60 + 80 = 180점
  5. 기둥 선회 (Pillar Orbit)           : 60점
  6. 두 기둥 S자 비행 (S-Flight)        : 80점
  7. 수평 링 상승 통과 (Horizontal Ring) : 70점
  8. 베이스 복귀 (Return to Base)       : 40점
  ─────────────────────────────────
  이론 만점                             : 720점 (+ 지식재산 가산점 100점)

사용 환경: Python 3 / MicroPython (ENJOY AI 드론 SDK 호환)
=============================================================================
uv run python files/enjoy_ai_drone_mission.py 
"""

import time
import math

# ─────────────────────────────────────────────
# [섹션 1] 드론 SDK 추상화 레이어
# ─────────────────────────────────────────────
# ENJOY AI 드론 키트는 대회마다 SDK가 약간 다를 수 있습니다.
# 아래는 가장 일반적인 API를 추상화한 것으로,
# 실제 SDK에 맞게 import와 함수명을 수정하세요.

class DroneController:
    """
    드론 제어 추상화 클래스.
    실제 대회에서 사용하는 SDK에 맞게 아래 메서드들을 수정하세요.
    
    일반적인 ENJOY AI 드론 SDK 예시:
      - from enjoyai_drone import Drone
      - from drone_sdk import EnjoyAIDrone
      - from espDrone import CopterDrone
    """
    
    def __init__(self):
        """드론 초기화 및 연결"""
        # ====================================================
        # TODO: 실제 SDK에 맞게 수정하세요
        # 예시:
        #   self.drone = Drone()
        #   self.drone.connect()
        # ====================================================
        self.drone = None  # 실제 드론 객체로 교체
        self.is_flying = False
        self.current_height = 0  # cm 단위
        
    # --- 기본 비행 제어 ---
    
    def takeoff(self, height_cm=80):
        """
        이륙: 드론 베이스에서 지정 높이까지 상승
        
        Args:
            height_cm: 목표 이륙 높이 (cm). 기본값 80cm.
                       링 통과 등을 고려하여 적절한 높이 설정
        """
        print(f"[이륙] 목표 높이: {height_cm}cm")
        # ====================================================
        # TODO: 실제 SDK 호출로 교체
        # 예시:
        #   self.drone.takeoff(height=height_cm)
        #   또는
        #   self.drone.arm()
        #   self.drone.set_throttle(height_cm)
        # ====================================================
        self.is_flying = True
        self.current_height = height_cm
        time.sleep(2)  # 이륙 안정화 대기
        print("[이륙] 완료 → +40점")
    
    def land(self):
        """착륙"""
        print("[착륙] 실행")
        # TODO: self.drone.land()
        self.is_flying = False
        self.current_height = 0
        time.sleep(1.5)
    
    def move_forward(self, distance_cm, speed=30):
        """전진 이동"""
        print(f"[이동] 전진 {distance_cm}cm (속도: {speed})")
        # TODO: self.drone.move_forward(distance_cm, speed)
        time.sleep(distance_cm / speed)  # 예상 소요시간
    
    def move_backward(self, distance_cm, speed=30):
        """후진 이동"""
    print(f"[이동] 후진 {distance_cm}cm")
        # TODO: self.drone.move_backward(distance_cm, speed)
        time.sleep(distance_cm / speed)
    
    def move_left(self, distance_cm, speed=30):
        """좌측 이동"""
        print(f"[이동] 좌측 {distance_cm}cm")
        # TODO: self.drone.move_left(distance_cm, speed)
        time.sleep(distance_cm / speed)
    
    def move_right(self, distance_cm, speed=30):
        """우측 이동"""
        print(f"[이동] 우측 {distance_cm}cm")
        # TODO: self.drone.move_right(distance_cm, speed)
        time.sleep(distance_cm / speed)
    
    def move_up(self, distance_cm, speed=20):
        """상승"""
        print(f"[이동] 상승 {distance_cm}cm")
        # TODO: self.drone.move_up(distance_cm, speed)
        self.current_height += distance_cm
        time.sleep(distance_cm / speed)
    
    def move_down(self, distance_cm, speed=20):
        """하강"""
        print(f"[이동] 하강 {distance_cm}cm")
        # TODO: self.drone.move_down(distance_cm, speed)
        self.current_height -= distance_cm
        time.sleep(distance_cm / speed)
    
    def rotate_cw(self, degrees, speed=30):
        """시계 방향 회전 (yaw)"""
        print(f"[회전] 시계방향 {degrees}°")
        # TODO: self.drone.rotate_cw(degrees)
        time.sleep(abs(degrees) / 90)
    
    def rotate_ccw(self, degrees, speed=30):
        """반시계 방향 회전 (yaw)"""
        print(f"[회전] 반시계방향 {degrees}°")
        # TODO: self.drone.rotate_ccw(degrees)
        time.sleep(abs(degrees) / 90)
    
    def hover(self, duration_sec=1.0):
        """제자리 호버링"""
        print(f"[호버링] {duration_sec}초")
        time.sleep(duration_sec)
    
    def set_height(self, target_height_cm, speed=20):
        """특정 높이로 이동"""
        diff = target_height_cm - self.current_height
        if diff > 0:
            self.move_up(diff, speed)
        elif diff < 0:
            self.move_down(abs(diff), speed)
        self.current_height = target_height_cm
    
    # --- 곡선/복합 비행 ---
    
    def fly_arc(self, radius_cm, angle_deg, direction="cw", speed=25):
        """
        원호 비행 (기둥 선회, S자 비행에 사용)
        
        Args:
            radius_cm: 회전 반경
            angle_deg: 회전 각도 (360 = 한 바퀴)
            direction: "cw" (시계방향) 또는 "ccw" (반시계방향)
            speed: 비행 속도
        """
        print(f"[원호비행] 반경={radius_cm}cm, 각도={angle_deg}°, 방향={direction}")
        # ====================================================
        # TODO: SDK에 arc/curve 명령이 있으면 사용
        # 예시:
        #   self.drone.fly_arc(radius_cm, angle_deg, direction)
        #
        # arc 명령이 없으면 아래 이산화(discretize) 방식 사용:
        # 원호를 작은 직선+회전 조합으로 분해
        # ====================================================
        steps = max(4, angle_deg // 30)  # 30도 간격으로 분해
        step_angle = angle_deg / steps
        # 각 스텝에서의 직선 이동 거리 (호의 길이)
        step_distance = 2 * radius_cm * math.sin(math.radians(step_angle / 2))
        
        for i in range(steps):
            self.move_forward(int(step_distance), speed)
            if direction == "cw":
                self.rotate_cw(int(step_angle))
            else:
                self.rotate_ccw(int(step_angle))
        
        print(f"[원호비행] 완료")
    
    def fly_figure_eight(self, radius_cm, speed=25):
        """
        8자 비행 (이중 가로봉 과제용)
        두 기둥 사이를 8자로 비행
        """
        print(f"[8자 비행] 반경={radius_cm}cm")
        # 왼쪽 원호 (반시계)
        self.fly_arc(radius_cm, 360, "ccw", speed)
        # 오른쪽 원호 (시계)
        self.fly_arc(radius_cm, 360, "cw", speed)
        print("[8자 비행] 완료")


# ─────────────────────────────────────────────
# [섹션 2] QR코드 기반 위치 인식
# ─────────────────────────────────────────────

class FieldNavigator:
    """
    필드 QR코드를 이용한 위치 인식 및 네비게이션.
    필드에는 20×20cm QR코드가 배치되어 있으며,
    각 QR코드는 필드 내 좌표를 나타냅니다.
    
    필드 좌표계:
      - 원점(0,0): 좌측 하단 (드론 베이스 위치)
      - X축: 우측 방향 (0~300cm)
      - Y축: 상단 방향 (0~300cm)
    """
    
    # ====================================================
    # 장애물 위치 좌표 (대회 당일 필드 배치에 따라 수정 필수!)
    # 아래는 일반적인 ENJOY AI 필드 배치 기준 예시값입니다.
    # 대회 당일 워밍업 시간에 실제 위치를 확인하고 수정하세요.
    # ====================================================
    
    # 드론 베이스 (좌측 하단, 30×30cm)
    BASE_POS = (15, 15)  # 베이스 중심 좌표
    
    # 장애물 좌표 (x, y) - 단위: cm
    # ※ 대회 당일 반드시 실제 배치 확인 후 수정!
    OBSTACLES = {
        "ring_1":           (100, 100),   # 링 1 (낮은 링)
        "ring_2":           (200, 100),   # 링 2 (높은 링)
        "single_bar":       (100, 200),   # 단일 가로봉 장애물
        "double_bar":       (200, 200),   # 이중 가로봉 장애물
        "pillar_single":    (150, 150),   # 단일 기둥
        "pillar_pair":      (250, 150),   # 두 기둥 (S자 비행용)
        "horizontal_ring":  (150, 250),   # 수평 링 (상승 통과용)
    }
    
    # 장애물별 필요 높이 (cm)
    OBSTACLE_HEIGHTS = {
        "ring_1":          70,   # 낮은 링 중심 높이
        "ring_2":          100,  # 높은 링 중심 높이
        "single_bar":      60,   # 가로봉 아래 통과 높이
        "double_bar":      60,   # 이중 가로봉 통과 높이
        "pillar_single":   80,   # 기둥 선회 높이
        "pillar_pair":     80,   # 두 기둥 S자 비행 높이
        "horizontal_ring": 50,   # 수평 링 아래 접근 높이 (통과 후 상승)
    }
    
    def __init__(self):
        self.current_pos = self.BASE_POS
    
    def read_qr_position(self):
        """
        하단 카메라로 QR코드를 읽어 현재 위치 파악
        
        Returns:
            (x, y) 튜플 또는 None (QR 인식 실패 시)
        """
        # ====================================================
        # TODO: 실제 카메라/QR 인식 코드로 교체
        # 예시:
        #   qr_data = self.drone.camera.read_qr()
        #   if qr_data:
        #       x, y = parse_qr_coordinates(qr_data)
        #       return (x, y)
        #   return None
        # ====================================================
        return self.current_pos
    
    def calculate_move(self, target_name):
        """
        현재 위치에서 목표 장애물까지의 이동량 계산
        
        Args:
            target_name: OBSTACLES 딕셔너리의 키
            
        Returns:
            (dx, dy) 이동해야 할 거리 (cm)
        """
        target = self.OBSTACLES[target_name]
        current = self.read_qr_position() or self.current_pos
        dx = target[0] - current[0]
        dy = target[1] - current[1]
        self.current_pos = target
        return (dx, dy)


# ─────────────────────────────────────────────
# [섹션 3] 미션 수행 클래스
# ─────────────────────────────────────────────

class CompetitionMission:
    """
    대회 미션 전체를 관리하는 메인 클래스.
    
    전략:
    1. 시간 효율 극대화 (180초 제한)
    2. 고배점 과제 우선 수행
    3. 안정적인 비행 경로 설계
    4. 복귀 시간 확보 (마지막 40점)
    
    배점 효율 순위 (점수/난이도):
      1순위: 이륙 (40점, 자동)
      2순위: 이중 가로봉 8자 (180점, 고난도)
      3순위: 링 통과 x2 (100점, 중간)
      4순위: 장애물 통과+회전 (100점, 중간)
      5순위: 두 기둥 S자 (80점, 중간)
      6순위: 수평 링 상승 (70점, 중간)
      7순위: 기둥 선회 (60점, 쉬움)
      8순위: 베이스 복귀 (40점, 필수)
    """
    
    def __init__(self):
        self.drone = DroneController()
        self.nav = FieldNavigator()
        self.score = 0
        self.start_time = None
        self.TIME_LIMIT = 180  # 초
        self.RETURN_BUFFER = 20  # 복귀용 예비 시간 (초)
    
    def elapsed_time(self):
        """경과 시간 (초)"""
        if self.start_time is None:
            return 0
        return time.time() - self.start_time
    
    def remaining_time(self):
        """남은 시간 (초)"""
        return self.TIME_LIMIT - self.elapsed_time()
    
    def should_return(self):
        """복귀해야 하는지 판단"""
        return self.remaining_time() <= self.RETURN_BUFFER
    
    def navigate_to(self, target_name, target_height=None):
        """
        특정 장애물 위치로 이동
        
        Args:
            target_name: 장애물 이름 (FieldNavigator.OBSTACLES 키)
            target_height: 목표 높이 (None이면 자동 설정)
        """
        if self.should_return():
            print(f"[경고] 시간 부족! {target_name} 건너뛰고 복귀합니다.")
            return False
        
        print(f"\n{'='*50}")
        print(f"[이동] → {target_name}")
        print(f"[시간] 경과: {self.elapsed_time():.1f}초 / 남은: {self.remaining_time():.1f}초")
        print(f"{'='*50}")
        
        # 목표까지의 이동량 계산
        dx, dy = self.nav.calculate_move(target_name)
        
        # 높이 조정
        if target_height is None:
            target_height = self.nav.OBSTACLE_HEIGHTS.get(target_name, 80)
        self.drone.set_height(target_height)
        
        # 수평 이동 (X축 → Y축 순서)
        if dx > 0:
            self.drone.move_right(abs(dx))
        elif dx < 0:
            self.drone.move_left(abs(dx))
        
        if dy > 0:
            self.drone.move_forward(abs(dy))
        elif dy < 0:
            self.drone.move_backward(abs(dy))
        
        self.drone.hover(0.5)  # 안정화
        return True
    
    # ─────────────────────────────────────────
    # 과제 1: 이륙 (40점)
    # ─────────────────────────────────────────
    def task_takeoff(self):
        """
        드론 베이스에서 이륙.
        이륙 높이는 첫 번째 과제(링 통과)를 고려하여 설정.
        """
        print("\n" + "▶" * 20)
        print("[과제 1] 이륙 (40점)")
        print("▶" * 20)
        
        self.start_time = time.time()
        self.drone.takeoff(height_cm=80)
        self.drone.hover(1.0)  # 이륙 후 안정화
        
        self.score += 40
        print(f"[점수] +40점 → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 2: 링 통과 (50점 x 2 = 100점)
    # ─────────────────────────────────────────
    def task_ring_pass(self, ring_name, ring_height):
        """
        수직 링 통과.
        링 외경 60cm → 드론이 중앙을 통과해야 함.
        높이 정확도가 핵심.
        
        Args:
            ring_name: "ring_1" 또는 "ring_2"
            ring_height: 링 중심 높이 (cm)
        """
        print(f"\n[과제 2] 링 통과: {ring_name} (50점)")
        
        if not self.navigate_to(ring_name, ring_height):
            return
        
        # 링 앞에서 정렬 후 통과
        # 링은 수직으로 세워져 있으므로 전진하여 통과
        print("[실행] 링 정렬 → 전진 통과")
        self.drone.hover(0.5)        # 정렬 대기
        self.drone.move_forward(80)   # 링을 관통할 충분한 거리
        self.drone.hover(0.5)        # 통과 후 안정화
        
        self.score += 50
        print(f"[점수] +50점 → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 3: 장애물 통과 (40 + 60 = 100점)
    # ─────────────────────────────────────────
    def task_obstacle_pass(self):
        """
        단일 가로봉 장애물:
          - 가로봉 아래 통과: 40점
          - 가로봉 한 바퀴 회전: +60점
        
        전략: 아래 통과 → 상승 → 가로봉 주위 한 바퀴 → 하강
        """
        print("\n[과제 3] 장애물 통과 (40+60 = 100점)")
        
        bar_height = self.nav.OBSTACLE_HEIGHTS["single_bar"]
        
        if not self.navigate_to("single_bar", bar_height - 20):
            return
        
        # Step 1: 가로봉 아래 통과 (40점)
        print("[실행] 가로봉 아래 통과")
        self.drone.move_forward(60)  # 가로봉 아래 통과
        self.drone.hover(0.3)
        
        self.score += 40
        print(f"[점수] +40점 (아래 통과) → 누적: {self.score}점")
        
        # Step 2: 상승 후 가로봉 한 바퀴 회전 (60점)
        print("[실행] 상승 → 가로봉 주위 회전")
        self.drone.move_up(40)            # 가로봉 위로 상승
        self.drone.fly_arc(30, 360, "cw") # 가로봉 주위 한 바퀴
        self.drone.hover(0.3)
        
        self.score += 60
        print(f"[점수] +60점 (가로봉 회전) → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 4: 이중 가로봉 장애물 (40+60+80 = 180점)
    # ─────────────────────────────────────────
    def task_double_bar(self):
        """
        이중 가로봉 장애물:
          - 두 가로봉 사이 통과: 40점
          - 가로봉 하나 주위 회전: +60점
          - 두 가로봉 8자 비행: +80점 (최고 보너스!)
        
        전략: 사이 통과 → 8자 비행으로 한번에 180점 획득
        """
        print("\n[과제 4] 이중 가로봉 장애물 (40+60+80 = 180점)")
        
        if not self.navigate_to("double_bar"):
            return
        
        bar_height = self.nav.OBSTACLE_HEIGHTS["double_bar"]
        
        # Step 1: 두 가로봉 사이 통과 (40점)
        print("[실행] 두 가로봉 사이 통과")
        self.drone.set_height(bar_height)
        self.drone.move_forward(50)  # 사이 통과
        self.drone.hover(0.3)
        
        self.score += 40
        print(f"[점수] +40점 (사이 통과) → 누적: {self.score}점")
        
        # Step 2: 상승 후 가로봉 하나 회전 (60점)
        print("[실행] 가로봉 하나 주위 회전")
        self.drone.move_up(30)
        self.drone.fly_arc(25, 360, "cw")
        self.drone.hover(0.3)
        
        self.score += 60
        print(f"[점수] +60점 (단일 회전) → 누적: {self.score}점")
        
        # Step 3: 8자 비행 (80점)
        print("[실행] 8자 비행 수행")
        self.drone.fly_figure_eight(25)
        self.drone.hover(0.5)
        
        self.score += 80
        print(f"[점수] +80점 (8자 비행) → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 5: 기둥 선회 (60점)
    # ─────────────────────────────────────────
    def task_pillar_orbit(self):
        """
        기둥 주위를 시계 방향 또는 반시계 방향으로 선회.
        시계 방향이 일반적으로 더 안정적.
        """
        print("\n[과제 5] 기둥 선회 (60점)")
        
        if not self.navigate_to("pillar_single"):
            return
        
        # 기둥 주위 선회 (360도)
        print("[실행] 기둥 주위 시계방향 선회")
        self.drone.fly_arc(40, 360, "cw")
        self.drone.hover(0.5)
        
        self.score += 60
        print(f"[점수] +60점 → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 6: 두 기둥 S자 비행 (80점)
    # ─────────────────────────────────────────
    def task_s_flight(self):
        """
        두 기둥 주위를 S자 모양으로 비행.
        기둥을 완전히 선회해도 추가 점수 없음 → S자만 정확히 수행.
        """
        print("\n[과제 6] 두 기둥 S자 비행 (80점)")
        
        if not self.navigate_to("pillar_pair"):
            return
        
        # S자 비행: 첫 번째 기둥을 반시계로 반원 → 두 번째 기둥을 시계로 반원
        print("[실행] S자 비행 수행")
        
        # 첫 번째 기둥 반원 (반시계 방향)
        self.drone.fly_arc(35, 180, "ccw")
        # 두 번째 기둥 반원 (시계 방향)
        self.drone.fly_arc(35, 180, "cw")
        
        self.drone.hover(0.5)
        
        self.score += 80
        print(f"[점수] +80점 → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 7: 수평 링 상승 통과 (70점)
    # ─────────────────────────────────────────
    def task_horizontal_ring(self):
        """
        수평으로 배치된 링(직경 60cm)을 아래에서 위로 통과.
        링 아래로 접근 → 링 중앙 정렬 → 수직 상승하여 통과.
        """
        print("\n[과제 7] 수평 링 상승 통과 (70점)")
        
        ring_bottom_height = self.nav.OBSTACLE_HEIGHTS["horizontal_ring"]
        
        if not self.navigate_to("horizontal_ring", ring_bottom_height):
            return
        
        # 링 아래에서 정렬 후 수직 상승
        print("[실행] 링 아래 정렬 → 수직 상승 통과")
        self.drone.hover(0.5)         # 정확한 위치 정렬
        self.drone.move_up(60)        # 링을 통과할 만큼 상승
        self.drone.hover(0.5)
        
        self.score += 70
        print(f"[점수] +70점 → 누적: {self.score}점")
    
    # ─────────────────────────────────────────
    # 과제 8: 드론 베이스 복귀 (40점)
    # ─────────────────────────────────────────
    def task_return_to_base(self):
        """
        드론 베이스로 복귀하여 착륙.
        드론 상단 투영의 일부가 베이스(30×30cm) 안에 있어야 함.
        
        ★ 반드시 마지막에 수행해야 점수 획득 가능 ★
        """
        print("\n" + "◀" * 20)
        print("[과제 8] 드론 베이스 복귀 (40점)")
        print("◀" * 20)
        
        # 베이스 좌표로 이동
        base = self.nav.BASE_POS
        current = self.nav.read_qr_position() or self.nav.current_pos
        
        dx = base[0] - current[0]
        dy = base[1] - current[1]
        
        print(f"[이동] 베이스까지: dx={dx}cm, dy={dy}cm")
        
        # 안전 높이로 조정 후 이동
        self.drone.set_height(80)
        
        if dx > 0:
            self.drone.move_right(abs(dx))
        elif dx < 0:
            self.drone.move_left(abs(dx))
        
        if dy > 0:
            self.drone.move_forward(abs(dy))
        elif dy < 0:
            self.drone.move_backward(abs(dy))
        
        # 베이스 위에서 착륙
        self.drone.hover(1.0)  # 정확한 위치 확인
        self.drone.land()
        
        self.nav.current_pos = base
        self.score += 40
        print(f"[점수] +40점 (복귀) → 최종: {self.score}점")
    
    # ─────────────────────────────────────────
    # 메인 미션 실행
    # ─────────────────────────────────────────
    def run_mission(self, route="default"):
        """
        전체 미션을 실행합니다.
        
        Args:
            route: 실행 경로 전략
                - "default": 고배점 우선 최적 경로
                - "safe": 안전 우선 (쉬운 과제부터)
                - "speed": 속도 우선 (가까운 과제부터)
        """
        print("=" * 60)
        print("  제3회 국제 창의 AI 드론 경진대회 - 자율비행 시작")
        print("  전략: " + route)
        print("=" * 60)
        
        try:
            # ─── 과제 1: 이륙 (필수, 40점) ───
            self.task_takeoff()
            
            if route == "default":
                # 고배점 우선 최적 경로
                # 이중 가로봉(180점) → 링 통과(100점) → 장애물(100점)
                # → S자(80점) → 수평링(70점) → 기둥(60점) → 복귀
                
                self.task_double_bar()          # 180점
                
                if not self.should_return():
                    self.task_ring_pass("ring_1", 
                                       self.nav.OBSTACLE_HEIGHTS["ring_1"])
                
                if not self.should_return():
                    self.task_ring_pass("ring_2", 
                                       self.nav.OBSTACLE_HEIGHTS["ring_2"])
                
                if not self.should_return():
                    self.task_obstacle_pass()    # 100점
                
                if not self.should_return():
                    self.task_s_flight()         # 80점
                
                if not self.should_return():
                    self.task_horizontal_ring()  # 70점
                
                if not self.should_return():
                    self.task_pillar_orbit()     # 60점
                
            elif route == "safe":
                # 안전 우선: 쉬운 것부터
                self.task_ring_pass("ring_1",
                                   self.nav.OBSTACLE_HEIGHTS["ring_1"])
                
                if not self.should_return():
                    self.task_ring_pass("ring_2",
                                       self.nav.OBSTACLE_HEIGHTS["ring_2"])
                
                if not self.should_return():
                    self.task_pillar_orbit()
                
                if not self.should_return():
                    self.task_obstacle_pass()
                
                if not self.should_return():
                    self.task_s_flight()
                
                if not self.should_return():
                    self.task_horizontal_ring()
                
                if not self.should_return():
                    self.task_double_bar()
            
            elif route == "speed":
                # 속도 우선: 필드 내 최단 경로로 순회
                # (좌표 기반으로 가장 가까운 순서)
                self.task_ring_pass("ring_1",
                                   self.nav.OBSTACLE_HEIGHTS["ring_1"])
                
                if not self.should_return():
                    self.task_obstacle_pass()
                
                if not self.should_return():
                    self.task_pillar_orbit()
                
                if not self.should_return():
                    self.task_ring_pass("ring_2",
                                       self.nav.OBSTACLE_HEIGHTS["ring_2"])
                
                if not self.should_return():
                    self.task_double_bar()
                
                if not self.should_return():
                    self.task_s_flight()
                
                if not self.should_return():
                    self.task_horizontal_ring()
            
            # ─── 과제 8: 베이스 복귀 (필수, 40점) ───
            # ★ 항상 마지막에 실행 ★
            self.task_return_to_base()
            
        except Exception as e:
            print(f"\n[오류 발생] {e}")
            print("[긴급 복귀] 베이스로 복귀 시도...")
            try:
                self.task_return_to_base()
            except:
                self.drone.land()
                print("[긴급 착륙] 완료")
        
        # ─── 결과 출력 ───
        elapsed = self.elapsed_time()
        print("\n" + "=" * 60)
        print(f"  미션 완료!")
        print(f"  총 점수: {self.score}점 / 720점")
        print(f"  소요 시간: {elapsed:.1f}초 / 180초")
        print(f"  남은 시간: {180 - elapsed:.1f}초")
        print("=" * 60)
        
        return self.score


# ─────────────────────────────────────────────
# [섹션 4] 실행
# ─────────────────────────────────────────────

if __name__ == "__main__":
    """
    실행 방법:
    1. DroneController 클래스의 TODO 부분을 실제 SDK로 교체
    2. FieldNavigator.OBSTACLES의 좌표를 실제 필드에 맞게 수정
    3. 아래 route 파라미터로 전략 선택:
       - "default" : 고배점 우선 (추천)
       - "safe"    : 안전 우선 (초보자용)
       - "speed"   : 최단경로 우선
    """
    
    # ========================================
    # 전략 선택 (대회 상황에 따라 변경)
    # ========================================
    STRATEGY = "default"  # "default", "safe", "speed"
    
    mission = CompetitionMission()
    final_score = mission.run_mission(route=STRATEGY)
    
    print(f"\n최종 점수: {final_score}점")
