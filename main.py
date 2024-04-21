import streamlit as st
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://raw.githubusercontent.com/Shi6aSK/SignalSolve/main/pages/Try%20Online.png");
background-size: 110%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("SignalSolve")

st.write("## An AI aid for your microphone which separates you from the noisy environment and helps boost your productivity.")
# Add a download button in the sidebar
st.sidebar.markdown("""
<a href="https://download.krisp.ai/win" download>
    <button>Download</button>
</a>
""", unsafe_allow_html=True)