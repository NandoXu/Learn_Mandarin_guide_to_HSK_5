import streamlit as st

st.title("📖 HSK 5 Grammar")
st.subheader("Advanced grammar patterns for HSK 5")

st.write("Master these essential grammar structures to reach HSK 5 proficiency.")

# Grammar sections
grammar_topics = {
    "Complex Sentence Structures": {
        "description": "Advanced ways to connect ideas",
        "examples": [
            "**把 (bǎ)** - Used to emphasize the object\n• 我把作业做完了 (I finished my homework)",
            "**被 (bèi)** - Passive voice\n• 书被他拿走了 (The book was taken by him)",
            "**比 (bǐ)** - Comparison\n• 北京比上海大 (Beijing is bigger than Shanghai)"
        ]
    },
    "Advanced Particles": {
        "description": "Particles that add nuance to sentences",
        "examples": [
            "**了 (le)** - Completed action\n• 我吃完了饭 (I finished eating)",
            "**着 (zhe)** - Ongoing action\n• 他正看着书 (He is reading a book)",
            "**过 (guo)** - Past experience\n• 我去过中国 (I have been to China)"
        ]
    },
    "Subjunctive Mood": {
        "description": "Expressing wishes, suggestions, and hypotheticals",
        "examples": [
            "**如果...就... (rú guǒ...jiù...)** - If...then...\n• 如果下雨，我们就待在家 (If it rains, we'll stay home)",
            "**宁可...也不... (nìng kě...yě bù...)** - Rather...than...\n• 宁可走路也不坐公交 (I'd rather walk than take the bus)"
        ]
    }
}

for topic, content in grammar_topics.items():
    with st.expander(f"🔍 {topic}"):
        st.write(content["description"])
        st.write("**Examples:**")
        for example in content["examples"]:
            st.write(example)
        st.write("---")

st.success("🎯 Practice these patterns regularly to improve your Chinese grammar skills!")