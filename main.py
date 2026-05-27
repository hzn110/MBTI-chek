import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="iOS MBTI Pokemon",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 아이폰 감성의 세련된 CSS 스타일시트 정의
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');
    
    /* 몽환적인 iOS 배경화면 스타일 그라데이션 */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Noto Sans KR", sans-serif;
        background: radial-gradient(circle at 10% 20%, rgba(98, 54, 255, 0.4) 0%, transparent 50%),
                    radial-gradient(circle at 90% 80%, rgba(255, 54, 153, 0.4) 0%, transparent 50%),
                    #0c0f1d;
        background-attachment: fixed;
        color: #f3f4f6;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    
    /* 헤더 타이틀 */
    .ios-title {
        font-weight: 800;
        font-size: 2.3rem;
        text-align: center;
        letter-spacing: -0.05rem;
        background: linear-gradient(180deg, #ffffff 40%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        margin-top: -20px;
    }
    
    .ios-subtitle {
        color: rgba(255, 255, 255, 0.5);
        text-align: center;
        font-size: 0.95rem;
        font-weight: 400;
        margin-bottom: 35px;
    }
    
    /* 모바일과 데스크톱 모두 끄떡없는 고품격 글래스 카드 구현 */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px) saturate(190%);
        -webkit-backdrop-filter: blur(25px) saturate(190%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        margin-top: 10px;
        margin-bottom: 25px;
    }
    
    /* 카드의 좌우 배치 레이아웃 */
    .card-content {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 35px;
    }
    
    .image-section {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* 네온 느낌의 이미지 그림자 효과 */
    .image-section img {
        width: 100%;
        max-width: 220px;
        height: auto;
        filter: drop-shadow(0px 12px 24px rgba(0,0,0,0.5));
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .image-section img:hover {
        transform: scale(1.08);
    }
    
    .info-section {
        flex: 1.3;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* 디테일 요소 */
    .ios-label {
        font-size: 0.8rem;
        font-weight: 700;
        color: #a5b4fc;
        text-transform: uppercase;
        letter-spacing: 0.08rem;
        margin: 0 0 6px 0;
    }
    
    .pokemon-title {
        font-weight: 800;
        font-size: 1.8rem;
        color: #ffffff;
        margin: 0 0 4px 0;
        letter-spacing: -0.03rem;
    }
    
    .pokemon-type {
        color: rgba(255, 255, 255, 0.45);
        font-size: 0.85rem;
        margin: 0 0 15px 0;
    }
    
    /* 태그 스타일 */
    .ios-tag-container {
        display: flex;
        gap: 8px;
        margin-bottom: 18px;
        flex-wrap: wrap;
    }
    
    .ios-tag {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 5px 12px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.9);
    }
    
    .pokemon-desc {
        font-size: 0.92rem;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.8);
        margin: 0;
    }
    
    /* 미디어 쿼리: 모바일 화면 최적화 (가로 폭이 좁아지면 위아래로 쌓임) */
    @media (max-width: 680px) {
        .card-content {
            flex-direction: column;
            text-align: center;
            gap: 20px;
        }
        .info-section {
            align-items: center;
        }
        .ios-tag-container {
            justify-content: center;
        }
        .image-section img {
            max-width: 160px;
        }
    }
    
    /* 스트림릿 기본 선택 박스 세련되게 수정 */
    div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 14px !important;
        backdrop-filter: blur(10px);
    }
    
    /* 셀렉트 박스 라벨 색상 변경 */
    label[data-testid="stWidgetLabel"] {
        color: rgba(255, 255, 255, 0.6) !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.05rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 데이터 구성 (오피셜 도감 ID 부여로 핫링크 에러 100% 극복!)
pokemon_db = {
    "ISTJ": {
        "name": "망나뇽 (Dragonite)", "id": 149, "type": "드래곤 / 비행",
        "tags": ["#원칙주의", "#성실함", "#완벽주의"],
        "desc": "한번 시작한 일은 끝까지 완수하는 책임감의 아이콘. 원칙적이고 믿음직한 모습이 ISTJ와 꼭 닮았습니다."
    },
    "ISFJ": {
        "name": "해피너스 (Blissey)", "id": 242, "type": "노말",
        "tags": ["#수호자", "#따뜻함", "#배려심"],
        "desc": "주변 사람들의 행복과 평안을 지키기 위해 온 힘을 다하는 상냥한 영혼, 해피너스는 따뜻한 ISFJ의 안식처입니다."
    },
    "INFJ": {
        "name": "가디안 (Gardevoir)", "id": 282, "type": "에스퍼 / 페어리",
        "tags": ["#통찰력", "#신비함", "#조력자"],
        "desc": "사람들의 마음 깊은 곳을 꿰뚫어 보고 보이지 않는 선을 실천하는 가디안은 통찰력 깊고 이타적인 INFJ를 대변합니다."
    },
    "INTJ": {
        "name": "뮤츠 (Mewtwo)", "id": 150, "type": "에스퍼",
        "tags": ["#전략가", "#독립성", "#이성적"],
        "desc": "빈틈없는 분석력과 차가운 카리스마를 지닌 고독한 천재 뮤츠는 장기적인 비전을 품고 실행하는 INTJ의 모습입니다."
    },
    "ISTP": {
        "name": "루카리오 (Lucario)", "id": 448, "type": "격투 / 강철",
        "tags": ["#해결사", "#침착함", "#실용주의"],
        "desc": "말보다는 행동으로, 위기 상황에서 가장 냉철하게 빛나는 장인 루카리오는 도구를 잘 다루고 관찰력이 뛰어난 ISTP입니다."
    },
    "ISFP": {
        "name": "메타몽 (Ditto)", "id": 132, "type": "노말",
        "tags": ["#유연함", "#자유로움", "#예술가"],
        "desc": "어디에도 구속되지 않고 주위 환경에 자연스럽게 동화하는 메타몽은 유연한 영혼과 미적 감각을 지닌 예술가 ISFP와 같습니다."
    },
    "INFP": {
        "name": "님피아 (Sylveon)", "id": 700, "type": "페어리",
        "tags": ["#감수성", "#이상주의", "#낭만"],
        "desc": "마음의 눈으로 세상을 보고 따뜻한 공감을 나누는 페어리 님피아는 순수한 이상과 상상력 가득한 INFP의 단짝입니다."
    },
    "INTP": {
        "name": "폴리곤 (Porygon)", "id": 137, "type": "노말",
        "tags": ["#분석가", "#호기심", "#논리력"],
        "desc": "디지털 데이터 속 숨겨진 원리와 논리를 찾아내는 탐구자 폴리곤은 끊임없이 생각하고 검증하는 아이디어 뱅크 INTP입니다."
    },
    "ESTP": {
        "name": "윈디 (Arcanine)", "id": 59, "type": "불꽃",
        "tags": ["#행동파", "#에너지", "#승부사"],
        "desc": "스릴 넘치는 도전을 즐기며 한발 앞서 달리는 불꽃 기운의 윈디는 뛰어난 현실 감각과 추진력을 지닌 ESTP입니다."
    },
    "ESFP": {
        "name": "피카츄 (Pikachu)", "id": 25, "type": "전기",
        "tags": ["#인싸", "#친화력", "#분위기메이커"],
        "desc": "모두의 관심과 사랑을 한몸에 받으며 활기찬 긍정 에너지를 전파하는 피카츄는 사교적이고 즐거움을 쫓는 ESFP 그 자체입니다."
    },
    "ENFP": {
        "name": "이브이 (Eevee)", "id": 133, "type": "노말",
        "tags": ["#잠재력", "#모험가", "#창의성"],
        "desc": "어디로 진화할지 모르는 수많은 잠재력과 상상력을 품은 이브이는 새로운 도전에 가슴 설레는 낙천주의자 ENFP입니다."
    },
    "ENTP": {
        "name": "팬텀 (Gengar)", "id": 94, "type": "고스트 / 독",
        "tags": ["#혁신가", "#재치", "#도전적"],
        "desc": "기존의 틀을 깨는 흥미로운 생각과 유쾌한 변칙을 만들어내는 천재 장난꾸러기 팬텀은 토론을 즐기고 브레인스토밍을 좋아하는 ENTP입니다."
    },
    "ESTJ": {
        "name": "괴력몬 (Machamp)", "id": 68, "type": "격투",
        "tags": ["#지도자", "#규율성", "#결단력"],
        "desc": "체계적이고 단호한 행동력으로 공동체를 안전하고 정교하게 리드하는 괴력몬은 계획적이고 확실한 결과를 선호하는 ESTJ입니다."
    },
    "ESFJ": {
        "name": "럭키 (Chansey)", "id": 113, "type": "노말",
        "tags": ["#사교적", "#리액션", "#협력자"],
        "desc": "모두와 원만하게 지내며 아낌없는 리액션과 지지를 보내는 럭키는 동료애가 가득하고 집단의 조화를 돕는 다정다감한 ESFJ입니다."
    },
    "ENFJ": {
        "name": "토게키스 (Togekiss)", "id": 468, "type": "페어리 / 비행",
        "tags": ["#멘토", "#리더십", "#선한영향력"],
        "desc": "모두가 평화롭고 한 단계 성장할 수 있도록 앞장서 이끌어주는 영웅 토게키스는 정의롭고 따뜻한 등대 같은 ENFJ입니다."
    },
    "ENTJ": {
        "name": "마기라스 (Tyranitar)", "id": 248, "type": "바위 / 악",
        "tags": ["#사령관", "#야망", "#강한의지"],
        "desc": "거침없는 결단력과 강력한 카리스마로 공동의 목표를 확실하게 쟁취해내는 마기라스는 타고난 야망가이자 전략적 리더인 ENTJ입니다."
    }
}

# 4. 헤더 렌더링
st.markdown('<div class="ios-title">✦ POKÉMON ID</div>', unsafe_allow_html=True)
st.markdown('<div class="ios-subtitle">Glassmorphism Profile 추천 서비스</div>', unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트 박스
mbti_list = sorted(list(pokemon_db.keys()))
selected_mbti = st.selectbox(
    "CHOOSE YOUR MBTI", 
    mbti_list, 
    index=0
)

# 6. 결과 출력 (모던 반응형 단일 HTML 카드 렌더링)
if selected_mbti:
    pokemon = pokemon_db[selected_mbti]
    
    # 깨지지 않고 배경이 완전히 투명해 멋지게 조화되는 오피셜 GitHub 이미지
    img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon['id']}.png"
    
    # 태그 HTML 생성
    tags_html = "".join([f'<span class="ios-tag">{tag}</span>' for tag in pokemon['tags']])
    
    # 전체를 하나의 완벽한 HTML 구조로 묶어서 st.markdown 출력!
    card_html = f"""
    <div class="glass-card">
        <div class="card-content">
            <div class="image-section">
                <img src="{img_url}" alt="{pokemon['name']}" />
            </div>
            <div class="info-section">
                <p class="ios-label">⚡ SOUL POKÉMON</p>
                <h2 class="pokemon-title">{pokemon['name']}</h2>
                <p class="pokemon-type">타입 : {pokemon['type']}</p>
                <div class="ios-tag-container">
                    {tags_html}
                </div>
                <p class="pokemon-desc">{pokemon['desc']}</p>
            </div>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)

# 하단 푸터
st.markdown("<p style='text-align: center; color: rgba(255, 255, 255, 0.25); font-size: 0.75rem; font-weight: 500; margin-top: 30px;'>Designed like iOS Widget by DangGok Dev</p>", unsafe_allow_html=True)
