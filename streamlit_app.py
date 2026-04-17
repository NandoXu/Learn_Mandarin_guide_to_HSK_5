import streamlit as st

st.title("ಠ_ಠ Mandarin guide to HSK 5 ಠ_ಠ")
st.subheader("Before you start")

intro_text = "First of all, I'm not a language teacher or a language expert. I'm just unemployed, went through depression, and chose to learn English and Mandarin after a year of it. I made this because I think these methods of learning language are worth sharing. I found this method to learn languages to be more effective than most templates or digital tools that would teach you Mandarin. \n\nI realized this method works because of my experiences in Surabaya, where I suddenly could speak Javanese (ngoko) naturally only through exposure. But exposure doesn't have to be natural—you can recreate it. You can use Discord and talk to strangers, watch movies in your target language, and train yourself directly in that language.\n\nSo I applied that insight to English and Mandarin, creating a faster, practical method."

st.write(intro_text)

# Start Learning Button
st.subheader("🚀 Ready to Start Learning?")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎓 START LEARNING HSK 1", type="primary", use_container_width=True):
        st.switch_page("pages/1_HSK_1.py")

st.info("💡 **Tip:** Start with HSK 1 if you're a complete beginner, or jump to higher levels if you already know some Mandarin!")
