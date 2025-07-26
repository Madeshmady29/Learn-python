import streamlit as st

st.set_page_config(page_title="Word Game Guess", page_icon="🎲", layout = "centered")
st.title("2-PLAYER WORD GUESS CHALLENGE")
for key, value in {'word': '', 'clue': '', 'guessed': False, 'guesss': '', 'attempts': 0, 'history': [], 'setup_done': False}.items():
    st.session_state.setdefault(key, value)

#player 1 sets the word and clue
if not st.session_state.setup_done:
    with st.expander("Player 1: set the word", expanded=True):
        with st.form("setup_form"):
            st.subheader("Playar 1: Set the secret word and a clue")
            word_input = st.text_input("Enter secret word", type = "password")
            clue_input = st.text_input("Enter a clue for the word")
            submitted = st.form_submit_button("Set Word")

            if submitted and word_input.strip() and clue_input.strip():
                st.session_state.word = word_input.lower().strip()
                st.session_state.clue = clue_input.strip()
                st.session_state.guessed = False
                st.session_state.attempts = 0
                st.session_state.history = []
                st.success("Word & clue set! Player 2 can guess now!")
                #st.session_state.setup_done = True
                #st.stop()

#player 2 guesses the word
if st.session_state.setup_done:
    st.divider()
    st.subheader("### Player 2: Guess the word!")
    st.info(f"Clue: {st.session_state.clue}")
    st.write(f"The word has **{len(st.session_state.word)} letters**.")
    
    with st.form('guess_form'):
        guess_input = st.text_input("Your guess").lower()
        guess_submit = st.form_submit_button("Submit Guess")

        if guess_submit and guess_input:
            st.session_state.attempts += 1
            st.session_state.history.append(guess_input)
            
            if guess_input == st.session_state.word:
                st.session_state.guessed = True
                st.success(f"Congratulations! You've guessed the word {st.session_state.attempts} attempts.")

            else:
                st.error("Incorrect guess. Try again!")

    if not st.session_state.guessed and st.session_state.attempts > 0:
        st.write(f"attempts: {st.session_state.attempts}")
        st.markdown("### Previous Guesses: ")
        st.write(st.session_state.history)

if st.button("Reset Game"):
    #keys_to_reset = ["word", "clue", "guessed", "guess", "attempts", "history"]
    for key in list(st.session_state.keys()):
        #if key in st.session_state:
        del st.session_state[key]
    st.rerun()