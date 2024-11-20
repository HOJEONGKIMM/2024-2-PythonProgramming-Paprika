# from fastapi import FastAPI, Query
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# from tensorflow.keras.models import load_model
# from tensorflow.keras.losses import MeanSquaredError  # mse를 명시적으로 등록
# import numpy as np
# import os


# # FastAPI 앱 초기화
# app = FastAPI()

# # 프론트엔드 경로 설정
# frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
# app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# # LSTM 모델 로드 (custom_objects로 'mse' 등록)
# model = load_model(
#     "models/congestion_prediction_model_lstm.h5",
#     custom_objects={'mse': MeanSquaredError()}
# )

# # direction 매핑 사전
# DIRECTION_MAP = {
#     "상선": 0,
#     "하선": 1,
#     "내선": 0,  # 내선을 기본적으로 '상선(0)'으로 처리
#     "외선": 1   # 외선을 기본적으로 '하선(1)'으로 처리
# }

# # 데이터 모델 정의
# class CongestionRequest(BaseModel):
#     station: str
#     line: str
#     direction: str
#     time: str
#     dayType: str

# # 예측 함수
# def predict_congestion(input_data):
#     # LSTM 모델에 데이터 전달
#     input_array = np.array([input_data])  # 모델 입력 형태로 변환
#     prediction = model.predict(input_array)
#     return float(prediction[0])

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
#     # direction 값을 정수로 매핑 (기본 값으로 처리)
#     direction_numeric = DIRECTION_MAP.get(direction, 0)  # 없는 값은 기본적으로 '상선(0)' 처리

#     # 모델 입력 데이터 생성
#     time_hour = int(time.split(":")[0])
#     day_numeric = 0 if dayType == "weekday" else 1  # 평일/주말 변환
#     input_data = [len(station), int(line), direction_numeric, time_hour, day_numeric]

#     # 예측 수행
#     current_congestion = predict_congestion(input_data)

#     # 과거/미래 혼잡도 샘플 생성 (단순히 ±5% 변화를 가정)
#     previous_congestion = max(0, current_congestion - 5)
#     next_congestion = min(100, current_congestion + 5)

#     # 결과 반환
#     return {
#         "current": current_congestion,
#         "previous": previous_congestion,
#         "next": next_congestion,
#     }



from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

# FastAPI 앱 초기화
app = FastAPI()

