import streamlit as st

st.title("📚 Resources & Tips")
st.subheader("Helpful resources for your Mandarin learning journey")

st.write("Here are some useful resources and study tips to accelerate your progress.")

# Study Tips
st.subheader("💡 Study Tips")

tips = [
    "**🎧 Listen Actively**: Watch Chinese dramas, listen to podcasts, and try to understand conversations",
    "**📝 Write Daily**: Keep a journal in Chinese to practice characters and sentence structure",
    "**🗣️ Speak Practice**: Find language exchange partners on apps like HelloTalk or Tandem",
    "**📖 Read Regularly**: Start with children's books, then move to news articles and novels",
    "**🔄 Review Consistently**: Use spaced repetition apps like Anki for vocabulary",
    "**🎯 Set Goals**: Break down HSK 5 into smaller milestones and celebrate achievements"
]

for tip in tips:
    st.write(f"• {tip}")

# Online Resources
st.subheader("🌐 Online Resources")

resources = {
    "Learning Platforms": [
        "[Duolingo Chinese](https://www.duolingo.com/) - Gamified learning",
        "[Memrise](https://www.memrise.com/) - Vocabulary building",
        "[Clozemaster](https://www.clozemaster.com/) - Contextual learning"
    ],
    "HSK Preparation": [
        "[HSK Academy](https://www.hsk.academy/) - Free HSK resources",
        "[ChinesePod101](https://www.chinesepod101.com/) - Comprehensive courses",
        "[Skritter](https://skritter.com/) - Character writing practice"
    ],
    "Media & Culture": [
        "[YouTube Chinese Channels](https://www.youtube.com/) - Search for 'Learn Chinese'",
        "[Netflix Chinese Shows](https://www.netflix.com/) - Mandarin with subtitles",
        "[CGTN](https://www.cgtn.com/) - Chinese news in English & Chinese"
    ]
}

for category, links in resources.items():
    with st.expander(f"📖 {category}"):
        for link in links:
            st.markdown(link)

# Progress Tracker
st.subheader("📊 Progress Tracker")

st.write("Track your daily learning progress:")

col1, col2, col3 = st.columns(3)

with col1:
    vocab_goal = st.number_input("Vocabulary words learned today", min_value=0, value=0)
with col2:
    study_time = st.slider("Study time (minutes)", 0, 240, 30)
with col3:
    confidence = st.selectbox("Today's confidence level", ["😟 Low", "😐 Medium", "😊 High", "🎉 Excellent"])

if st.button("Save Progress"):
    st.success("🎯 Progress saved! Keep up the great work!")

# Motivation
st.subheader("🚀 Stay Motivated")

st.info("""
**Remember:** Learning Chinese is a marathon, not a sprint. Progress might be slow at first,
but with consistent practice, you'll see amazing results. Every character you learn brings
you closer to fluency!

**Fun Fact:** Chinese has over 50,000 characters, but you only need about 2,500-3,000
for basic fluency, and HSK 5 requires around 2,500 words.
""")

st.balloons()