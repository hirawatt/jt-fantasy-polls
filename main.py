import streamlit as st
import streamlit.components.v1 as components

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
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        "Get Help": "https://hirawat.in",
        "About": "Boilerplate streamlit app",
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


# widget

def main() -> None:
    # Start Writing Code Here
    st.markdown('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSedLYR3Ye77ie5qFozkBBUGFJIdgWn3Qy65475kkt8l0gXoBA/viewform?embedded=true" width="1000" height="600" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)
    #footer()

if __name__ == '__main__':
    main()
