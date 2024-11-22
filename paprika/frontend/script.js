// 호선과 역 정보
const stationsByLine = {
    "1": ["청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각", "시청", "서울"],
    "2": ["성수", "뚝섬", "한양대", "왕십리", "상왕십리", "신당", "동대문역사문화공원", "을지로4가", "을지로3가", 
        "을지로입구", "시청", "충정로", "아현", "이대", "신촌(지하)", "홍대입구", "합정", "당산", "영등포구청", 
        "문래", "신도림", "대림", "구로디지털단지", "신대방", "신림", "봉천", "서울대입구", "낙성대", "사당", "방배",
         "서초", "교대",  "강남", "역삼", "선릉", "삼성", "종합운동장", "잠실새내", "잠실", "잠실나루", "강변", "구의",
          "건대입구",  "성수", "용답", "신답", "용두", "신설동"],
    "3": ["지축", "구파발", "연신내", "불광", "녹번", "홍제", "무악재", "독립문", "경복궁", "안국", "종로3가",
        "을지로3가", "충무로", "동대입구", "약수", "금호", "옥수", "압구정", "신사", "잠원", "고속터미널", 
        "교대", "남부터미널", "양재", "매봉", "도곡", "대치", "학여울", "대청", "일원", "수서", "가락시장",
        "경찰병원", "오금"],
    "4": ["당고개", "상계", "노원", "창동", "쌍문", "수유", "미아", "미아사거리", "길음", "성신여대입구", 
        "한성대입구", "혜화", "동대문", "동대문역사문화공원", "충무로", "명동", "회현", "서울", "숙대입구", 
        "삼각지", "신용산", "이촌", "동작", "총신대입구", "사당", "남태령"],
    "5": ["방화", "개화산", "김포공항", "송정", "마곡", "발산", "우장산", "화곡", "까치산", "신정", "목동", 
        "오목교", "양평", "영등포구청", "영등포시장", "신길", "여의도", "여의나루", "마포", "공덕", 
        "애오개", "충정로", "서대문", "광화문", "종로3가", "을지로4가", "동대문역사문화공원", "청구", 
        "신금호", "행당", "왕십리", "마장", "답십리", "장한평", "군자", "아차산", "광나루", "천호역", "강동(하남)역", 
        "길동", "굽은다리", "명일", "고덕", "상일동", "강일", "미사", "하남풍산", "하남시청", "하남검단산", 
        "강동(마천)", "둔촌동", "올림픽공원(한국체대)", "방이", "오금", "개롱", "거여", "마천"],
    "6": ["응암", "역촌", "불광", "독바위", "연신내", "구산", "새절", "증산", "디지털미디어시티", "월드컵경기장",  
        "마포구청", "망원", "합정", "상수", "광흥창", "대흥", "공덕", "효창공원앞", "삼각지", "녹사평", "이태원", "한강진", 
        "버티고개", "약수", "청구", "신당", "동묘앞", "창신", "보문", "안암", "고려대", "월곡", "상월곡",  "돌곶이", "석계", 
        "태릉입구", "화랑대", "봉화산", "신내"],
    "7": ['장암', '도봉산', '수락산', '마들', '노원', '중계', '하계', '공릉', '태릉입구', '먹골', '중화', 
        '상봉',  '면목', '사가정', '용마산', '중곡', '군자', '어린이대공원', '건대입구', '자양(뚝섬한강공원)', '청담',  
        '강남구청', '학동', '논현', '반포', '고속터미널', '내방', '총신대입구', '남성', '숭실대입구', '상도',  '장승배기', 
        '신대방삼거리', '보라매', '신풍', '대림', '남구로', '가산디지털단지', '철산', '광명사거리',  '천왕', '온수']    ,
    "8": ["암사역사공원", "암사", "천호", "강동구청", "몽촌토성", "잠실", "석촌", "송파", "가락시장", "문정",  "장지",
        "복정", "남위례", "산성", "남한산성입구", "단대오거리", "신흥", "수진", "모란"]

};

