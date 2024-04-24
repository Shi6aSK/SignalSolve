import streamlit as st


def page_meta(page_title: str, page_icon, layout="wide", show_title=True, is_under_construction=False):
    st.set_page_config(page_title=f"Signal Solve | {page_title}", page_icon=page_icon, layout=layout)