# 프론트엔드 경로 설정
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# 미리 정의된 혼잡도 데이터
CONGESTION_DATA = [
    {"station": "청량리", "line": "1", "direction": "상선", "time": "5:30", "predicted_congestion": 8.912764710187913},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "6:00", "predicted_congestion": 20.600160616636277},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "6:30", "predicted_congestion": 9.210353583097458},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "7:00", "predicted_congestion": 20.62118992209435},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "7:30", "predicted_congestion": 8.174793934822084},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "8:00", "predicted_congestion": 20.95724342465401},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "8:30", "predicted_congestion": 7.401058530807496},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "9:00", "predicted_congestion": 13.092983919382096},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "9:30", "predicted_congestion": 8.970024597644807},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "10:00", "predicted_congestion": 12.702482503652574},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "10:30", "predicted_congestion": 6.09355731010437},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "11:00", "predicted_congestion": 12.112802284955979},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "11:30", "predicted_congestion": 6.6409405231475835},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "12:00", "predicted_congestion": 11.182602274417878},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "12:30", "predicted_congestion": 7.662483644485475},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "13:00", "predicted_congestion": 9.314588069915771},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "13:30", "predicted_congestion": 7.782728505134584},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "14:00", "predicted_congestion": 8.41958920955658},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "14:30", "predicted_congestion": 7.469571733474732},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "15:00", "predicted_congestion": 10.178326517343523},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "15:30", "predicted_congestion": 7.422571849822999},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "16:00", "predicted_congestion": 17.19718049168587},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "16:30", "predicted_congestion": 8.058204460144044},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "17:00", "predicted_congestion": 18.643223369121554},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "17:30", "predicted_congestion": 10.724730867147446},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "18:00", "predicted_congestion": 18.742800128459933},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "18:30", "predicted_congestion": 14.410490494966508},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "19:00", "predicted_congestion": 20.692197239398958},
    {"station": "청량리", "line": "1", "direction": "상선", "time": "19:30", "predicted_congestion": 16.50887167453766},
    {
        "station": "뚝섬",
        "line": "1",
        "direction": "상선",
        "time": "5:30",
        "predicted_congestion": 8.912764710187913
    },
    {
        "station": "뚝섬",
        "line": "1",
        "direction": "상선",
        "time": "6:00",
        "predicted_congestion": 20.600160616636277
    },
    {
        "station": "뚝섬",
        "line": "1",
        "direction": "상선",
        "time": "6:30",
        "predicted_congestion": 9.210353583097458
    },
    {
        "station": "뚝섬",
        "line": "1",
        "direction": "상선",
        "time": "7:00",
        "predicted_congestion": 20.62118992209435
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "7:30",
        "predicted_congestion": 8.174793934822084
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "8:00",
        "predicted_congestion": 20.95724342465401
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "8:30",
        "predicted_congestion": 7.401058530807496
    },
    {
        "station": "뚝섬",
        "line": "1",
        "direction": "상선",
        "time": "9:00",
        "predicted_congestion": 13.092983919382096
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "9:30",
        "predicted_congestion": 8.970024597644807
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "10:00",
        "predicted_congestion": 12.702482503652574
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "10:30",
        "predicted_congestion": 6.09355731010437
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "11:00",
        "predicted_congestion": 12.112802284955979
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "11:30",
        "predicted_congestion": 6.6409405231475835
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "12:00",
        "predicted_congestion": 11.182602274417878
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "12:30",
        "predicted_congestion": 7.662483644485475
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "13:00",
        "predicted_congestion": 9.314588069915771
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "13:30",
        "predicted_congestion": 7.782728505134584
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "14:00",
        "predicted_congestion": 8.41958920955658
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "14:30",
        "predicted_congestion": 7.469571733474732
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "15:00",
        "predicted_congestion": 10.178326517343523
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "15:30",
        "predicted_congestion": 7.422571849822999
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "16:00",
        "predicted_congestion": 17.19718049168587
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "16:30",
        "predicted_congestion": 8.058204460144044
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "17:00",
        "predicted_congestion": 18.643223369121554
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "17:30",
        "predicted_congestion": 10.724730867147446
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "18:00",
        "predicted_congestion": 18.742800128459933
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "18:30",
        "predicted_congestion": 14.410490494966508
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "19:00",
        "predicted_congestion": 20.692197239398958
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "19:30",
        "predicted_congestion": 16.50887167453766
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "20:00",
        "predicted_congestion": 18.28812537789345
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "20:30",
        "predicted_congestion": 19.010829859972002
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "21:00",
        "predicted_congestion": 21.24344894886017
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "21:30",
        "predicted_congestion": 14.891105121374132
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "22:00",
        "predicted_congestion": 13.98511301279068
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "22:30",
        "predicted_congestion": 14.858340293169023
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "23:00",
        "predicted_congestion": 14.266019672155382
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "23:30",
        "predicted_congestion": 14.101245564222337
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "0:00",
        "predicted_congestion": 14.11254764199257
    },
    {
        "station": "뚝섬",
        "line": "2",
        "direction": "상선",
        "time": "0:30",
        "predicted_congestion": 8.796747744083405
    },
    {
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "5:30",
    "predicted_congestion": 8.912764710187913
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "6:00",
    "predicted_congestion": 20.600160616636277
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "6:30",
    "predicted_congestion": 9.210353583097458
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "7:00",
    "predicted_congestion": 20.62118992209435
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "7:30",
    "predicted_congestion": 8.174793934822084
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "8:00",
    "predicted_congestion": 20.95724342465401
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "8:30",
    "predicted_congestion": 7.401058530807496
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "9:00",
    "predicted_congestion": 13.092983919382096
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "9:30",
    "predicted_congestion": 8.970024597644807
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "10:00",
    "predicted_congestion": 12.702482503652574
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "10:30",
    "predicted_congestion": 6.09355731010437
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "11:00",
    "predicted_congestion": 12.112802284955979
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "11:30",
    "predicted_congestion": 6.6409405231475835
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "12:00",
    "predicted_congestion": 11.182602274417878
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "12:30",
    "predicted_congestion": 7.662483644485475
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "13:00",
    "predicted_congestion": 9.314588069915771
},
{
    "station": "독립문",
    "line": "3",
    "direction": "상선",
    "time": "13:30",
    "predicted_congestion": 7.782728505134584
},
{
    "station": "을지로3가",
    "line": "3",
    "direction": "상선",
    "time": "5:30",
    "predicted_congestion": 8.912764710187913
},
{
    "station": "을지로3가",
    "line": "3",
    "direction": "상선",
    "time": "6:00",
    "predicted_congestion": 20.600160616636277
},
{
    "station": "을지로3가",
    "line": "3",
    "direction": "상선",
    "time": "6:30",
    "predicted_congestion": 9.210353583097458
}

]



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
    # 시간 계산 함수
    def get_time_offset(base_time, offset_minutes):
        from datetime import datetime, timedelta
        time_format = "%H:%M"
        base_time_obj = datetime.strptime(base_time, time_format)
        offset_time = base_time_obj + timedelta(minutes=offset_minutes)
        return offset_time.strftime(time_format)

    # 30분 앞과 뒤 시간 계산
    time_previous = get_time_offset(time, -30)
    time_next = get_time_offset(time, 30)

    # 데이터 필터링
    filtered_data = [
        entry for entry in CONGESTION_DATA
        if entry["station"] == station and entry["line"] == line and entry["direction"] == direction
    ]
    
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
