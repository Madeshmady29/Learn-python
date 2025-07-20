import streamlit as st

if 'word' not in st.session_state:
    st.session_state.word = ''
if 'clue' not in st.session_state:
    st.session_state.clue = ''
if 'guessed' not in st.session_state:
    st.session_state.guessed = False
if 'guess' not in st.session_state:
    st.session_state.guess = ''
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

st.title("2-palyer Word Guess Game")

st.markdown("### Player 1: Enter a secret word and a clue")

with st.form("setup_form"):
    word_input = st.text_input("Enter the secret word(Palyer 1):", type="password")
    clue_input = st.text_input("Enter a clue for the secret word(Palyer 1):")
    submitted = st.form_submit_button("submit")

    if submitted:
        st.session_state.word = word_input.lower().strip()
        st.session_state.clue = clue_input.strip()
        st.session_state.guessed = False
        st.session_state.attempts = 0
        st.success("word and clue set! Now Player 2 can guess. ")

if st.session_state.word:
    st.markdown("### player 2: Try to guess the secret word!")
    st.info(f"Clue: {st.session_state.clue}")

    guess_input = st.text_input("Enter your guess (Player 2)").lower()

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess_input == st.session_state.word:
            st.session_state.guessed = True
            st.success(f"Correct! The secret word was '{st.session_state.word}'. You guessed it in {st.session_state.attempts} tries.")

        else:
            st.error("Incorrect guess. Try again.")

        if not st.session_state.guessed and st.session_state.attempts > 0:
            st.write(f"Attempts: {st.session_state.attempts}")

if st.button("Reset Game"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
                                    

