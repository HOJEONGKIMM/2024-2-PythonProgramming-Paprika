# from fastapi import FastAPI, Query
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# import os

# # FastAPI 앱 초기화
# app = FastAPI()

# # 프론트엔드 경로 설정
# frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
# app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# # 미리 정의된 혼잡도 데이터
# CONGESTION_DATA = []



# # 메인 페이지 엔드포인트
# @app.get("/", response_class=HTMLResponse)
# async def root():
#     """
#     메인 페이지 반환
#     """
#     # 프론트엔드의 index.html 파일 경로
#     frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
#     with open(frontend_path, "r", encoding="utf-8") as file:
#         content = file.read()
#     return content

# # 혼잡도 예측 API
# @app.get("/api/getCongestion")
# async def get_congestion(
#     station: str = Query(...),
#     line: str = Query(...),
#     direction: str = Query(...),
#     time: str = Query(...),
#     dayType: str = Query(...)
# ):
#     """
#     혼잡도 예측 API
#     """
#     # 시간 계산 함수
#     def get_time_offset(base_time, offset_minutes):
#         from datetime import datetime, timedelta
#         time_format = "%H:%M"
#         base_time_obj = datetime.strptime(base_time, time_format)
#         offset_time = base_time_obj + timedelta(minutes=offset_minutes)
#         return offset_time.strftime(time_format)

#     # 30분 앞과 뒤 시간 계산
#     time_previous = get_time_offset(time, -30)
#     time_next = get_time_offset(time, 30)

#     # 데이터 필터링
#     filtered_data = [
#         entry for entry in CONGESTION_DATA
#         if entry["station"] == station and entry["line"] == line and entry["direction"] == direction
#     ]
    
#     # 현재, 이전, 다음 시간 데이터 추출
#     current_data = next((entry for entry in filtered_data if entry["time"] == time), None)
#     previous_data = next((entry for entry in filtered_data if entry["time"] == time_previous), None)
#     next_data = next((entry for entry in filtered_data if entry["time"] == time_next), None)

#     # 결과 반환
#     return {
#         "current": current_data["predicted_congestion"] if current_data else None,
#         "previous": previous_data["predicted_congestion"] if previous_data else None,
#         "next": next_data["predicted_congestion"] if next_data else None,
#         "time_previous": time_previous,
#         "time_next": time_next,
#     }


from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import json
from datetime import datetime, timedelta

# FastAPI 앱 초기화
app = FastAPI()

# 프론트엔드 경로 설정
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# 혼잡도 데이터 로드 함수
def load_congestion_data():
    """
    혼잡도 데이터를 JSON 파일에서 로드
    """
    try:
        current_dir = os.path.dirname(__file__)  # 현재 파일 경로
        json_path = os.path.join(current_dir, "models", "final_result.json")  # 상대 경로
        with open(json_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        raise RuntimeError(f"JSON 데이터 로드 실패: {e}")

# 혼잡도 데이터 로드
CONGESTION_DATA = load_congestion_data()


# 메인 페이지 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    메인 페이지 반환
    """
    # 프론트엔드의 index.html 파일 경로
    try:
        index_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
        with open(index_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html 파일을 찾을 수 없습니다.")


# 혼잡도 예측 API
@app.get("/api/getCongestion")
async def get_congestion(
    station: str = Query(..., description="지하철 역 이름"),
    line: str = Query(..., description="호선 번호"),
    direction: str = Query(..., description="방향 (상행선/하행선)"),
    time: str = Query(..., description="시간 (HH:MM 형식)"),
    dayType: str = Query(..., description="요일 유형 (평일/주말)")
):
    """
    혼잡도 예측 API
    """

    def get_time_offset(base_time, offset_minutes):
        """
        주어진 시간에서 offset만큼 더하거나 뺀 시간 반환
        """
        try:
            time_format = "%H:%M"
            base_time_obj = datetime.strptime(base_time, time_format)
            offset_time = base_time_obj + timedelta(minutes=offset_minutes)
            return offset_time.strftime(time_format)
        except ValueError:
            raise HTTPException(status_code=400, detail="올바른 시간 형식이 아닙니다. HH:MM 형식으로 입력하세요.")

    # 30분 앞과 뒤 시간 계산
    time_previous = get_time_offset(time, -30)
    time_next = get_time_offset(time, 30)

    # 데이터 필터링
    filtered_data = [
        entry for entry in CONGESTION_DATA
        if entry["station"] == station and entry["line"] == line and entry["direction"] == direction
    ]

    if not filtered_data:
        raise HTTPException(status_code=404, detail="입력된 조건에 해당하는 데이터가 없습니다.")

    # 현재, 이전, 다음 시간 데이터 추출
    current_data = next((entry for entry in filtered_data if entry["time"] == time), None)
    previous_data = next((entry for entry in filtered_data if entry["time"] == time_previous), None)
    next_data = next((entry for entry in filtered_data if entry["time"] == time_next), None)

    # 결과 반환
    return {
        "current": current_data["predicted_congestion"] if current_data else None,
        "previous": previous_data["predicted_congestion"] if previous_data else None,
        "next": next_data["predicted_congestion"] if next_data else None,
        "time_previous": time_previous,
        "time_next": time_next,
    }
