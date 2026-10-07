from datetime import datetime
import random
import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title='오늘의 운세 프로그램', page_icon='✨', layout='centered'
)

# --- 운세 데이터 풀 ---
zodiac_signs = [
    '쥐띠',
    '소띠',
    '호랑이띠',
    '토끼띠',
    '용띠',
    '뱀띠',
    '말띠',
    '양띠',
    '원숭이띠',
    '닭띠',
    '개띠',
    '돼지띠',
]

luck_levels = ['최고의 하루! 🌟', '행운이 가득한 날 ✨', '평온하고 무난한 하루 🍀', '조심스런 주의가 필요한 날 ⚠️']

overall_fortunes = [
    '생각지도 못한 곳에서 기쁜 소식이 들려오는 하루입니다. 적극적으로 움직여 보세요.',
    '작은 노력이 큰 결실로 돌아오는 보람찬 하루입니다. 자신감을 가지세요.',
    '주변 사람들과의 원만한 소통이 행운을 불러옵니다. 귀인의 도움이 따를 수 있습니다.',
    '급할수록 돌아가라는 말이 잇듯이, 차분하게 일상을 점검하는 여유가 필요합니다.',
    '오랫동안 고민하던 문제가 자연스럽게 해결되면서 마음의 안정을 찾게 됩니다.',
]

wealth_fortunes = [
    '뜻밖의 수입이 생기거나 재물 운이 상승하는 길일입니다.',
    '지출이 발생할 수 있으나, 가치 있는 곳에 쓰이므로 걱정하지 않아도 됩니다.',
    '안정적인 자금 흐름을 유지합니다. 무리한 투자보다는 저축에 집중하세요.',
    '주변의 솔깃한 정보에 흔들리지 말고 본인의 판단을 믿어야 하는 날입니다.',
]

love_fortunes = [
    '솔로라면 새로운 인연을 만날 수 있는 설레는 기회가 찾아옵니다.',
    '연인이 있다면 작은 이벤트나 따뜻한 말 한마디로 사랑이 더욱 깊어집니다.',
    '주변 사람들에게 베푼 친절이 따뜻한 인연으로 돌아오는 하루입니다.',
    '가까운 사람과의 오해가 생기지 않도록 진심 어린 대화를 나눠보세요.',
]

work_fortunes = [
    '아이디어가 반짝이는 날로, 중요한 업무나 프로젝트에서 두각을 나타낼 수 있습니다.',
    '동료나 상사와의 협력이 빛을 발하여 좋은 성과를 거두는 시기입니다.',
    '꼼꼼한 마감 체크와 서류 검토가 중요한 하루입니다. 실수를 예방하세요.',
    '잠시 휴식을 취하며 재충전의 시간을 갖는 것이 장기적인 업무에 도움이 됩니다.',
]


def get_daily_fortune(zodiac):
  # 오늘 날짜와 띠 조합으로 고정된 시드(Seed) 생성 (하루 동안 같은 띠는 같은 운세 유지)
  today_str = datetime.now().strftime('%Y%m%d')
  seed_val = int(today_str) + hash(zodiac)
  random.seed(seed_val)

  return {
      'level': random.choice(luck_levels),
      'overall': random.choice(overall_fortunes),
      'wealth': random.choice(wealth_fortunes),
      'love': random.choice(love_fortunes),
      'work': random.choice(work_fortunes),
  }


# --- UI 구성 ---
st.title('🔮 오늘의 운세 확인하기')
st.markdown(
    f'오늘은 **{datetime.now().strftime("%Y년 %m월 %d일")}**입니다. 나의 띠를'
    ' 선택하고 오늘의 운세를 확인해 보세요!'
)
st.markdown('---')

# 띠 선택 드롭다운
selected_zodiac = st.selectbox('자신의 띠를 선택하세요:', zodiac_signs)

if st.button('운세 확인하기 ✨', type='primary'):
  with st.spinner('운세를 불러오는 중입니다...'):
    fortune = get_daily_fortune(selected_zodiac)

  st.success(f'🎉 **{selected_zodiac}**의 오늘의 운세가 도착했습니다!')

  # 운세 출력 카드 형식
  st.markdown(f'### 🌟 종합 운세: {fortune["level"]}')
  st.write(fortune['overall'])

  col1, col2 = st.columns(2)

  with col1:
    st.markdown('#### 💰 재물운')
    st.write(fortune['wealth'])

    st.markdown('#### ❤️ 연애운')
    st.write(fortune['love'])

  with col2:
    st.markdown('#### 💼 직장/학업운')
    st.write(fortune['work'])

  st.markdown('---')
  st.caption('※ 운세는 가벼운 재미로 참고하시고, 행복한 하루 보내세요!')