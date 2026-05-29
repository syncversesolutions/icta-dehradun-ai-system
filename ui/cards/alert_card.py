import streamlit as st


def render_alert(alert):

    st.markdown(f"""

    <div class="alert-card">

        <h4>{alert['title']}</h4>

        <p>{alert['message']}</p>

        <small>{alert['location']}</small>

    </div>

    """, unsafe_allow_html=True)