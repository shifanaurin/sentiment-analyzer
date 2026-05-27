import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        return "😊 Positive", polarity, "#00C851"
    elif polarity < -0.1:
        return "😠 Negative", polarity, "#ff4444"
    else:
        return "😐 Neutral", polarity, "#ffbb33"

# Page config
st.set_page_config(page_title="Social Media Sentiment Analyzer", page_icon="💬")

# Header
st.title("💬 Social Media Sentiment Analyzer")
st.subheader("Paste any comment and find out if it's positive, negative or neutral!")

# Input
comment = st.text_area("Paste your social media comment here:", height=150, placeholder="Type or paste a comment...")

if st.button("Analyze Sentiment"):
    if comment.strip():
        sentiment, score, color = analyze_sentiment(comment)
        
        st.markdown("---")
        st.markdown(f"### Result:")
        st.markdown(f"<h2 style='color:{color}'>{sentiment}</h2>", unsafe_allow_html=True)
        
        st.markdown(f"**Polarity Score:** {score:.2f}")
        st.progress(float((score + 1) / 2))
        
        if score > 0.1:
            st.success("This comment has a positive tone! 🎉")
        elif score < -0.1:
            st.error("This comment has a negative tone! ⚠️")
        else:
            st.warning("This comment has a neutral tone. 😐")
            
        st.markdown("---")
        st.caption("Score ranges from -1 (very negative) to +1 (very positive)")
    else:
        st.error("Please enter a comment to analyze!")