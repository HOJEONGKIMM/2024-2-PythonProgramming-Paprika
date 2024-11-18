// 호선과 역 정보
const stationsByLine = {
    "1": ["청량리역", "제기동역", "신설동역", "동묘앞역", "동대문역", "종로5가역", "종로3가역", "종각역", "시청역", "서울역"],
    "2": ["성수역", "뚝섬역", "한양대역", "왕십리역", "상왕십리역", "신당역", "동대문역사문화공원역", "을지로4가역", "을지로3가역", "을지로입구역",
        "시청역", "충정로역", "아현역", "이대역", "신촌(지하)역", "홍대입구역", "합정역", "당산역", "영등포구청역", "문래역", "신도림역",
        "대림역", "구로디지털단지역", "신대방역", "신림역", "봉천역", "서울대입구역", "낙성대역", "사당역", "방배역", "서초역", "교대역", 
        "강남역", "역삼역", "선릉역", "삼성역", "종합운동장역", "잠실새내역", "잠실역", "잠실나루역", "강변역", "구의역", "건대입구역", 
        "성수역", "용답역", "신답역", "용두역", "신설동역"],
    "3": ["지축역", "구파발역", "연신내역", "불광역", "녹번역", "홍제역", "무악재역", "독립문역", "경복궁역", "안국역", "종로3가역",
        "을지로3가역", "충무로역", "동대입구역", "약수역", "금호역", "옥수역", "압구정역", "신사역", "잠원역", "고속터미널역", 
        "교대역", "남부터미널역", "양재역", "매봉역", "도곡역", "대치역", "학여울역", "대청역", "일원역", "수서역", "가락시장역",
        "경찰병원역", "오금역"],
    "4": ["당고개역", "상계역", "노원역", "창동역", "쌍문역", "수유역", "미아역", "미아사거리역", "길음역", "성신여대입구역", 
        "한성대입구역", "혜화역", "동대문역", "동대문역사문화공원역", "충무로역", "명동역", "회현역", "서울역", "숙대입구역", 
        "삼각지역", "신용산역", "이촌역", "동작역", "총신대입구역", "사당역", "남태령역"],
    "5": ["방화역", "개화산역", "김포공항역", "송정역", "마곡역", "발산역", "우장산역", "화곡역", "까치산역", "신정역", "목동역", 
        "오목교역", "양평역", "영등포구청역", "영등포시장역", "신길역", "여의도역", "여의나루역", "마포역", "공덕역", 
        "애오개역", "충정로역", "서대문역", "광화문역", "종로3가역", "을지로4가역", "동대문역사문화공원역", "청구역", 
        "신금호역", "행당역", "왕십리역", "마장역", "답십리역", "장한평역", "군자역", "아차산역", "광나루역", "천호역", "강동(하남)역", 
        "길동역", "굽은다리역", "명일역", "고덕역", "상일동역", "강일역", "미사역", "하남풍산역", "하남시청역", "하남검단산역", 
        "강동(마천)역", "둔촌동역", "올림픽공원(한국체대)역", "방이역", "오금역", "개롱역", "거여역", "마천역"],
    "6": ["응암역", "역촌역", "불광역", "독바위역", "연신내역", "구산역", "새절역", "증산역", "디지털미디어시티역", "월드컵경기장역", 
        "마포구청역", "망원역", "합정역", "상수역", "광흥창역", "대흥역", "공덕역", "효창공원앞역", "삼각지역", "녹사평역", "이태원역",
        "한강진역", "버티고개역", "약수역", "청구역", "신당역", "동묘앞역", "창신역", "보문역", "안암역", "고려대역", "월곡역", "상월곡역", 
        "돌곶이역", "석계역", "태릉입구역", "화랑대역", "봉화산역", "신내역"],
    "7": ["장암역", "도봉산역", "수락산역", "마들역", "노원역", "중계역", "하계역", "공릉역", "태릉입구역", "먹골역", "중화역", "상봉역", 
        "면목역", "사가정역", "용마산역", "중곡역", "군자역", "어린이대공원역", "건대입구역", "자양(뚝섬한강공원)역", "청담역", 
        "강남구청역", "학동역", "논현역", "반포역", "고속터미널역", "내방역", "총신대입구역", "남성역", "숭실대입구역", "상도역", 
        "장승배기역", "신대방삼거리역", "보라매역", "신풍역", "대림역", "남구로역", "가산디지털단지역", "철산역", "광명사거리역", 
        "천왕역", "온수역"],
    "8": ["암사역사공원역", "암사역", "천호역", "강동구청역", "몽촌토성역", "잠실역", "석촌역", "송파역", "가락시장역", "문정역", 
        "장지역", "복정역", "남위례역", "산성역", "남한산성입구역", "단대오거리역", "신흥역", "수진역", "모란역"]
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
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/getCongestion?station=${station}&line=${line}&direction=${direction}&time=${time}&dayType=${dayType}`);
        
        if (!response.ok) {
            throw new Error("API 호출 실패");
        }

        const data = await response.json();

        document.querySelector('.contents-text .fw-bold:nth-of-type(1)').innerText = `${data.current.toFixed(2)}%`;
        document.querySelector('.contents-text .fw-bold:nth-of-type(2)').innerText = `${data.previous.toFixed(2)}%`;
        document.querySelector('.contents-text .fw-bold:nth-of-type(3)').innerText = `${data.next.toFixed(2)}%`;
    } catch (error) {
        console.error("Error fetching congestion data:", error);
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

    const time = `${timeSelect.replace("시", "")}:${minuteSelect.replace("분", "")}`;

    if (station && line && direction && dayType && time) {
        fetchCongestionData(station, line, direction, time, dayType);
    } else {
        alert("모든 입력값을 선택해주세요!");
    }
});
