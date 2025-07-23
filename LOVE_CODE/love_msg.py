import streamlit as st

st.set_page_config(page_title ="Secret Love Message", page_icon=":heart:", layout = "crntered")

st.title("Secret Love Message")

for key, value in {
    "message": "",
    "secret_code": "",
    "mode": "send", 
    "message_saved": False,
}.items():
    st.session_state.setdefault(key, value)

mode = st.radio("Choose your mode:", ["Send a Message", "Receive a Message"])
st.session_state.mode = "send" if mode == "Send a Message" else "receive"

st.divider()

if st.session_state.mode == "send":
    st.subheader("compose your secret love message")
    with st.form("send_form"):
        secret = st.text_input("Set a secret passcode", type = "password")
        msg = st.text_area("Write your message of love")
        send_button = st.form_submit_button("Save secret message")

        if send_button and msg.strip() and secret.strip():
            st.session_state.secret_code = secret.strip()
            st.session_state.message = msg.strip()
            st.session_state.message_saved = True
            st.success("Message saved! You can now share the secret code with your loved one.")

elif st.session_state.mode == "receive":
    st.subheader("Enter secret code to unlock this message")

    if not st.session_state.message_saved:
        st.warning("No message is currently saved")

    else:
        entered_code = st.text_input("Enter the secret code", type = "password")
        if st.button ("unlock message"):
            if entered_code == st.session_state.secret_code:
                st.success("Message unlocked!")
                st.markdown(f"**Secret Message:**\n\n{st.session_state.message}")
            else:
                st.error("Incorrect secret code. Please try again.")

if st.button("clear all"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

                    