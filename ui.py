import streamlit as st
from youtube_analyzer import build_youtube_agent

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="AI YouTube Analyzer",
    page_icon="🎬",
    layout="centered"
)

# ------------------- CUSTOM STYLING -------------------
page_bg = """
<style>

/* Background with AI feel */
.stApp {
    background: radial-gradient(circle at top, #0f2027, #0b1a1f, #000000);
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

/* Glass Card */
.main-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 16px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.5);
}

/* Title */
.big-title {
    font-size: 38px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #a0b3c2;
    margin-bottom: 25px;
}

/* Input */
.stTextInput>div>div>input {
    background-color: #111;
    color: white;
    border: 1px solid #333;
    padding: 12px;
    border-radius: 10px;
}

/* Modern Button */
.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 10px;
    padding: 0.7rem 1.5rem;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ff4b2b, #ff416c);
}

/* Wave Loader (AI Processing style) */
.wave {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.wave div {
  width: 6px;
  height: 20px;
  margin: 3px;
  background: #ff4b2b;
  animation: wave 1s infinite ease-in-out;
}

.wave div:nth-child(2) { animation-delay: 0.1s; }
.wave div:nth-child(3) { animation-delay: 0.2s; }
.wave div:nth-child(4) { animation-delay: 0.3s; }
.wave div:nth-child(5) { animation-delay: 0.4s; }

@keyframes wave {
  0%, 100% { height: 10px; }
  50% { height: 30px; }
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ------------------- HEADER -------------------
st.markdown('<div class="big-title">🎬 AI YouTube Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste a video link and let AI break it down for you</div>', unsafe_allow_html=True)

# ------------------- MAIN CARD -------------------
st.markdown('<div class="main-card">', unsafe_allow_html=True)

# ------------------- AGENT -------------------
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# ------------------- INPUT -------------------
video = st.text_input(
    "Enter YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=..."
)

analyze = st.button("🚀 Analyze Video")

# ------------------- PROCESSING + OUTPUT -------------------
if video and analyze:
    loader_placeholder = st.empty()

    # Wave animation loader
    loader_placeholder.markdown("""
    <div class="wave">
        <div></div><div></div><div></div><div></div><div></div>
    </div>
    <p style='text-align:center; color:#aaa;'>Analyzing video with AI...</p>
    """, unsafe_allow_html=True)

    response = agent.run(f"analyze this video: {video}")

    loader_placeholder.empty()

    st.subheader("📊 Analysis Report")
    st.markdown(response.content)

st.markdown('</div>', unsafe_allow_html=True)