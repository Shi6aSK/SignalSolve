import streamlit as st
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://lh3.googleusercontent.com/pw/AP1GczOi_f5UL6xDwd0nx649CG_8kUNCEGiZm-AlyeE3HXnO-4WtcGKy4f4avzSPrNDZIr64HlN7gllMSF0Priee_nS8lyTVObepujtlSKHWE9ypzTBxvmNqKdAQBeoCY9Lm25kkU3M5kqGmh4Cadl-AytAgxEwsdlHE2-6x_7FdFLAAQ9Di_xQbwj_PdRQ9nzwAbq4Hyku3g93f0E6FqZZWUtv2wI8pJ5D3KFArScX05rMbE7-7Y9mGm-nEzXMoFaxlipxBw14vH14xLCcG0TFz_T-10HOnbasSbKWIrF-rQD97EPjK-eCx-OqXQrm3y5Mm7-2dHZz7p2wQMTYoM4wI2dPqfHTHRjBuBQz06hq5sZYxPk5Kdlmt98TPo7lNZxKXwZpkddMxqzVXzKOYOKAKZvBfxhcqLcZwb14VhKXJEfGj0W8c6draXzDWWN8l1M7FzV2TwV-V3xDnLe1ltOHB_X7mENWXZYsBKlRvDQWKfPqd7D9_aq3MlrXz18QMg4yBpeLtxLa6KFfK3soYH0vpkZaa0_S2iD5ON4FH6M5YODsUY3TCi8-cF1DEIln3h5vRkPJhtmVT---N9BTuqEq_npbTYA1Jv57od80VrIKBExd0xqJpi0ER9IoS9THbVxL-CHUPTKHqjJj4XGp0Ouu6WTEp-h0Fem5kA9d3mAf8RhkCE_JJXW7O3nTCx1EcDdUE5qW9blk2pTI7IrSa_drTAjPSj0qRlcn-JOGwNM49NnQTbLGSlcQhGGnr7qWO4MbgvlP0y9i794NvqCMWmWm-Zy0cCPjbqHQmrPP73Ifykb0JCoEhS4afOJEEy34KhxAsT2KmY5TyxSnlkC4f7TOWZ7ZdQcokkIgXSKMPbZLAkjJnmxrgHJL9BY8uBm9MdcvzHbdX5wclMh8VKjxvoGKoytW8EFlB39ZV_Bel_Xovq-iZUOqSY0KdSH1lu2ZjtExx_k79cMKFWmdI6J03pX2GtPE=w1280-h832-s-no-gm?authuser=0");
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

st.write("An AI aid for your microphone which separates you from the noisy environment and helps boost your productivity.")