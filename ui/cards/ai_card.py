import streamlit as st


def render_ai_card(recommendation):

    st.markdown(f"""

    <div class="metric-card">

        <h4>{recommendation['title']}</h4>

        <p>{recommendation['reason']}</p>

        <p><b>Impact:</b> {recommendation['impact']}</p>

        <p><b>Confidence:</b> {recommendation['confidence']}</p>

    </div>

    """, unsafe_allow_html=True)