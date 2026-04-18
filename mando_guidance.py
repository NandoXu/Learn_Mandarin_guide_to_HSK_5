import streamlit as st

# Initialize session state for HSK progress tracking
if 'hsk_completed' not in st.session_state:
    st.session_state.hsk_completed = {
        'hsk1': False,
        'hsk2': False,
        'hsk3': False,
        'hsk4': False,
        'hsk5': False
    }

# Hide the sidebar and the toggle button
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("ಠ_ಠ Mandarin guide to HSK 5 ಠ_ಠ")
st.markdown("<h1 style='font-size: 32px; font-weight: bold;'>HSK 5级汉语指南</h1>", unsafe_allow_html=True) 
st.subheader("Before you start")

intro_text = "First of all, I'm not a language teacher or a language expert. I'm just unemployed, went through depression, and chose to learn English and Mandarin after a year of it. I made this because I think these methods of learning language are worth sharing. I found this method to learn languages to be more effective than most templates or digital tools that would teach you Mandarin. \n\nI realized this method works because of my experiences in Surabaya, where I suddenly could speak Javanese (ngoko) naturally only through exposure. But exposure doesn't have to be natural—you can recreate it. You can use Discord and talk to strangers, watch movies in your target language, and train yourself directly in that language.\n\nSo I applied that insight to English and Mandarin, creating a faster, practical method."

st.write(intro_text)

# Start Learning Button
st.subheader("🚀 Choose Your Level 选择你的等级")

st.write("Complete levels in order to unlock the next ones:")

# HSK Level Buttons - All in unified layout
col1, col2 = st.columns(2)

with col1:
    # HSK 1 - Always unlocked
    if st.button("🎓 HSK 1 - Beginner\n(Basic greetings, numbers, simple sentences)", use_container_width=True):
        st.switch_page("pages/1_HSK_1.py")

    # HSK 3 - Locked until HSK 2 is completed
    hsk3_unlocked = st.session_state.hsk_completed['hsk2']
    if hsk3_unlocked:
        if st.button("🎓 HSK 3 - Intermediate\n(Opinions, comparisons, daily communication)", use_container_width=True):
            st.switch_page("pages/7_HSK_3.py")
    else:
        st.button("🔒 HSK 3 - Intermediate\n(Complete HSK 2 first)", disabled=True, use_container_width=True)

    # HSK 5 - Locked until HSK 4 is completed
    hsk5_unlocked = st.session_state.hsk_completed['hsk4']
    if hsk5_unlocked:
        if st.button("🎓 HSK 5 - Advanced Fluency\n(Native-like proficiency, complex topics)", use_container_width=True):
            st.switch_page("pages/9_HSK_5.py")
    else:
        st.button("🔒 HSK 5 - Advanced Fluency\n(Complete HSK 4 first)", disabled=True, use_container_width=True)

with col2:
    # HSK 2 - Locked until HSK 1 is completed
    hsk2_unlocked = st.session_state.hsk_completed['hsk1']
    if hsk2_unlocked:
        if st.button("🎓 HSK 2 - Elementary\n(Time, food, places, questions)", use_container_width=True):
            st.switch_page("pages/6_HSK_2.py")
    else:
        st.button("🔒 HSK 2 - Elementary\n(Complete HSK 1 first)", disabled=True, use_container_width=True)

    # HSK 4 - Locked until HSK 3 is completed
    hsk4_unlocked = st.session_state.hsk_completed['hsk3']
    if hsk4_unlocked:
        if st.button("🎓 HSK 4 - Upper Intermediate\n(Complex sentences, abstract concepts)", use_container_width=True):
            st.switch_page("pages/8_HSK_4.py")
    else:
        st.button("🔒 HSK 4 - Upper Intermediate\n(Complete HSK 3 first)", disabled=True, use_container_width=True)

st.info("💡 **Level Guide:**\n• **HSK 1-2**: Basic communication\n• **HSK 3-4**: Practical fluency\n• **HSK 5**: Professional/academic level")
st.info("💡 **级别指南:**\n• **HSK 1-2**: 基础交流\n• **HSK 3-4**: 实用流利\n• **HSK 5**: 专业/学术水平")   