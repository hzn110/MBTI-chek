import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="iOS Liquid Glass Pokemon",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 초현실적인 애플 리퀴드 글라스(Liquid Glassmorphism) CSS 정의
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');
    
    /* 1. ★ 리퀴드 블루-시안 몽환적 액체 배경 완벽 구현 ★ */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Noto Sans KR", sans-serif;
        background-color: #030515 !important;
        
        /* 캡처 화면 속 쨍한 네온 블루와 시안(Cyan) 리퀴드 액체 광원 표현 */
        background-image: 
            radial-gradient(at 10% 20%, rgba(13, 61, 251, 0.45) 0px, transparent 50%),
            radial-gradient(at 90% 10%, rgba(0, 210, 255, 0.45) 0px, transparent 50%),
            radial-gradient(at 50% 90%, rgba(157, 78, 221, 0.3) 0px, transparent 60%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }
    
    /* 2. 스트림릿 레이아웃 안정화 (절대 깨지지 않음) */
    [data-testid="stAppViewBlockContainer"] {
        background: transparent !important;
    }
    
    /* 3. 폰트 및 타이틀 디자인 */
    .ios-title {
        font-weight: 900;
        font-size: 2.5rem;
        text-align: center;
        letter-spacing: -0.06rem;
        background: linear-gradient(180deg, #ffffff 50%, rgba(255, 255, 255, 0.6) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
        margin-top: -20px;
    }
    
    .ios-subtitle {
        color: rgba(255, 255, 255, 0.5);
        text-align: center;
        font-size: 0.95rem;
        font-weight: 500;
        letter-spacing: 0.05rem;
        margin-bottom: 40px;
        text-transform: uppercase;
    }
    
    /* 4. ★ 핵심: 캡처본과 똑같은 두껍고 쨍한 리퀴드 유리 카드 ★ */
    .liquid-glass-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.11) 0%, rgba(255, 255, 255, 0.02) 100%);
        
        /* 캡처 화면 속 초고밀도 블러 및 증폭 필터 */
        backdrop-filter: blur(45px) saturate(220%); 
        -webkit-backdrop-filter: blur(45px) saturate(220%);
        
        /* 애플 위젯처럼 둥글고 부드러운 모서리 */
        border-radius: 36px; 
        
        /* 리퀴드 글라스의 핵심인 쨍하고 굵은 화이트 하이라이트 아웃라인 */
        border: 1.5px solid rgba(255, 255, 255, 0.28); 
        
        padding: 35px;
        
        /* 외부 묵직한 그림자 + 안쪽 유리의 입체감을 살리는 듀얼 내부 그림자(Inset Shadow) */
        box-shadow: 
            0 40px 80px rgba(0, 4, 30, 0.5), 
            inset 0 1.5px 1.5px rgba(255, 255, 255, 0.4),
            inset 0 -1.5px 1.5px rgba(0, 0, 0, 0.2);
            
        margin-top: 10px;
        margin-bottom: 25px;
    }
    
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
        position: relative;
    }
    
    /* 포켓몬 뒤에 뽀얀 글래스 백그라운드 발광판 추가 */
    .image-section::before {
        content: "";
        position: absolute;
        width: 160px;
        height: 160px;
        background: radial-gradient(circle, rgba(0, 210, 255, 0.3) 0%, transparent 70%);
        filter: blur(20px);
        z-index: 1;
    }
    
    .image-section img {
        width: 100%;
        max-width: 220px;
        height: auto;
        position: relative;
        z-index: 2;
        filter: drop-shadow(0px 15px 30px rgba(0, 210, 255, 0.25));
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .image-section img:hover {
        transform: scale(1.08) translateY(-5px);
    }
    
    .info-section {
        flex: 1.3;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* 텍스트 스타일링 */
    .ios-label {
        font-size: 0.8rem;
        font-weight: 700;
        color: #00d2ff; /* 캡처 화면의 형광 블루 색상 적용 */
        text-transform: uppercase;
        letter-spacing: 0.1rem;
        margin: 0 0 6px 0;
    }
    
    .pokemon-title {
        font-weight: 800;
        font-size: 1.9rem;
        color: #ffffff;
        margin: 0 0 4px 0;
        letter-spacing: -0.04rem;
    }
    
    .pokemon-type {
        color: rgba(255, 255, 255, 0.45);
        font-size: 0.85rem;
        margin: 0 0 15px 0;
    }
    
    /* 유리 느낌을 극대화한 알약 태그 */
    .ios-tag-container {
        display: flex;
        gap: 8px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    
    .ios-tag {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: inset 0 1px 1px rgba(255,255,255,0.2);
        padding: 6px 14px;
        border-radius: 14px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #ffffff;
    }
    
    .pokemon-desc {
        font-size: 0.95rem;
        line-height: 1.65;
        color: rgba(255, 255, 255, 0.85);
        margin: 0;
    }
    
    /* 모바일 반응형 화면 최적화 */
    @media (max-width: 680px) {
        .card-content {
            flex-direction: column;
            text-align: center;
            gap: 25px;
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
    
    /* 5. 스트림릿 셀렉트 박스도 캡처본 위젯 느낌으로 완벽화 */
    div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 18px !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
        box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.15) !important;
    }
    
    label[data-testid="stWidgetLabel"] {
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.08rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 오직 '귀엽고 이쁜' 최고 존엄 포켓몬 데이터 구성
pokemon_db = {
    "ISTJ": {
        "name": "치라치노 (Cinccino)", "id": 573, "type": "노말",
        "tags": ["#깔끔쟁이", "#단정함", "#예의바름"],
        "desc": "하얗고 보드라운 털망토를 두른 치라치노는 먼지 하나 용납하지 않는 깔끔한 성격을 지녔어요. 규칙적이고 완벽한 일 처리를 추구하는 ISTJ의 단정한 매력과 똑 닮았습니다."
    },
    "ISFJ": {
        "name": "멍파치 (Yamper)", "id": 835, "type": "전기",
        "tags": ["#애교쟁이", "#충직함", "#다정다감"],
        "desc": "주인 곁을 든든하게 지키며 꼬리를 살랑이는 사랑스러운 멍파치! 주변 소중한 사람들을 한없이 챙겨주고 배려하는 다정하고 믿음직한 ISFJ의 단짝친구입니다."
    },
    "INFJ": {
        "name": "뮤 (Mew)", "id": 151, "type": "에스퍼",
        "tags": ["#신비로움", "#천사", "#순수함"],
        "desc": "영리하고 맑은 눈망울을 가진 환상의 포켓몬 뮤는 깊은 내면과 신비로운 지혜를 가지고 있어요. 영적인 조화와 이상적인 가치를 쫓는 INFJ의 따뜻한 영혼을 투영합니다."
    },
    "INTJ": {
        "name": "에브이 (Espeon)", "id": 196, "type": "에스퍼",
        "tags": ["#우아함", "#고양이", "#지적인_미녀"],
        "desc": "태양의 기운을 받아 우아하게 빛나는 보랏빛 고양이 에브이. 조용하지만 뛰어난 지적 능력과 독립적인 매력으로 세상을 바라보는 똑똑하고 카리스마 넘치는 INTJ형 포켓몬입니다."
    },
    "ISTP": {
        "name": "나몰빼미 (Rowlet)", "id": 722, "type": "풀 / 비행",
        "tags": ["#동글동글", "#마이웨이", "#침착함"],
        "desc": "동글동글 귀여운 외모 속에 언제나 침착하고 무던한 성격을 감춘 나몰빼미! 불필요한 참견은 거절하며 효율적으로 내 일을 묵묵히 해내는 쿨한 실용주의자 ISTP와 환상의 궁합입니다."
    },
    "ISFP": {
        "name": "메타몽 (Ditto)", "id": 132, "type": "노말",
        "tags": ["#말랑말랑", "#유연함", "#자유로운_영혼"],
        "desc": "말랑말랑하고 귀여운 연보랏빛 메타몽은 정해진 틀 없이 무엇이든 변신할 수 있어요! 매 순간 세상의 미적 감각을 유연하게 느끼며 살아가는 평화로운 예술가 ISFP를 쏙 빼닮았습니다."
    },
    "INFP": {
        "name": "님피아 (Sylveon)", "id": 700, "type": "페어리",
        "tags": ["#파스텔리본", "#로맨틱", "#요정"],
        "desc": "바람에 흩날리는 이쁜 리본 감각과 순수한 마음을 지닌 요정 님피아! 풍부한 감수성과 낭만적인 상상으로 세상을 아름답게 만들기를 꿈꾸는 마음 여린 INFP의 분신입니다."
    },
    "INTP": {
        "name": "물짱이 (Mudkip)", "id": 258, "type": "물",
        "tags": ["#엉뚱함", "#똑똑한_귀요미", "#호기심"],
        "desc": "멍해 보이는 순진한 얼굴로 사실은 레이더 같은 지느러미로 온 세상을 치밀하게 감지하는 물짱이! 혼자 사색하며 온갖 호기심 가득한 가설을 설계하는 영리한 INTP의 매력둥이입니다."
    },
    "ESTP": {
        "name": "염버니 (Scorbunny)", "id": 813, "type": "불꽃",
        "tags": ["#에너자이저", "#활달한_토끼", "#도전주의"],
        "desc": "가슴에 뜨거운 열정을 지니고 쉴 새 없이 발랄하게 뛰어다니는 귀여운 토끼 염버니! 망설임 없이 행동하고 위기를 온몸으로 즐기는 활력 넘치는 ESTP의 페이스메이커입니다."
    },
    "ESFP": {
        "name": "피카츄 (Pikachu)", "id": 25, "type": "전기",
        "tags": ["#아이돌", "#사랑둥이", "#우주의_중심"],
        "desc": "존재 자체가 귀엽고 깜찍한 만인의 사랑 피카츄! 발랄한 스파크로 주변 사람들에게 늘 유쾌한 긍정 에너지와 큰 웃음을 채워주는 쾌활한 분위기 메이커 ESFP의 우상입니다."
    },
    "ENFP": {
        "name": "이브이 (Eevee)", "id": 133, "type": "노말",
        "tags": ["#무한성장", "#사랑스러움", "#모험가"],
        "desc": "폭신한 털과 초롱초롱한 눈으로 무한한 미래의 가능성을 품은 사랑둥이 이브이! 흥미진진한 모험과 새로운 변화를 맞이할 때 가장 반짝이는 열정 가득한 ENFP 그 자체입니다."
    },
    "ENTP": {
        "name": "파치리스 (Pachirisu)", "id": 417, "type": "전기",
        "tags": ["#장난꾸러기", "#재치만점", "#통통튀는"],
        "desc": "통통 튀는 푸른 꼬리를 세우며 호기심 가득한 얼굴로 장난을 궁리하는 파치리스! 기발한 아이디어와 똑 부러지는 재치로 친구들을 즐겁게 만드는 토론광 ENTP와 아주 닮았습니다."
    },
    "ESTJ": {
        "name": "치라미 (Minccino)", "id": 572, "type": "노말",
        "tags": ["#정리대장", "#야무짐", "#리더쉽"],
        "desc": "꼬리를 빗자루 삼아 엉망진창인 곳을 싹 정돈하고 지휘하는 깜찍한 치라미! 탁월한 책임감과 완벽한 계획으로 언제나 솔선수범 모범을 보이는 야무진 카리스마 ESTJ형 포켓몬입니다."
    },
    "ESFJ": {
        "name": "마휘핑 (Alcremie)", "id": 869, "type": "페어리",
        "tags": ["#달콤함", "#모두의_행복", "#러블리 크림"],
        "desc": "달콤한 크림을 나누어주어 주변에 미소와 사교의 행복을 선사하는 마휘핑! 타인의 마음에 깊이 동조하고 집단의 화합과 유대를 따스하게 이끌어내는 사교 천사 ESFJ를 연상시킵니다."
    },
    "ENFJ": {
        "name": "토게피 (Togepi)", "id": 175, "type": "페어리",
        "tags": ["#선한_영향력", "#기쁨의_알", "#희망의_빛"],
        "desc": "세상의 선한 마음과 축복을 가득 품어 모두에게 행운의 희망을 나누어주는 아기 천사 토게피! 타인을 긍정적으로 성장시키고 행복을 이끌어주는 열정적인 영혼 ENFJ의 화신입니다."
    },
    "ENTJ": {
        "name": "식스테일 (Vulpix)", "id": 37, "type": "불꽃",
        "tags": ["#당당함", "#기품있는_여우", "#목표지향"],
        "desc": "귀엽고 풍성한 6개의 꼬리를 한껏 뽐내며 당당하게 걸어 나가는 식스테일! 자존감이 높고 주도면밀하게 자신의 비전을 멋지게 장악해 나가는 당찬 승부사 ENTJ의 우아한 모습입니다."
    }
}

# 4. 헤더 렌더링
st.markdown('<div class="ios-title">✦ LIQUID GLASS ID</div>', unsafe_allow_html=True)
st.markdown('<div class="ios-subtitle">Mbti Sweet Pokemon Widget</div>', unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트 박스
mbti_list = sorted(list(pokemon_db.keys()))
selected_mbti = st.selectbox(
    "CHOOSE YOUR MBTI", 
    mbti_list, 
    index=0
)

# 6. 결과 출력 (초현실적 반응형 리키드 글래스 디스플레이 렌더링)
if selected_mbti:
    pokemon = pokemon_db[selected_mbti]
    
    # 깃허브 오피셜 고화질 투명 PNG 이미지
    img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon['id']}.png"
    
    # 태그 생성
    tags_html = "".join([f'<span class="ios-tag">{tag}</span>' for tag in pokemon['tags']])
    
    # 캡처본 속 고유의 빛 번짐과 입체 유리 각을 그대로 구현한 마크업
    card_html = f"""
    <div class="liquid-glass-card">
        <div class="card-content">
            <div class="image-section">
                <img src="{img_url}" alt="{pokemon['name']}" />
            </div>
            <div class="info-section">
                <p class="ios-label">⚡️ LIQUID GLASS SPEC</p>
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
st.markdown("<p style='text-align: center; color: rgba(255, 255, 255, 0.25); font-size: 0.75rem; font-weight: 500; margin-top: 30px;'>Liquid UI Designed for DangGok High School Dev ✦</p>", unsafe_allow_html=True)
