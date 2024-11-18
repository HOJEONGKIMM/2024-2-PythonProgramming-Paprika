from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError  # mse를 명시적으로 등록
import numpy as np
import os


# FastAPI 앱 초기화
app = FastAPI()

# 프론트엔드 경로 설정
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# LSTM 모델 로드 (custom_objects로 'mse' 등록)
model = load_model(
    "models/congestion_prediction_model_lstm.h5",
    custom_objects={'mse': MeanSquaredError()}
)

# direction 매핑 사전
DIRECTION_MAP = {
    "상선": 0,
    "하선": 1,
    "내선": 0,  # 내선을 기본적으로 '상선(0)'으로 처리
    "외선": 1   # 외선을 기본적으로 '하선(1)'으로 처리
}

# 데이터 모델 정의
class CongestionRequest(BaseModel):
    station: str
    line: str
    direction: str
    time: str
    dayType: str

# 예측 함수
def predict_congestion(input_data):
    # LSTM 모델에 데이터 전달
    input_array = np.array([input_data])  # 모델 입력 형태로 변환
    prediction = model.predict(input_array)
    return float(prediction[0])

# 메인 페이지 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    메인 페이지 반환
    """
    # 프론트엔드의 index.html 파일 경로
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    with open(frontend_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

# 혼잡도 예측 API
@app.get("/api/getCongestion")
async def get_congestion(
    station: str = Query(...),
    line: str = Query(...),
    direction: str = Query(...),
    time: str = Query(...),
    dayType: str = Query(...)
):
    """
    혼잡도 예측 API
    """
    # direction 값을 정수로 매핑 (기본 값으로 처리)
    direction_numeric = DIRECTION_MAP.get(direction, 0)  # 없는 값은 기본적으로 '상선(0)' 처리

    # 모델 입력 데이터 생성
    time_hour = int(time.split(":")[0])
    day_numeric = 0 if dayType == "weekday" else 1  # 평일/주말 변환
    input_data = [len(station), int(line), direction_numeric, time_hour, day_numeric]

    # 예측 수행
    current_congestion = predict_congestion(input_data)

    # 과거/미래 혼잡도 샘플 생성 (단순히 ±5% 변화를 가정)
    previous_congestion = max(0, current_congestion - 5)
    next_congestion = min(100, current_congestion + 5)

    # 결과 반환
    return {
        "current": current_congestion,
        "previous": previous_congestion,
        "next": next_congestion,
    }
