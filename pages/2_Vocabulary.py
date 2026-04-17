import streamlit as st

st.title("📚 HSK 5 Vocabulary")
st.subheader("Essential vocabulary for HSK 5 level")

st.write("Here you'll find organized vocabulary lists to help you master HSK 5 words.")

# Vocabulary categories
categories = {
    "Business & Work": [
        "会议 (huì yì) - meeting",
        "合同 (hé tong) - contract",
        "经理 (jīng lǐ) - manager",
        "发展 (fā zhǎn) - development",
        "投资 (tóu zī) - investment"
    ],
    "Education & Learning": [
        "研究 (yán jiū) - research",
        "学位 (xué wèi) - degree",
        "专业 (zhuān yè) - major/specialty",
        "课程 (kè chéng) - course",
        "知识 (zhī shi) - knowledge"
    ],
    "Environment & Nature": [
        "环境 (huán jìng) - environment",
        "污染 (wū rǎn) - pollution",
        "保护 (bǎo hù) - protection",
        "气候 (qì hòu) - climate",
        "资源 (zī yuán) - resources"
    ]
}

for category, words in categories.items():
    with st.expander(f"📖 {category}"):
        for word in words:
            st.write(f"• {word}")

st.info("💡 Tip: Practice these words daily and try to use them in sentences!")