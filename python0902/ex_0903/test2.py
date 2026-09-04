import streamlit as st
import time

placeholder = st.empty()

with placeholder.container() :
    st.write("how are you?")

    sentiment_mapping = ["so bad", "bad", "so so", "good", "great"]
    selected = st.feedback("faces")

    if selected is not None:
        time.sleep(0.5)
        st.write("goooood")
        time.sleep(2)
        st.write("then..")
        time.sleep(2)
        st.write("join with us?")
        time.sleep(1)

        global submit
        submit = st.button("JOIN", type="primary") 
        if submit :
            time.sleep(0.1)
            st.title(":red[WELCOME]")
            time.sleep(0.1)
            st.title(":red[WELCOME]")
            time.sleep(0.1)
            st.title(":red[WELCOME]")
            time.sleep(0.1)
            st.title(":red[WELCOME]")
            time.sleep(0.1)

            placeholder.empty()

            time.sleep(2)
            with placeholder.container() : 
                prompt = st.chat_input("welcome :)")
                if prompt:
                    st.write(prompt)