// 방향 정보
const directionsByLine = {
    "1": ["상선", "하선"],
    "2": ["내선", "외선"],
    "3": ["상선", "하선"],
    "4": ["상선", "하선"],
    "5": ["상선", "하선"],
    "6": ["상선", "하선"],
    "7": ["상선", "하선"],
    "8": ["상선", "하선"]
};

// 호선 변경 시 출발역 옵션 업데이트
function updateStationOptions() {
    const lineSelect = document.getElementById("line-select");
    const stationSelect = document.getElementById("station-select");
    const selectedLine = lineSelect.value;

    stationSelect.innerHTML = '<option selected>출발역 선택</option>';

    if (stationsByLine[selectedLine]) {
        stationsByLine[selectedLine].forEach(station => {
            const option = document.createElement("option");
            option.value = station;
            option.textContent = station;
            stationSelect.appendChild(option);
        });
    }
}

// 상/하선 옵션 업데이트
function updateDirectionOptions() {
    const lineSelect = document.getElementById("line-select");
    const directionSelect = document.getElementById("direction-select");
    const selectedLine = lineSelect.value;

    directionSelect.innerHTML = '<option selected>상/하선 선택</option>';

    if (directionsByLine[selectedLine]) {
        directionsByLine[selectedLine].forEach(direction => {
            const option = document.createElement("option");
            option.value = direction;
            option.textContent = direction;
            directionSelect.appendChild(option);
        });
    }
}

// 혼잡도 API 호출 및 데이터 업데이트
async function fetchCongestionData(station, line, direction, time, dayType) {
    // API 요청
    const response = await fetch(`http://127.0.0.1:8000/api/getCongestion?station=${station}&line=${line}&direction=${direction}&time=${time}&dayType=${dayType}`);
    
    // API 요청 성공 여부 확인
    if (response.ok) {
        const data = await response.json();

        // 현재 혼잡도 업데이트
        const currentCongestion = data.current !== null ? `${data.current.toFixed(2)}` : "데이터 없음";
        document.querySelector('.contents-text .fw-bold:nth-of-type(1)').innerText = currentCongestion;

        // 30분 전 혼잡도 업데이트
        const previousCongestion = data.previous !== null ? `${data.previous.toFixed(2)}` : "데이터 없음";
        document.querySelector('.contents-text .fw-bold:nth-of-type(2)').innerText = previousCongestion;

        // 30분 후 혼잡도 업데이트
        const nextCongestion = data.next !== null ? `${data.next.toFixed(2)}%` : "데이터 없음";
        document.querySelector('.contents-text .fw-bold:nth-of-type(3)').innerText = nextCongestion;
    } else {
        // API 요청 실패 시 처리
        document.querySelector('.contents-text .fw-bold:nth-of-type(1)').innerText = "API 호출 실패";
        document.querySelector('.contents-text .fw-bold:nth-of-type(2)').innerText = "API 호출 실패";
        document.querySelector('.contents-text .fw-bold:nth-of-type(3)').innerText = "API 호출 실패";
    }
}


// 입력 값 검증 후 혼잡도 데이터 요청
document.getElementById("fetch-button").addEventListener("click", () => {
    const station = document.getElementById("station-select").value;
    const line = document.getElementById("line-select").value;
    const direction = document.getElementById("direction-select").value;
    const dayType = document.getElementById("day-type-select").value;
    const timeSelect = document.getElementById("time-select").value;
    const minuteSelect = document.getElementById("minute-select").value;

    // 시간 입력값 포맷팅 (예: "05:30")
    const time = `${timeSelect.replace("시", "")}:${minuteSelect.replace("분", "")}`;

    // 입력값 검증
    if (station && line && direction && dayType && time) {
        fetchCongestionData(station, line, direction, time, dayType);
    } else {
        alert("모든 입력값을 선택해주세요!");
    }
});
