import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# credentials
page_title = st.secrets['initialize']['page_title']
sidebar_title = st.secrets['initialize']['sidebar_title']
website = st.secrets['credits']['website']
name = st.secrets['credits']['name']
buymeacoffee = st.secrets['credits']['buymeacoffee']
api_key = st.secrets['api_key']
api_secret = st.secrets['api_secret']

# streamlit
st.set_page_config(
    '{}'.format(page_title),
    ':moneybag:',
    layout='centered',
    initial_sidebar_state='collapsed',
    menu_items={
        "Get Help": "https://hirawat.in",
        "About": "Fantasy Sports App",
    },
)
st.title(':star: ' + page_title )
st.sidebar.title(':cyclone: ' +  sidebar_title)

# footer & credits section
def footer():
    st.markdown('<div style="text-align: center">Made with ❤️ by <a href="{}">{}</a></div>'.format(website, name), unsafe_allow_html=True)
    with st.sidebar.expander("Credits", expanded=True):
        components.html(
            '{}'.format(buymeacoffee),
            height=80
        )


# google form inputs processing
def top_players():

    df = pd.read_csv("./data/leaderboard-demo.csv")
    return df
# widget
tab1, tab2, tab3, tab4 = st.tabs(["Leaderboard", "Points Table", "Team Standings", "Team Info"])

with tab1:
    st.header("🌟 LeaderBoard")
    st.markdown("""
    > Last Updated: Match 0
    """)
    df = top_players()
    st.dataframe(df)

with tab2:
    st.header("Points for categories")
    df = pd.read_csv("./data/points.csv")
    st.dataframe(df)

with tab3:
    st.header("Team Standings")
    df = pd.read_csv("./data/team-standings.csv")
    st.dataframe(df)

def main() -> None:
    # Start Writing Code Here
    with st.expander("Rules"):
        st.markdown("""
        ### 1. Only combinations of **unique** email-id, phone no. & name will be selected for the final entries.
        ### 2. In case of a points draw - the fastest entry will be selected.
        > Scores are updated after every match. 
        """)

    #st.markdown('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSedLYR3Ye77ie5qFozkBBUGFJIdgWn3Qy65475kkt8l0gXoBA/viewform?embedded=true" width="1000" height="600" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)
    st.markdown("""
    # 🔮 Select your picks - [Fill this form](https://docs.google.com/forms/d/e/1FAIpQLSedLYR3Ye77ie5qFozkBBUGFJIdgWn3Qy65475kkt8l0gXoBA/viewform)
    ---
    # 🎁 Top 3 with highest points will get special prizes
    """)
    #footer()

if __name__ == '__main__':
    main()
